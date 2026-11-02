#!/usr/bin/env python3
"""Bygger data/produksjon_A75.parquet og data/last_A65.parquet på nytt fra rå ENTSO-E-XML.

A75 (faktisk produksjon per type, art. 16.1.b/c) og A65 (faktisk totallast, art. 6.1.a) står ikke på ENTSO-Es liste
over data for fri gjenbruk (18.10.2023) og distribueres derfor ikke i pakken. Med egen ENTSO-E-token kan de hentes
og bygges med nøyaktig samme kode som i preregistreringen (build/build_series.py, khepri_dc/entsoe_xml.py).

Bruk:
  python rebuild_data_KHEPRI-DC_v1.py --raw-dir raw                # bruk rå XML som finnes (raw/A75, raw/A65)
  ENTSOE_API_TOKEN=... python rebuild_data_KHEPRI-DC_v1.py --fetch --raw-dir raw   # hent først, så bygg
Utdata: data/produksjon_A75.parquet, data/last_A65.parquet. Skriptet skriver sha256 og innholdshash og sammenligner
med data/SHA256_A75_A65_KHEPRI-DC_v1.txt. Henting: P1Y per sone og UTC-år, 5 s mellom kall, HTTP 429 → 90 s, maks
3 forsøk. Tokenet skrives aldri ut.
"""
import argparse
import hashlib
import os
import shutil
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ZONES = {"NO_1": "10YNO-1--------2", "NO_2": "10YNO-2--------T", "NO_3": "10YNO-3--------J",
         "NO_4": "10YNO-4--------9", "NO_5": "10Y1001A1001A48H"}
YEARS = (2023, 2024, 2025)
URL = "https://web-api.tp.entsoe.eu/api"
FILES = ("produksjon_A75.parquet", "last_A65.parquet")
KEYS = {"produksjon_A75.parquet": ["sone", "time_utc", "produksjon_MW", "n_typer"],
        "last_A65.parquet": ["sone", "time_utc", "last_MW"]}


def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def innholdshash(p):
    """sha256 av innholdet: sortert på sone + time_utc, kolonner i fast rekkefølge, CSV med %.17g og ISO-tid i UTC."""
    import pandas as pd
    d = pd.read_parquet(p)[KEYS[os.path.basename(p)]].sort_values(["sone", "time_utc"]).reset_index(drop=True)
    d["time_utc"] = d["time_utc"].dt.tz_convert("UTC").dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    return hashlib.sha256(d.to_csv(index=False, float_format="%.17g", lineterminator="\n").encode()).hexdigest()


def hent(raw_dir, token, serier=("A75", "A65"), years=YEARS, zones=ZONES, maaned=None):
    import requests
    s = requests.Session(); s.headers["User-Agent"] = "KHEPRI-DC-rebuild/1.0"
    for serie in serier:
        os.makedirs(os.path.join(raw_dir, serie), exist_ok=True)
        for k, eic in zones.items():
            for y in years:
                if maaned:
                    ps, pe = f"{y}{maaned:02d}010000", (f"{y}{maaned+1:02d}010000" if maaned < 12 else f"{y+1}01010000")
                    navn = f"{serie}_{k}_{y}-{maaned:02d}.xml"
                else:
                    ps, pe, navn = f"{y}01010000", f"{y+1}01010000", f"{serie}_{k}_{y}.xml"
                ut = os.path.join(raw_dir, serie, navn)
                if os.path.exists(ut):
                    continue
                p = {"documentType": serie, "processType": "A16", "periodStart": ps, "periodEnd": pe}
                p["in_Domain" if serie == "A75" else "outBiddingZone_Domain"] = eic
                for forsok in range(3):
                    r = s.get(URL, params={**p, "securityToken": token}, timeout=180)
                    if r.status_code == 429:
                        time.sleep(90); continue
                    break
                if r.status_code != 200:
                    sys.exit(f"HTTP {r.status_code} for {navn}")
                open(ut, "wb").write(r.content)
                print(f"hentet {navn} ({len(r.content)} byte)")
                time.sleep(5)


def bygg(raw_dir, out_dir):
    from build import build_series
    with tempfile.TemporaryDirectory() as tmp:
        build_series.main(raw_dir, tmp)
        os.makedirs(out_dir, exist_ok=True)
        for f in FILES:
            shutil.copyfile(os.path.join(tmp, f), os.path.join(out_dir, f))


def sammenlign(out_dir, manifest):
    forventet = {}
    if os.path.exists(manifest):
        for l in open(manifest):
            if l.strip() and not l.startswith("#"):
                h, typ, navn = l.split()
                forventet[(navn, typ)] = h
    ok = True
    for f in FILES:
        p = os.path.join(out_dir, f)
        b, c = sha256(p), innholdshash(p)
        eb, ec = forventet.get((f, "byte")), forventet.get((f, "innhold"))
        print(f"{f}: sha256 {b} ({'lik' if b == eb else 'ULIK' if eb else 'ukjent'}), "
              f"innholdshash {c} ({'lik' if c == ec else 'ULIK' if ec else 'ukjent'})")
        ok &= (c == ec) if ec else False
    return ok


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--raw-dir", default="raw"); a.add_argument("--out", default="data")
    a.add_argument("--fetch", action="store_true", help="hent A75/A65 fra ENTSO-E (krever ENTSOE_API_TOKEN)")
    a.add_argument("--manifest", default="data/SHA256_A75_A65_KHEPRI-DC_v1.txt")
    x = a.parse_args()
    if x.fetch:
        tok = os.environ.get("ENTSOE_API_TOKEN") or sys.exit("sett ENTSOE_API_TOKEN")
        hent(x.raw_dir, tok)
    bygg(x.raw_dir, x.out)
    sys.exit(0 if sammenlign(x.out, x.manifest) else 1)
