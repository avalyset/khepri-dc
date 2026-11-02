"""Bygger bearbeidede timeserier fra rå ENTSO-E-XML (som ikke committes) til parquet i data/.

- produksjon_A75.parquet: time_utc, sone, produksjon_MW (sum over produksjonstyper med verdi i timen;
  NaN hvis ingen type har verdi), n_typer. Kun TimeSeries med inBiddingZone_Domain (produksjon).
- last_A65.parquet: time_utc, sone, last_MW (A65, processType A16).
- flyt_A11.parquet: time_utc, fra, til, flyt_MW (fysisk flyt, out_Domain=fra, in_Domain=til).
Alle timer i UTC, 2023–2025, varighetsvektet timemiddel av A03-ekspanderte intervaller (khepri_dc.entsoe_xml).
Skriptet skriver bare tellinger (rader, manglende timer, konflikter) — aldri verdier eller summer.

Bruk: python -m build.build_series <raw-katalog> <ut-katalog>
"""
import glob
import json
import os
import sys

import pandas as pd

from khepri_dc import entsoe_xml as X

ZONES = {"NO_1": "NO1", "NO_2": "NO2", "NO_3": "NO3", "NO_4": "NO4", "NO_5": "NO5"}
BORDERS = ("NO_1-NO_2 NO_1-NO_3 NO_1-NO_5 NO_1-SE_3 NO_2-NO_5 NO_2-DK_1 NO_2-DE_LU NO_2-NL NO_2-GB NO_3-NO_4 "
           "NO_3-NO_5 NO_3-SE_2 NO_4-SE_1 NO_4-SE_2 NO_4-FI").split()
YEARS = (2023, 2024, 2025)


def navn(k):
    return ZONES.get(k, k.replace("_", ""))


def filer(raw, serie, key, y):
    return sorted(glob.glob(os.path.join(raw, serie, f"{serie}_{key}_{y}*.xml")))


def main(raw, ut):
    os.makedirs(ut, exist_ok=True)
    tell = {"A75": {}, "A65": {}, "A11": {}}
    P, Lr, F = [], [], []
    for y in YEARS:
        # A75
        for k, z in ZONES.items():
            fs = filer(raw, "A75", k, y)
            n_forbruk = 0

            def keyfn(a):
                nonlocal n_forbruk
                if "outBiddingZone_Domain.mRID" in a and "inBiddingZone_Domain.mRID" not in a:
                    n_forbruk += 1
                    return None
                return a.get("psrType")
            h, konf = X.collect({k: fs}, y, keyfn)
            typer = pd.DataFrame({sub: s for (_, sub), s in h.items()})
            prod = typer.sum(axis=1, min_count=1)
            P.append(pd.DataFrame({"time_utc": prod.index, "sone": z, "produksjon_MW": prod.values,
                                   "n_typer": typer.notna().sum(axis=1).values}))
            tell["A75"][f"{z}_{y}"] = {"filer": len(fs), "typer": len(typer.columns), "timer": int(len(prod)),
                                       "manglende_timer": int(prod.isna().sum()),
                                       "timer_ikke_alle_typer": int((typer.notna().sum(axis=1) < len(typer.columns)).sum()),
                                       "forbruksserier_utelatt": n_forbruk, "konflikter": int(sum(konf.values()))}
        # A65
        for k, z in ZONES.items():
            fs = filer(raw, "A65", k, y)
            h, konf = X.collect({k: fs}, y, lambda a: "last")
            s = h[(k, "last")]
            Lr.append(pd.DataFrame({"time_utc": s.index, "sone": z, "last_MW": s.values}))
            tell["A65"][f"{z}_{y}"] = {"filer": len(fs), "timer": int(len(s)), "manglende_timer": int(s.isna().sum()),
                                       "konflikter": int(sum(konf.values()))}
        # A11
        for b in BORDERS:
            a, c = b.split("-", 1)
            for fra, til in ((a, c), (c, a)):
                key = f"{fra}__{til}"
                fs = filer(raw, "A11", key, y)
                h, konf = X.collect({key: fs}, y, lambda at: "flyt")
                s = h.get((key, "flyt"), X.to_hourly(pd.DataFrame(columns=["v", "res"]), y))
                F.append(pd.DataFrame({"time_utc": s.index, "fra": navn(fra), "til": navn(til), "flyt_MW": s.values}))
                tell["A11"][f"{navn(fra)}->{navn(til)}_{y}"] = {"filer": len(fs), "timer": int(len(s)),
                                                                "manglende_timer": int(s.isna().sum()),
                                                                "konflikter": int(sum(konf.values()))}
    pd.concat(P, ignore_index=True).to_parquet(os.path.join(ut, "produksjon_A75.parquet"), index=False)
    pd.concat(Lr, ignore_index=True).to_parquet(os.path.join(ut, "last_A65.parquet"), index=False)
    pd.concat(F, ignore_index=True).to_parquet(os.path.join(ut, "flyt_A11.parquet"), index=False)
    json.dump(tell, open(os.path.join(ut, "BYGGTELLING.json"), "w"), indent=1, ensure_ascii=False, sort_keys=True)
    for serie, d in tell.items():
        mangl = sum(v["manglende_timer"] for v in d.values()); konf = sum(v["konflikter"] for v in d.values())
        print(f"{serie}: {len(d)} serie-år, manglende timer totalt {mangl}, konflikter {konf}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
