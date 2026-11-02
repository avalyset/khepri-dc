"""Utforskende, ikke preregistrert (A-DC2 steg 1). Klassifiserer hver A75-TimeSeries i rå XML etter domene
(kun metadata): in = inBiddingZone (produksjon), out = outBiddingZone (forbruk). Bruk: python -m diagnose.sjekk_a75_serier <raw>"""
import collections, glob, os, sys
from lxml import etree

raw = sys.argv[1]
for f in sorted(glob.glob(os.path.join(raw, "A75", "A75_NO_*_20*.xml"))):
    root = etree.parse(f).getroot()
    c = collections.Counter(); prod = set(); forb = set()
    for ts in root.iter():
        if etree.QName(ts).localname != "TimeSeries":
            continue
        names = {etree.QName(x).localname for x in ts}
        psr = next((y.text for x in ts if etree.QName(x).localname == "MktPSRType" for y in x), None)
        i, o = "inBiddingZone_Domain.mRID" in names, "outBiddingZone_Domain.mRID" in names
        k = {(True, False): "in", (False, True): "out", (True, True): "begge", (False, False): "ingen"}[(i, o)]
        c[k] += 1
        (prod if k == "in" else forb if k == "out" else set()).add(psr)
    print(os.path.basename(f), dict(c), "produksjon:", ",".join(sorted(prod)), "| forbruk:", ",".join(sorted(forb)) or "-")
