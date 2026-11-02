"""Datatester. Kjøres bare når dataene finnes; ellers hoppes de over med melding (ingen syntetiske data her)."""
import hashlib
import os

import pytest

ROT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROT, "data")


def _sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def _manifest():
    m = {}
    for l in open(os.path.join(D, "SHA256_A75_A65_KHEPRI-DC_v1.txt")):
        if l.strip() and not l.startswith("#"):
            h, typ, navn = l.split()
            m[(navn, typ)] = h
    return m


@pytest.mark.parametrize("navn", ["produksjon_A75.parquet", "last_A65.parquet"])
def test_a75_a65_lik_prereg(navn):
    p = os.path.join(D, navn)
    if not os.path.exists(p):
        pytest.skip(f"{navn} distribueres ikke (ENTSO-E-vilkår); bygg med rebuild_data_KHEPRI-DC_v1.py og egen token")
    assert _sha(p) == _manifest()[(navn, "byte")]


def test_a11_lik_prereg():
    p = os.path.join(D, "flyt_A11.parquet")
    if not os.path.exists(p):
        pytest.skip("flyt_A11.parquet mangler")
    assert _sha(p) == "a549031daca866fe38b77535a0192a8437d7d1f7ac400be3feb4ad5d130d976d"
