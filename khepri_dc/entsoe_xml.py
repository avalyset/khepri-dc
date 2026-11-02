"""Parser for ENTSO-E Transparency-XML (A75, A65, A11) med A03-ekspansjon og timeaggregering.

A03 (variable sized block): et Point på posisjon p gjelder fram til neste Point i samme Period;
siste Point gjelder til Period-slutt. Posisjoner før første Point er udefinerte (NaN).
Timeverdi (MW) = middel av de underliggende intervallene i timen; timen får NaN hvis ikke alle
intervallene i timen er definert. Tid er alltid UTC; timen merkes med starttidspunktet.
Modulen leser verdier, men skriver dem aldri ut.
"""
from __future__ import annotations

import re
from collections import defaultdict

import numpy as np
import pandas as pd
from lxml import etree

_RES = {"PT15M": 15, "PT30M": 30, "PT60M": 60}


def _ln(el):
    return etree.QName(el).localname


def _child(el, name):
    for c in el:
        if _ln(c) == name:
            return c
    return None


def _txt(el, name):
    c = _child(el, name)
    return None if c is None else (c.text or "").strip()


def _ts(s: str) -> pd.Timestamp:
    return pd.Timestamp(s.replace("Z", "+00:00")).tz_convert("UTC")


def expand_period(start: pd.Timestamp, end: pd.Timestamp, res_min: int, points: dict[int, float],
                  curve: str = "A03") -> pd.DataFrame:
    """Returnerer native intervaller: indeks = intervallstart (UTC), kolonner v (MW) og res (minutter)."""
    n = int((end - start) / pd.Timedelta(minutes=res_min))
    idx = pd.date_range(start, periods=n, freq=f"{res_min}min", tz="UTC")
    vals = np.full(n, np.nan)
    if curve == "A01":  # sekvensiell: hver posisjon eksplisitt
        for p, v in points.items():
            if 1 <= p <= n:
                vals[p - 1] = v
    else:  # A03
        cur = np.nan
        for p in range(1, n + 1):
            if p in points:
                cur = points[p]
            vals[p - 1] = cur
    return pd.DataFrame({"v": vals, "res": float(res_min)}, index=idx)


def parse_timeseries(xml: bytes):
    """Gir (attributter, serie på native oppløsning) for hver TimeSeries i dokumentet.
    Attributter: psrType, in_domain, out_domain, inBZ, outBZ, curveType."""
    root = etree.fromstring(xml)
    out = []
    for ts in root.iter():
        if _ln(ts) != "TimeSeries":
            continue
        attrs = {}
        for c in ts:
            n = _ln(c)
            if n in ("in_Domain.mRID", "out_Domain.mRID", "inBiddingZone_Domain.mRID",
                     "outBiddingZone_Domain.mRID", "curveType", "businessType"):
                attrs[n] = (c.text or "").strip()
            if n == "MktPSRType":
                attrs["psrType"] = _txt(c, "psrType")
        curve = attrs.get("curveType", "A01")
        parts = []
        for per in ts:
            if _ln(per) != "Period":
                continue
            ti = _child(per, "timeInterval")
            start, end = _ts(_txt(ti, "start")), _ts(_txt(ti, "end"))
            res = _RES[_txt(per, "resolution")]
            pts = {}
            for pt in per:
                if _ln(pt) == "Point":
                    pts[int(_txt(pt, "position"))] = float(_txt(pt, "quantity"))
            if pts:
                parts.append(expand_period(start, end, res, pts, curve))
        if parts:
            out.append((attrs, pd.concat(parts)))
    return out


def merge_native(parts: list[pd.DataFrame]) -> tuple[pd.DataFrame, int]:
    """Slår sammen biter av samme serie. Returnerer (native intervaller, antall konflikter).
    Konflikt = samme intervallstart med ulik verdi (begge definert); første forekomst beholdes."""
    if not parts:
        return pd.DataFrame(columns=["v", "res"]), 0
    s = pd.concat(parts)
    s = s[~s["v"].isna()]
    dup = s.index.duplicated(keep=False)
    konflikt = 0
    if dup.any():
        g = s[dup].groupby(level=0)["v"].nunique()
        konflikt = int((g > 1).sum())
    s = s[~s.index.duplicated(keep="first")].sort_index()
    return s, konflikt


def to_hourly(s: pd.DataFrame, year: int) -> pd.Series:
    """Varighetsvektet timemiddel (MW) for alle UTC-timer i året. En time er dekket når de definerte
    intervallene i timen summerer til 60 minutter; ellers NaN."""
    hours = pd.date_range(f"{year}-01-01", f"{year + 1}-01-01", freq="h", tz="UTC", inclusive="left")
    if len(s) == 0:
        return pd.Series(np.nan, index=hours)
    s = s[(s.index >= hours[0]) & (s.index < hours[-1] + pd.Timedelta(hours=1))]
    h = s.index.floor("h")
    minutes = s["res"].groupby(h).sum()
    energy = (s["v"] * s["res"]).groupby(h).sum()
    hourly = (energy / 60.0).where(np.isclose(minutes, 60.0))
    return hourly.reindex(hours)


def collect(files_by_key: dict, year: int, key_fn) -> tuple[dict, dict]:
    """files_by_key: {nøkkel: [xml-stier]}. key_fn(attrs) -> undernøkkel (f.eks. psrType) eller None for å hoppe over.
    Returnerer ({(nøkkel, undernøkkel): timeserie}, {(nøkkel, undernøkkel): konflikter})."""
    hourly, conflicts = {}, {}
    for key, paths in files_by_key.items():
        bits = defaultdict(list)
        for p in paths:
            for attrs, s in parse_timeseries(open(p, "rb").read()):
                sub = key_fn(attrs)
                if sub is not None:
                    bits[sub].append(s)
        for sub, lst in bits.items():
            s, k = merge_native(lst)
            hourly[(key, sub)] = to_hourly(s, year)
            conflicts[(key, sub)] = k
    return hourly, conflicts
