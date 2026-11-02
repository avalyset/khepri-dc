"""Datasenter-MW reservert/kø per kommune (Dok 15:2086-vedlegg, 08.05.2025) summert per budområde.
Koblingen kommune -> budområde er en ANTAKELSE (fylkes-/nettregion-basert), ikke fra kilden.
Ingen balansestørrelse beregnes; dette er reservasjonstall."""
# (kommune, fylke, reservert_MW, kø_MW, antatt_budområde)
RADER = [
    ("Modalen", "Vestland", 300, 300, "NO5"), ("Time", "Rogaland", 426, 150, "NO2"),
    ("Narvik", "Nordland", 230, 0, "NO4"), ("Tydal", "Trøndelag", 140, 0, "NO3"),
    ("Valle", "Agder", 140, 0, "NO2"), ("Skien", "Telemark", 299, 480, "NO2"),
    ("Bjerkreim", "Rogaland", 136, 360, "NO2"), ("Ringerike", "Buskerud", 139.5, 521, "NO1"),
    ("Vennesla", "Agder", 85, 0, "NO2"), ("Øygarden", "Vestland", 75, 44, "NO5"),
    ("Namsskogan", "Trøndelag", 70, 5, "NO3"), ("Bremanger", "Vestland", 60, 124.8, "NO5"),
    ("Tinn", "Telemark", 66, 0, "NO2"), ("Sarpsborg", "Østfold", 30, 30, "NO1"),
    ("Lillestrøm", "Akershus", 59, 170, "NO1"), ("Oslo", "Oslo", 39.2, 29.3, "NO1"),
    ("Vestby", "Akershus", 29, 99, "NO1"), ("Hustadvika", "Møre og Romsdal", 15, 0, "NO3"),
    ("Sortland", "Nordland", 10, 30, "NO4"), ("Sandnes", "Rogaland", 11, 8, "NO2"),
    ("Hemnes", "Nordland", 1.5, 20, "NO4"), ("Lørenskog", "Akershus", 1, 0, "NO1"),
    ("Vefsn", "Nordland", 0, 23, "NO4"), ("Meløy", "Nordland", 0, 30, "NO4"),
    ("Rana", "Nordland", 0, 436, "NO4"), ("Hamar", "Innlandet", 0, 179, "NO1"),
    ("Vågå", "Innlandet", 0, 10, "NO1"), ("Eidsvoll", "Akershus", 0, 175, "NO1"),
    ("Sør-Varanger", "Finnmark", 0, 29, "NO4"), ("Sunndal", "Møre og Romsdal", 0, 8, "NO3"),
    ("Åfjord", "Trøndelag", 0, 5.8, "NO3"), ("Stjørdal", "Trøndelag", 0, 180, "NO3"),
    ("Alta", "Finnmark", 0, 5, "NO4"), ("Hammerfest", "Finnmark", 0, 25, "NO4"),
    ("Balsfjord", "Troms", 0, 12.72, "NO4"), ("Porsanger", "Finnmark", 0, 600, "NO4"),
    ("Tønsberg", "Vestfold", 0, 120, "NO1"),
]
TVILSOMME = {"Namsskogan": "grensen NO3/NO4 går nær Namsskogan", "Vågå": "Nord-Gudbrandsdal kan ligge i NO1 eller NO5/NO3",
             "Tinn": "Telemark-vest kan ligge i NO2 eller NO1", "Valle": "Setesdal, antatt NO2",
             "Hustadvika": "Møre og Romsdal, antatt NO3", "Sunndal": "Møre og Romsdal, antatt NO3",
             "Bremanger": "Nordfjord, antatt NO5 (kan være NO3)", "Tønsberg": "Vestfold, antatt NO1 (kan være NO2)",
             "Skien": "Telemark, antatt NO2 (kan være NO1)", "Ringerike": "antatt NO1"}
if __name__ == "__main__":
    tot = {}
    for k, f, r, q, z in RADER:
        a = tot.setdefault(z, [0.0, 0.0]); a[0] += r; a[1] += q
    print("budområde | reservert MW | kø MW")
    for z in sorted(tot): print(f"{z} | {tot[z][0]:.1f} | {tot[z][1]:.1f}")
    R = sum(r for _, _, r, _, _ in RADER); Q = sum(q for _, _, _, q, _ in RADER)
    print(f"SUM | {R:.1f} | {Q:.1f}   (kilden oppgir 2 362 reservert og 4 210 kø)")
    print("Tvilsom kobling:", "; ".join(f"{k}: {v}" for k, v in TVILSOMME.items()))
