"""Utforskende, ikke preregistrert (A-DC2 steg 2 og 3a).
D_t = NP(A11) − NP(A75−A65) per sone og UTC-time. Skjevhet (middel), median, andel D > 0, årssum (TWh), middel |D|.
Pumpeforbruk: A75-forbruksserier (outBiddingZone, B10/B18) fra rå XML for 2025, timeaggregert som i build_series.
Bruk: python -m diagnose.avvik_d <raw> <ut-katalog>"""
import glob, os, sys
import numpy as np
import pandas as pd
from khepri_dc import analysis as A
from khepri_dc import entsoe_xml as X

raw, ut = sys.argv[1], sys.argv[2]
os.makedirs(ut, exist_ok=True)
NP = A.les_np("data"); flyt = pd.read_parquet("data/flyt_A11.parquet")
rows, D_all = [], {}
for z in A.ZONES:
    d = (A.np_a11(flyt, z) - NP[z]).dropna(); D_all[z] = d
    for y in A.YEARS:
        e = d[d.index.year == y]
        rows.append({"sone": z, "aar": y, "timer": len(e), "middel_D_MW": e.mean(), "median_D_MW": e.median(),
                     "andel_D_pos_pct": (e > 0).mean() * 100, "sum_D_TWh": e.sum() / 1e6, "middel_abs_D_MW": e.abs().mean(),
                     "sd_D_MW": e.std()})
dt = pd.DataFrame(rows); dt.to_csv(f"{ut}/avvik_D.csv", index=False, float_format="%.6f")

# pumpeforbruk (A75 forbruksserier), 2025
prow = []
for k, z in {"NO_2": "NO2", "NO_3": "NO3", "NO_5": "NO5"}.items():
    for y in A.YEARS:
        fs = sorted(glob.glob(os.path.join(raw, "A75", f"A75_{k}_{y}*.xml")))
        def keyfn(a):
            return a.get("psrType") if ("outBiddingZone_Domain.mRID" in a and "inBiddingZone_Domain.mRID" not in a) else None
        h, _ = X.collect({k: fs}, y, keyfn)
        for (_, psr), s in h.items():
            d = D_all[z][D_all[z].index.year == y]
            j = pd.concat([d.rename("D"), s.rename("p")], axis=1).dropna()
            prow.append({"sone": z, "aar": y, "psrType": psr, "timer_med_verdi": int(s.notna().sum()),
                         "sum_pumpe_TWh": s.sum() / 1e6, "sum_D_samme_timer_TWh": j["D"].sum() / 1e6,
                         "r_D_mot_pumpe": j["D"].corr(j["p"]) if len(j) > 2 else np.nan,
                         "middel_D_naar_pumpe_gt0": j.loc[j["p"] > 0, "D"].mean(),
                         "middel_D_naar_pumpe_0": j.loc[j["p"] <= 0, "D"].mean()})
pt = pd.DataFrame(prow); pt.to_csv(f"{ut}/pumpe_2025.csv", index=False, float_format="%.6f")
pd.set_option("display.width", 200)
print(dt.round(3).to_string(index=False)); print(); print(pt.round(4).to_string(index=False))
