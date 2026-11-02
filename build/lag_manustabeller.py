"""Fyller {{TABELL_*}}-plassholdere i manusmalen med tabeller generert fra results/*.csv (ingen håndtastede tall).
Bruk: python -m build.lag_manustabeller <mal.md> <ut.md>"""
import json
import sys

import pandas as pd

R = "results"
sc = pd.read_csv(f"{R}/scenarier.csv"); fr = pd.read_csv(f"{R}/minste_f.csv"); ko = pd.read_csv(f"{R}/kontroll.csv")
P = json.load(open("params/parametre.json"))
h = sc[sc.variant == "hoved"]
Z = ["NO1", "NO2", "NO3", "NO4", "NO5"]; Y = [2023, 2024, 2025]


def n(x, d):
    s = f"{x:.{d}f}".replace("-", "−")
    return s.replace(".", ",")


def t_s0():
    L = ["| Sone | (i) andel timer NP < 0 (%) 2023 / 2024 / 2025 | (ii) des–feb (%) | (iii) sum NP (TWh) | (iv) laveste NP (MW) |",
         "|---|---|---|---|---|"]
    for z in Z:
        d = h[(h.sone == z) & (h.scenario == "S0")].set_index("aar")
        L.append(f"| {z} | " + " / ".join(n(d.loc[y, 'andel_under0_pct'], 1) for y in Y) + " | "
                 + " / ".join(n(d.loc[y, 'vinter_andel_under0_pct'], 1) for y in Y) + " | "
                 + " / ".join(n(d.loc[y, 'sum_TWh'], 1) for y in Y) + " | "
                 + " / ".join(n(d.loc[y, 'min_MW'], 0) for y in Y) + " |")
    return "\n".join(L)


def t_last():
    L = ["| Sone | R | Q | E_ref | R_new | L S1 | L S2 | L S3 | L S4 |", "|---|---|---|---|---|---|---|---|---|"]
    for z in Z:
        d = h[(h.sone == z) & (h.aar == 2025)].set_index("scenario")
        rn = max(0.0, P["R_MW"][z] - P["E_MW"][z]["2025"] / P["brukstid"])
        L.append(f"| {z} | {n(P['R_MW'][z],0)} | {n(P['Q_MW'][z],0)} | {n(P['E_MW'][z]['2025'],0)} | {n(rn,0)} | "
                 + " | ".join(n(d.loc[s, "L_MW"], 0) for s in ("S1", "S2", "S3", "S4")) + " |")
    return "\n".join(L)


def t_scen(s):
    L = [f"| Sone | (i) andel timer NP − L < 0 (%) | Δ(i) mot S0 (pp) | (ii) des–feb (%) | (iii) sum (TWh) | (iv) laveste (MW) |",
         "|---|---|---|---|---|---|"]
    for z in Z:
        d = h[(h.sone == z) & (h.scenario == s)].set_index("aar")
        f = lambda c, k: " / ".join(n(d.loc[y, c], k) for y in Y)
        L.append(f"| {z} | {f('andel_under0_pct',1)} | {f('d_andel_pp',1)} | {f('vinter_andel_under0_pct',1)} | {f('sum_TWh',1)} | {f('min_MW',0)} |")
    return "\n".join(L)


def t_f():
    L = ["| Sone | minste f der (iii) ≤ 0: 2023 / 2024 / 2025 | minste f der (ii) > 50 %: 2023 / 2024 / 2025 |", "|---|---|---|"]
    d = fr[fr.variant == "hoved"]
    for z in Z:
        e = d[d.sone == z].set_index("aar")
        g = lambda c: " / ".join("ikke nådd" if pd.isna(e.loc[y, c]) else n(e.loc[y, c], 2) for y in Y)
        L.append(f"| {z} | {g('f_sum_le0')} | {g('f_vinter_gt50')} |")
    return "\n".join(L)


def t_ko():
    L = ["| Sone | MAE / middel abs NP: 2023 / 2024 / 2025 | r: 2023 / 2024 / 2025 | Innenfor 0,05 |", "|---|---|---|---|"]
    for z in Z:
        e = ko[ko.sone == z].set_index("aar")
        L.append(f"| {z} | " + " / ".join(n(e.loc[y, 'rel'], 3) for y in Y) + " | "
                 + " / ".join(n(e.loc[y, 'r'], 3) for y in Y) + " | "
                 + ("ja" if e.innenfor.all() else ("nei" if not e.innenfor.any() else "delvis")) + " |")
    return "\n".join(L)


def t_a11():
    import os
    if not os.path.exists(f"{R}/tillegg_a11_scenarier.csv"):
        return ""
    a = pd.read_csv(f"{R}/tillegg_a11_scenarier.csv"); af = pd.read_csv(f"{R}/tillegg_a11_minste_f.csv")
    hf = fr[fr.variant == "hoved"]
    g = lambda d, z, y, s, c: d[(d.sone == z) & (d.aar == y) & (d.scenario == s)][c].iloc[0]
    ff = lambda d, z, y: d[(d.sone == z) & (d.aar == y)].f_sum_le0.iloc[0]
    fx = lambda x: "ikke nådd" if pd.isna(x) else n(x, 2)
    L = ["| Sone | År | (i) S0 (%) | (i) S3 (%) | (iii) S3 (TWh) | minste f, (iii) ≤ 0 |", "|---|---|---|---|---|---|"]
    for z in Z:
        for y in Y:
            L.append(f"| {z} | {y} | {n(g(h,z,y,'S0','andel_under0_pct'),1)} / {n(g(a,z,y,'S0','andel_under0_pct'),1)} | "
                     f"{n(g(h,z,y,'S3','andel_under0_pct'),1)} / {n(g(a,z,y,'S3','andel_under0_pct'),1)} | "
                     f"{n(g(h,z,y,'S3','sum_TWh'),1)} / {n(g(a,z,y,'S3','sum_TWh'),1)} | {fx(ff(hf,z,y))} / {fx(ff(af,z,y))} |")
    return "\n".join(L)


if __name__ == "__main__":
    t = open(sys.argv[1], encoding="utf-8").read()
    for k, f in {"S0": t_s0, "LAST": t_last, "S3": lambda: t_scen("S3"), "S4": lambda: t_scen("S4"),
                 "F": t_f, "KONTROLL": t_ko, "A11": t_a11}.items():
        t = t.replace("{{TABELL_" + k + "}}", f())
    assert "{{TABELL_" not in t
    open(sys.argv[2], "w", encoding="utf-8").write(t)
