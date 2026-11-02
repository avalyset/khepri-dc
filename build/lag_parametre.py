"""Lager params/parametre.json: R og Q (Statnett, datasenter, avlest 2026-11-02, arkiv/STATNETT_ARKIV_…),
E_y per prisområde og UTC-år fra Elhub consumption_datacenter_per_mba_hour (CC BY 4.0), brukstid 0,70.
Bruk: python -m build.lag_parametre <elhub-csv> <ut-json>"""
import hashlib
import json
import sys

from build.elhub_ey import ey, les

R_MW = {"NO1": 1398.0, "NO2": 1950.0, "NO3": 96.0, "NO4": 477.0, "NO5": 270.0}
Q_MW = {"NO1": 2220.0, "NO2": 3092.0, "NO3": 1646.0, "NO4": 2258.0, "NO5": 894.0}

if __name__ == "__main__":
    src, ut = sys.argv[1], sys.argv[2]
    g = ey(les(src))
    E = {z: {} for z in R_MW}
    for _, r in g.iterrows():
        E[r["PRISOMRÅDE"]][str(int(r["aar"]))] = round(float(r["E_MW"]), 6)
    P = {"brukstid": 0.70, "E_ref_aar": 2025, "R_MW": R_MW, "Q_MW": Q_MW, "E_MW": E,
         "kilder": {"R_Q": "Statnett, Statistikk om tilknytningssaker (Power BI), forbruk, næringstype Datasenter, "
                           "avlest 2026-11-02; arkiv/STATNETT_ARKIV_KHEPRI-DC_v1_2026-11-02.md",
                    "E": "Elhub consumption_datacenter_per_mba_hour (CC BY 4.0), lastet ned 2026-11-02, sha256 "
                         + hashlib.sha256(open(src, "rb").read()).hexdigest(),
                    "brukstid": "NVE, Metode for framskriving av strømforbruk i datasentre, 11.08.2026, s. 4"}}
    json.dump(P, open(ut, "w"), indent=1, ensure_ascii=False, sort_keys=True)
    print("skrevet", ut)
