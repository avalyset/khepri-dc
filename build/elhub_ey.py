"""E_y: gjennomsnittlig datasenterlast (MW) per prisområde og UTC-år fra Elhub
consumption_datacenter_per_mba_hour (CC BY 4.0). Bruk: python -I elhub_ey.py <csv> [<eldre csv for revisjonssjekk>]"""
import sys
import pandas as pd

def les(p):
    d = pd.read_csv(p, sep=";", decimal=",", dtype={"PRISOMRÅDE": str})
    assert pd.api.types.is_numeric_dtype(d["VOLUM_KWH"]), "VOLUM_KWH ikke numerisk"
    d["t"] = pd.to_datetime(d["STARTTID"], utc=True)
    return d

def ey(d):
    d = d[(d["t"].dt.year >= 2023) & (d["t"].dt.year <= 2025)].copy()
    d["aar"] = d["t"].dt.year
    g = d.groupby(["PRISOMRÅDE", "aar"]).agg(kwh=("VOLUM_KWH", "sum"), timer=("t", "nunique")).reset_index()
    g["forventet"] = g["aar"].map({2023: 8760, 2024: 8784, 2025: 8760})
    g["E_MW"] = g["kwh"] / 1000.0 / g["forventet"]
    return g

if __name__ == "__main__":
    d = les(sys.argv[1]); g = ey(d)
    print(g.to_string(index=False, float_format=lambda x: f"{x:.3f}"))
    print("nasjonal E_MW per år:", g.groupby("aar")["E_MW"].sum().round(3).to_dict())
    if len(sys.argv) > 2:
        o = les(sys.argv[2]); k = ["t", "PRISOMRÅDE"]
        m = d.merge(o, on=k, suffixes=("", "_gml"))
        m = m[(m["t"].dt.year >= 2023) & (m["t"].dt.year <= 2025)]
        print("felles rader 2023-25:", len(m), " ulik VOLUM_KWH:", int((m["VOLUM_KWH"] != m["VOLUM_KWH_gml"]).sum()))
