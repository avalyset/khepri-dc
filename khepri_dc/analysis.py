"""KHEPRI-DC v1 — preregistrert analyse (deskriptiv, deterministisk, i ettertid).

NP_t = produksjon_t (sum A75 alle typer) − last_t (A65 faktisk totallast), MW, per budområde og UTC-time.
Lagt på flat datasenterlast i år y og scenario s (MW):
    L_{s,y} = (E_ref − E_y) + b × (w_s × R_new + q_s × Q),   R_new = max(0, R − E_ref / b),   b = 0,70
S0 er observert (L = 0). Kurve: w = q = f, f = 0,00–1,00 i steg 0,01 (løftet E_ref − E_y er med).
Utfall per sone, år, scenario: (i) andel timer med NP − L < 0; (ii) samme for desember–februar i året;
(iii) årlig sum NP − L (TWh); (iv) laveste timeverdi NP − L (MW); (v) endring mot S0.
Kontroll: NP_A11 = Σ flyt ut − Σ flyt inn over sonens egne grenser, mot NP: middel absolutt avvik (MAE),
MAE / middel |NP| og Pearson r. Grense: MAE / middel |NP| ≤ 0,05.

Bruk: python -m khepri_dc.analysis --data data --params params/parametre.json --out results
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os

import numpy as np
import pandas as pd

ZONES = ["NO1", "NO2", "NO3", "NO4", "NO5"]
YEARS = [2023, 2024, 2025]
SCENARIOS = {  # navn: (w, q)
    "S0": None,
    "S1": (0.25, 0.0),
    "S2": (1.0, 0.0),
    "S3": (1.0 / 3.0, 1.0 / 3.0),
    "S4": (1.0, 1.0),
}
F_GRID = np.round(np.arange(0, 101) / 100.0, 2)
KONTROLL_GRENSE = 0.05
VINTER = (12, 1, 2)


# ---------- kjerneberegninger (rene funksjoner, testet på syntetiske data) ----------

def r_new(R: float, E_ref: float, b: float) -> float:
    return max(0.0, R - E_ref / b)


def last_paalagt(E_ref: float, E_y: float, R: float, Q: float, w: float, q: float, b: float) -> float:
    return (E_ref - E_y) + b * (w * r_new(R, E_ref, b) + q * Q)


def utfall(np_t: pd.Series, L: float) -> dict:
    """np_t: NP per UTC-time (MW), NaN for timer uten gyldig verdi. L: flat påslag (MW)."""
    d = (np_t - L).dropna()
    vin = d[d.index.month.isin(VINTER)]
    return {
        "timer": int(d.size),
        "andel_under0_pct": float((d < 0).mean() * 100) if d.size else float("nan"),
        "vinter_timer": int(vin.size),
        "vinter_andel_under0_pct": float((vin < 0).mean() * 100) if vin.size else float("nan"),
        "sum_TWh": float(d.sum() / 1e6),
        "min_MW": float(d.min()) if d.size else float("nan"),
    }


def kurve(np_t: pd.Series, E_ref: float, E_y: float, R: float, Q: float, b: float) -> pd.DataFrame:
    rows = []
    for f in F_GRID:
        L = last_paalagt(E_ref, E_y, R, Q, f, f, b)
        u = utfall(np_t, L)
        rows.append({"f": float(f), "L_MW": L, **u})
    return pd.DataFrame(rows)


def minste_f(kv: pd.DataFrame) -> tuple:
    """(minste f der sum_TWh ≤ 0, minste f der vinterandel > 50 %); None = ikke nådd."""
    a = kv.loc[kv["sum_TWh"] <= 0, "f"]
    c = kv.loc[kv["vinter_andel_under0_pct"] > 50, "f"]
    return (float(a.iloc[0]) if len(a) else None, float(c.iloc[0]) if len(c) else None)


def np_a11(flyt: pd.DataFrame, sone: str) -> pd.Series:
    """flyt: kolonner time_utc, fra, til, flyt_MW (lang form). Σ ut − Σ inn over sonens egne grenser.
    Timen blir NaN hvis én av sonens retninger mangler."""
    ut = flyt[flyt["fra"] == sone].pivot(index="time_utc", columns="til", values="flyt_MW")
    inn = flyt[flyt["til"] == sone].pivot(index="time_utc", columns="fra", values="flyt_MW")
    return ut.sum(axis=1, min_count=ut.shape[1]) - inn.sum(axis=1, min_count=inn.shape[1])


def kontroll(np_t: pd.Series, np_x: pd.Series) -> dict:
    j = pd.concat([np_t.rename("a"), np_x.rename("b")], axis=1).dropna()
    mae = float((j["a"] - j["b"]).abs().mean())
    ref = float(j["a"].abs().mean())
    return {"timer": int(len(j)), "MAE_MW": mae, "middel_abs_NP_MW": ref,
            "rel": mae / ref if ref else float("nan"), "r": float(j["a"].corr(j["b"])),
            "innenfor": bool(mae / ref <= KONTROLL_GRENSE) if ref else False}


# ---------- kjøring ----------

def _sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def _fmt(x, nd):
    if x is None:
        return "ikke nådd"
    if isinstance(x, float) and np.isnan(x):
        return "–"
    return f"{x:.{nd}f}"


def les_np(data: str) -> dict:
    prod = pd.read_parquet(os.path.join(data, "produksjon_A75.parquet"))
    last = pd.read_parquet(os.path.join(data, "last_A65.parquet"))
    out = {}
    for z in ZONES:
        p = prod[prod["sone"] == z].set_index("time_utc")["produksjon_MW"]
        l = last[last["sone"] == z].set_index("time_utc")["last_MW"]
        out[z] = (p - l).sort_index()
    return out


def kjor(data: str, params_path: str, outdir: str) -> None:
    P = json.load(open(params_path))
    b = P["brukstid"]
    np_all = les_np(data)
    flyt = pd.read_parquet(os.path.join(data, "flyt_A11.parquet"))
    os.makedirs(outdir, exist_ok=True)

    def ey(z, y, variant):
        return 0.0 if variant == "E0" else P["E_MW"][z][str(y)]

    def eref(z, variant):
        return 0.0 if variant == "E0" else P["E_MW"][z][str(P["E_ref_aar"])]

    scen_rows, kurve_rows, f_rows, kontroll_rows = [], [], [], []
    for variant in ("hoved", "E0"):
        for y in YEARS:
            for z in ZONES:
                s = np_all[z]
                s = s[s.index.year == y]
                R, Q = P["R_MW"][z], P["Q_MW"][z]
                E_ref, E_y = eref(z, variant), ey(z, y, variant)
                base = utfall(s, 0.0)
                for sn, wq in SCENARIOS.items():
                    L = 0.0 if wq is None else last_paalagt(E_ref, E_y, R, Q, wq[0], wq[1], b)
                    u = base if wq is None else utfall(s, L)
                    scen_rows.append({"variant": variant, "aar": y, "sone": z, "scenario": sn, "L_MW": L, **u,
                                      "d_andel_pp": u["andel_under0_pct"] - base["andel_under0_pct"],
                                      "d_vinter_pp": u["vinter_andel_under0_pct"] - base["vinter_andel_under0_pct"],
                                      "d_sum_TWh": u["sum_TWh"] - base["sum_TWh"],
                                      "d_min_MW": u["min_MW"] - base["min_MW"]})
                kv = kurve(s, E_ref, E_y, R, Q, b)
                kv.insert(0, "sone", z); kv.insert(0, "aar", y); kv.insert(0, "variant", variant)
                kurve_rows.append(kv)
                fa, fb = minste_f(kv)
                f_rows.append({"variant": variant, "aar": y, "sone": z, "f_sum_le0": fa, "f_vinter_gt50": fb})
    for y in YEARS:
        for z in ZONES:
            s = np_all[z]; s = s[s.index.year == y]
            x = np_a11(flyt, z); x = x[x.index.year == y]
            kontroll_rows.append({"aar": y, "sone": z, **kontroll(s, x)})

    sc = pd.DataFrame(scen_rows); kv = pd.concat(kurve_rows, ignore_index=True)
    fr = pd.DataFrame(f_rows); ko = pd.DataFrame(kontroll_rows)
    sc.to_csv(os.path.join(outdir, "scenarier.csv"), index=False, float_format="%.6f")
    kv.to_csv(os.path.join(outdir, "kurve.csv"), index=False, float_format="%.6f")
    fr.to_csv(os.path.join(outdir, "minste_f.csv"), index=False, float_format="%.2f")
    ko.to_csv(os.path.join(outdir, "kontroll.csv"), index=False, float_format="%.6f")
    skriv_md(sc, fr, ko, P, data, params_path, os.path.join(outdir, "RESULTATER_KHEPRI-DC_v1_2026-11-02.md"))
    figurer(kv, outdir)


def skriv_md(sc, fr, ko, P, data, params_path, path):
    L = ["# RESULTATER — KHEPRI-DC v1 (2026-11-02)", "",
         "Generert av khepri_dc/analysis.py (uendret etter tagg prereg-v1). Deskriptivt, i ettertid; ikke en prognose.", "",
         "## Inndata (sha256)", ""]
    for f in ("produksjon_A75.parquet", "last_A65.parquet", "flyt_A11.parquet"):
        L.append(f"- `{f}`: `{_sha(os.path.join(data, f))}`")
    L.append(f"- `{os.path.basename(params_path)}`: `{_sha(params_path)}`")
    L += ["", "Tolkning: netto import er ikke mangel eller rasjonering (se PREREG, tolkningsregler).", ""]
    for variant, tittel in (("hoved", "Hovedanalyse (E fra Elhub per prisområde)"), ("E0", "Sensitivitet E = 0")):
        L += [f"## {tittel}", ""]
        for y in YEARS:
            L += [f"### {y}", "",
                  "| Sone | Scenario | L (MW) | Timer | (i) andel NP−L<0 (%) | (ii) des–feb (%) | (iii) sum (TWh) | (iv) min (MW) | Δ(i) pp | Δ(ii) pp | Δ(iii) TWh | Δ(iv) MW |",
                  "|---|---|---|---|---|---|---|---|---|---|---|---|"]
            d = sc[(sc["variant"] == variant) & (sc["aar"] == y)]
            for _, r in d.iterrows():
                L.append(f"| {r.sone} | {r.scenario} | {_fmt(r.L_MW,1)} | {r.timer} | {_fmt(r.andel_under0_pct,2)} | "
                         f"{_fmt(r.vinter_andel_under0_pct,2)} | {_fmt(r.sum_TWh,3)} | {_fmt(r.min_MW,0)} | "
                         f"{_fmt(r.d_andel_pp,2)} | {_fmt(r.d_vinter_pp,2)} | {_fmt(r.d_sum_TWh,3)} | {_fmt(r.d_min_MW,0)} |")
            L.append("")
        L += [f"### Kurve: minste f ({tittel})", "",
              "| År | Sone | minste f der (iii) ≤ 0 | minste f der (ii) > 50 % |", "|---|---|---|---|"]
        for _, r in fr[fr["variant"] == variant].iterrows():
            a = None if pd.isna(r.f_sum_le0) else float(r.f_sum_le0)
            c = None if pd.isna(r.f_vinter_gt50) else float(r.f_vinter_gt50)
            L.append(f"| {r.aar} | {r.sone} | {_fmt(a,2)} | {_fmt(c,2)} |")
        L.append("")
    L += ["## Kontroll: NP fra A11 mot A75 − A65", "",
          f"Grense (preregistrert): MAE / middel |NP| ≤ {KONTROLL_GRENSE:.2f}.", "",
          "| År | Sone | Timer | MAE (MW) | Middel abs NP (MW) | MAE/middel | r | Innenfor |", "|---|---|---|---|---|---|---|---|"]
    for _, r in ko.iterrows():
        L.append(f"| {r.aar} | {r.sone} | {r.timer} | {_fmt(r.MAE_MW,1)} | {_fmt(r.middel_abs_NP_MW,1)} | {_fmt(r.rel,4)} | {_fmt(r.r,4)} | {'ja' if r.innenfor else 'nei'} |")
    L.append("")
    open(path, "w", encoding="utf-8").write("\n".join(L))


def figurer(kv, outdir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    for z in ZONES:
        fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
        for y in YEARS:
            d = kv[(kv["variant"] == "hoved") & (kv["sone"] == z) & (kv["aar"] == y)]
            ax[0].plot(d["f"], d["sum_TWh"], label=str(y))
            ax[1].plot(d["f"], d["vinter_andel_under0_pct"], label=str(y))
        ax[0].axhline(0, lw=0.6, color="0.5"); ax[1].axhline(50, lw=0.6, color="0.5", ls="--")
        ax[0].set_xlabel("f (andel av reservert + kø)"); ax[0].set_ylabel("(iii) årlig sum NP − L (TWh)")
        ax[1].set_xlabel("f (andel av reservert + kø)"); ax[1].set_ylabel("(ii) des–feb: andel timer NP − L < 0 (%)")
        ax[0].legend(fontsize=8); fig.suptitle(f"{z}: kurve over f", fontsize=10); fig.tight_layout()
        fig.savefig(os.path.join(outdir, f"kurve_{z}.png"), dpi=150, metadata={"Software": None})
        plt.close(fig)


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--data", default="data"); a.add_argument("--params", default="params/parametre.json")
    a.add_argument("--out", default="results")
    x = a.parse_args()
    kjor(x.data, x.params, x.out)
