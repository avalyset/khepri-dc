"""Tester på SYNTETISKE data (ingen ekte ENTSO-E-verdier)."""
import json
import os

import numpy as np
import pandas as pd
import pytest

from khepri_dc import analysis as A
from khepri_dc import entsoe_xml as X

NS = "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0"


def _xml(periods, curve="A03", psr="B12"):
    ps = []
    for start, end, res, pts in periods:
        p = "".join(f"<Point><position>{k}</position><quantity>{v}</quantity></Point>" for k, v in pts.items())
        ps.append(f"<Period><timeInterval><start>{start}</start><end>{end}</end></timeInterval>"
                  f"<resolution>{res}</resolution>{p}</Period>")
    return (f'<GL_MarketDocument xmlns="{NS}"><TimeSeries><inBiddingZone_Domain.mRID>X</inBiddingZone_Domain.mRID>'
            f"<curveType>{curve}</curveType><MktPSRType><psrType>{psr}</psrType></MktPSRType>{''.join(ps)}"
            f"</TimeSeries></GL_MarketDocument>").encode()


def test_a03_hold_forrige_og_timemiddel_15min():
    # 2 timer à 4 kvarter; punkt 1 = 10, punkt 3 = 30 (pos 2 holder 10, pos 4 holder 30), pos 5 = 50 → til slutt
    xml = _xml([("2023-01-01T00:00Z", "2023-01-01T02:00Z", "PT15M", {1: 10, 3: 30, 5: 50})])
    (attrs, nat), = X.parse_timeseries(xml)
    assert attrs["psrType"] == "B12"
    assert list(nat["v"]) == [10, 10, 30, 30, 50, 50, 50, 50]
    h = X.to_hourly(nat, 2023)
    assert h.iloc[0] == pytest.approx(20.0) and h.iloc[1] == pytest.approx(50.0)
    assert h.iloc[2:].isna().all() and len(h) == 8760


def test_delvis_time_blir_nan_og_blandet_oppløsning():
    xml = _xml([("2024-01-01T00:00Z", "2024-01-01T01:00Z", "PT60M", {1: 7}),
                ("2024-01-01T01:00Z", "2024-01-01T01:30Z", "PT15M", {1: 1, 2: 3})])
    (_, nat), = X.parse_timeseries(xml)
    h = X.to_hourly(nat, 2024)
    assert h.iloc[0] == 7 and np.isnan(h.iloc[1]) and len(h) == 8784


def test_a03_manglende_posisjon_1_er_udefinert():
    xml = _xml([("2023-03-01T00:00Z", "2023-03-01T02:00Z", "PT60M", {2: 5})])
    (_, nat), = X.parse_timeseries(xml)
    h = X.to_hourly(X.merge_native([nat])[0], 2023)
    t0 = pd.Timestamp("2023-03-01T00:00Z")
    assert np.isnan(h[t0]) and h[t0 + pd.Timedelta(hours=1)] == 5


def test_merge_konflikt_telles():
    a = X.expand_period(pd.Timestamp("2023-01-01T00:00Z"), pd.Timestamp("2023-01-01T01:00Z"), 60, {1: 1.0})
    b = X.expand_period(pd.Timestamp("2023-01-01T00:00Z"), pd.Timestamp("2023-01-01T01:00Z"), 60, {1: 2.0})
    c = X.expand_period(pd.Timestamp("2023-01-01T00:00Z"), pd.Timestamp("2023-01-01T01:00Z"), 60, {1: 1.0})
    assert X.merge_native([a, b])[1] == 1 and X.merge_native([a, c])[1] == 0


def test_r_new_og_last():
    assert A.r_new(100, 140, 0.7) == 0.0
    assert A.r_new(1000, 70, 0.7) == pytest.approx(900)
    # L = (E_ref − E_y) + 0,7 (w R_new + q Q)
    assert A.last_paalagt(70, 50, 1000, 200, 1, 1, 0.7) == pytest.approx(20 + 0.7 * 1100)
    assert A.last_paalagt(70, 70, 1000, 200, 0, 0, 0.7) == 0


def test_utfall_kjente_svar():
    idx = pd.date_range("2023-01-01", periods=8760, freq="h", tz="UTC")
    s = pd.Series(100.0, index=idx)
    s[idx.month == 7] = -50.0
    u = A.utfall(s, 0.0)
    jul = int((idx.month == 7).sum())
    assert u["andel_under0_pct"] == pytest.approx(jul / 8760 * 100)
    assert u["vinter_andel_under0_pct"] == 0.0
    assert u["sum_TWh"] == pytest.approx((100 * (8760 - jul) - 50 * jul) / 1e6)
    assert u["min_MW"] == -50
    u2 = A.utfall(s, 150.0)
    assert u2["andel_under0_pct"] == 100.0 and u2["vinter_andel_under0_pct"] == 100.0


def test_kurve_minste_f():
    idx = pd.date_range("2023-01-01", periods=8760, freq="h", tz="UTC")
    s = pd.Series(70.0, index=idx)
    # E_ref = E_y = 0, R = 0, Q = 1000: L(f) = 700 f. Sum ≤ 0 når 700 f ≥ 70 → f = 0,10
    kv = A.kurve(s, 0, 0, 0, 1000, 0.7)
    fa, fb = A.minste_f(kv)
    assert fa == pytest.approx(0.10) and fb == pytest.approx(0.11)
    kv0 = A.kurve(s, 0, 0, 0, 0, 0.7)
    assert A.minste_f(kv0) == (None, None)


def test_np_a11_fortegn():
    t = pd.date_range("2023-01-01", periods=2, freq="h", tz="UTC")
    f = pd.DataFrame({"time_utc": list(t) * 4,
                      "fra": ["NO1"] * 2 + ["NO2"] * 2 + ["NO1"] * 2 + ["SE3"] * 2,
                      "til": ["NO2"] * 2 + ["NO1"] * 2 + ["SE3"] * 2 + ["NO1"] * 2,
                      "flyt_MW": [100, 100, 0, 10, 50, 50, 0, 0]})
    x = A.np_a11(f, "NO1")
    assert list(x) == [150, 140]


def test_ende_til_ende_syntetisk(tmp_path):
    rng = np.random.default_rng(1)
    rows_p, rows_l, rows_f = [], [], []
    for y in A.YEARS:
        idx = pd.date_range(f"{y}-01-01", f"{y+1}-01-01", freq="h", tz="UTC", inclusive="left")
        for z in A.ZONES:
            prod = 1000 + rng.normal(0, 100, len(idx)); last = 900 + rng.normal(0, 100, len(idx))
            rows_p.append(pd.DataFrame({"time_utc": idx, "sone": z, "produksjon_MW": prod, "n_typer": 3}))
            rows_l.append(pd.DataFrame({"time_utc": idx, "sone": z, "last_MW": last}))
        for a, b in [("NO1", "NO2"), ("NO2", "NO3"), ("NO3", "NO4"), ("NO4", "NO5")]:
            for fra, til in ((a, b), (b, a)):
                rows_f.append(pd.DataFrame({"time_utc": idx, "fra": fra, "til": til, "flyt_MW": 10.0}))
    d = tmp_path / "data"; d.mkdir()
    pd.concat(rows_p).to_parquet(d / "produksjon_A75.parquet", index=False)
    pd.concat(rows_l).to_parquet(d / "last_A65.parquet", index=False)
    pd.concat(rows_f).to_parquet(d / "flyt_A11.parquet", index=False)
    P = {"brukstid": 0.7, "E_ref_aar": 2025,
         "R_MW": {z: 500.0 for z in A.ZONES}, "Q_MW": {z: 800.0 for z in A.ZONES},
         "E_MW": {z: {"2023": 10.0, "2024": 20.0, "2025": 30.0} for z in A.ZONES}}
    pp = tmp_path / "parametre.json"; pp.write_text(json.dumps(P))
    out = tmp_path / "res"
    A.kjor(str(d), str(pp), str(out))
    md1 = (out / "RESULTATER_KHEPRI-DC_v1_2026-11-02.md").read_bytes()
    A.kjor(str(d), str(pp), str(out))
    assert md1 == (out / "RESULTATER_KHEPRI-DC_v1_2026-11-02.md").read_bytes()  # deterministisk
    sc = pd.read_csv(out / "scenarier.csv")
    s4 = sc[(sc.variant == "hoved") & (sc.aar == 2023) & (sc.sone == "NO1") & (sc.scenario == "S4")].iloc[0]
    assert s4.L_MW == pytest.approx(20 + 0.7 * ((500 - 30 / 0.7) + 800))
    for z in A.ZONES:
        assert os.path.exists(out / f"kurve_{z}.png")
