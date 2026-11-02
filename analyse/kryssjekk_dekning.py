"""Uavhengig kryssjekk av timedekning i rå ENTSO-E-XML (kun tidsintervaller, ingen verdier leses).
A03: en Period med minst ett Point dekker hele timeInterval (manglende posisjoner = hold forrige).
Bruk: python -I kryssjekk_dekning.py <år> <xml>..."""
import sys, re
from datetime import datetime, timedelta, timezone
aar = int(sys.argv[1]); dekket = set()
for f in sys.argv[2:]:
    t = open(f, encoding="utf-8").read()
    for per in re.findall(r"<Period>(.*?)</Period>", t, flags=re.S):
        if "<Point>" not in per: continue
        s = re.search(r"<start>([^<]+)</start>", per).group(1); e = re.search(r"<end>([^<]+)</end>", per).group(1)
        res = re.search(r"<resolution>([^<]+)</resolution>", per).group(1)
        p = lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%MZ").replace(tzinfo=timezone.utc)
        h = p(s).replace(minute=0)
        if p(s).minute: h += timedelta(hours=1)  # kun hele timer
        while h + timedelta(hours=1) <= p(e):
            if h.year == aar: dekket.add(h)
            h += timedelta(hours=1)
forv = int((datetime(aar + 1, 1, 1) - datetime(aar, 1, 1)).total_seconds() // 3600)
print(f"år {aar}: forventet {forv}, dekket {len(dekket)}, manglende {forv - len(dekket)}")
