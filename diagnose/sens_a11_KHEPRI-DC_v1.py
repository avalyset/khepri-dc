"""Utforskende, ikke preregistrert (A-DC2 steg 4). Sensitivitet: samme scenarier og f-kurve som den preregistrerte
analysen, men med NP fra fysisk flyt (A11: Σ ut − Σ inn over sonens egne grenser) i stedet for A75 − A65.
Importerer funksjonene fra khepri_dc/analysis.py uendret. Hovedmålet leses fra results/scenarier.csv og minste_f.csv.

Bruk (fra repo-roten): python diagnose/sens_a11_KHEPRI-DC_v1.py
Ut: results/TILLEGG_KHEPRI-DC_v1_2026-11-02.md, results/tillegg_a11_scenarier.csv, results/tillegg_a11_minste_f.csv
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd  # noqa: E402

from khepri_dc import analysis as A  # noqa: E402

P = json.load(open("params/parametre.json")); b = P["brukstid"]
flyt = pd.read_parquet("data/flyt_A11.parquet")
rows, frows = [], []
for y in A.YEARS:
    for z in A.ZONES:
        s = A.np_a11(flyt, z); s = s[s.index.year == y]
        R, Q = P["R_MW"][z], P["Q_MW"][z]
        E_ref, E_y = P["E_MW"][z][str(P["E_ref_aar"])], P["E_MW"][z][str(y)]
        base = A.utfall(s, 0.0)
        for sn, wq in A.SCENARIOS.items():
            L = 0.0 if wq is None else A.last_paalagt(E_ref, E_y, R, Q, wq[0], wq[1], b)
            u = base if wq is None else A.utfall(s, L)
            rows.append({"aar": y, "sone": z, "scenario": sn, "L_MW": L, **u})
        fa, fb = A.minste_f(A.kurve(s, E_ref, E_y, R, Q, b))
        frows.append({"aar": y, "sone": z, "f_sum_le0": fa, "f_vinter_gt50": fb})
sc = pd.DataFrame(rows); fr = pd.DataFrame(frows)
sc.to_csv("results/tillegg_a11_scenarier.csv", index=False, float_format="%.6f")
fr.to_csv("results/tillegg_a11_minste_f.csv", index=False, float_format="%.2f")

hs = pd.read_csv("results/scenarier.csv"); hs = hs[hs.variant == "hoved"]
hf = pd.read_csv("results/minste_f.csv"); hf = hf[hf.variant == "hoved"]


def n(x, d):
    return "ikke nådd" if pd.isna(x) else f"{x:.{d}f}".replace("-", "−").replace(".", ",")


def g(df, z, y, s, c):
    return df[(df.sone == z) & (df.aar == y) & (df.scenario == s)][c].iloc[0]


L = ["# TILLEGG — KHEPRI-DC v1 (2026-11-02): sensitivitet med NP fra A11", "",
     "**Utforskende, ikke preregistrert.** Samme scenarier, parametre og f-kurve som den preregistrerte analysen "
     "(funksjonene importert uendret fra khepri_dc/analysis.py), men NP = netto fysisk flyt ut av sonen (A11) i stedet "
     "for A75 − A65. Begrunnelse: DEV-1 og truth/DIAGNOSE_DEV1. Hovedmålet står uendret i RESULTATER.", "",
     "Hver celle: hovedmål (A75 − A65) / A11. År 2023 · 2024 · 2025.", "",
     "| Sone | År | (i) andel timer < 0, S0 (%) | (i) S3 (%) | (iii) årssum S3 (TWh) | minste f der (iii) ≤ 0 |",
     "|---|---|---|---|---|---|"]
for z in A.ZONES:
    for y in A.YEARS:
        L.append(f"| {z} | {y} | {n(g(hs,z,y,'S0','andel_under0_pct'),1)} / {n(g(sc,z,y,'S0','andel_under0_pct'),1)} | "
                 f"{n(g(hs,z,y,'S3','andel_under0_pct'),1)} / {n(g(sc,z,y,'S3','andel_under0_pct'),1)} | "
                 f"{n(g(hs,z,y,'S3','sum_TWh'),2)} / {n(g(sc,z,y,'S3','sum_TWh'),2)} | "
                 f"{n(hf[(hf.sone==z)&(hf.aar==y)].f_sum_le0.iloc[0],2)} / {n(fr[(fr.sone==z)&(fr.aar==y)].f_sum_le0.iloc[0],2)} |")
L += ["", "Full A11-tabell for alle scenarier: results/tillegg_a11_scenarier.csv og tillegg_a11_minste_f.csv.", ""]
open("results/TILLEGG_KHEPRI-DC_v1_2026-11-02.md", "w", encoding="utf-8").write("\n".join(L))
print("\n".join(L))
