"""Utforskende, ikke preregistrert (A-DC2 steg 3b). Årlig A75-produksjon og A65-last per sone (TWh) mot Elhubs
production_per_group_mba_hour, consumption_per_group_mba_hour og gridloss_per_hour_mba (CC BY 4.0). UTC-år.
Bruk: python -m diagnose.dekning_elhub <elhub-katalog> <ut-katalog>"""
import os, sys
import pandas as pd
from khepri_dc import analysis as A

ek, ut = sys.argv[1], sys.argv[2]

def les(f, col, faktor):
    d = pd.read_csv(os.path.join(ek, f), sep=";", decimal=",", dtype={"PRISOMRÅDE": str})
    d["t"] = pd.to_datetime(d["STARTTID"], utc=True); d["aar"] = d["t"].dt.year
    d = d[d["aar"].between(2023, 2025)]
    return d.groupby(["PRISOMRÅDE", "aar"])[col].sum() * faktor / 1e6  # -> TWh (fra MWh)

prod_e = les("production_per_group_mba_hour-all-no.csv", "VOLUM_KWH", 1e-3)
forb_e = les("consumption_per_group_mba_hour-all-no.csv", "VOLUM_KWH", 1e-3)
tap_e = les("gridloss_per_hour_mba-all-no.csv", "NETTAP_MWH", 1.0)
p = pd.read_parquet("data/produksjon_A75.parquet"); l = pd.read_parquet("data/last_A65.parquet")
p["aar"] = p.time_utc.dt.year; l["aar"] = l.time_utc.dt.year
pa = p.groupby(["sone", "aar"]).produksjon_MW.sum() / 1e6; la = l.groupby(["sone", "aar"]).last_MW.sum() / 1e6
rows = []
for z in A.ZONES:
    for y in A.YEARS:
        rows.append({"sone": z, "aar": y, "A75_TWh": pa[(z, y)], "Elhub_prod_TWh": prod_e[(z, y)],
                     "A75_minus_Elhub_prod": pa[(z, y)] - prod_e[(z, y)],
                     "A65_TWh": la[(z, y)], "Elhub_forbruk_TWh": forb_e[(z, y)], "Elhub_nettap_TWh": tap_e[(z, y)],
                     "A65_minus_Elhub_forbruk": la[(z, y)] - forb_e[(z, y)],
                     "A65_minus_Elhub_forbruk_og_nettap": la[(z, y)] - forb_e[(z, y)] - tap_e[(z, y)]})
d = pd.DataFrame(rows); d.to_csv(os.path.join(ut, "dekning_elhub.csv"), index=False, float_format="%.4f")
pd.set_option("display.width", 220); print(d.round(2).to_string(index=False))
