# NUMBERS — KHEPRI-DC v1 (2026-11-02)

Hvert tall i løpende tekst i manus/MANUS_KHEPRI-DC_v1_2026-11-02.md, README, Brevetpakken og komitéutkastene, med
kilde. Tallene i manusets tabeller 1–6 er generert direkte fra results/*.csv og params/parametre.json av
build/lag_manustabeller.py og listes ikke enkeltvis.

| Tall i teksten | Verdi | Kilde |
|---|---|---|
| Andel timer NP < 0, NO1, S0 | 76,3 / 83,2 / 99,0 % → «76–99 %» | results/scenarier.csv, hoved, S0, NO1, andel_under0_pct (76,34 / 83,15 / 99,01) |
| Andel timer NP < 0, NO3, S0 | 81,2 / 88,3 / 65,1 % → «65–88 %» | samme, NO3 (81,21 / 88,26 / 65,13) |
| NO2, NO4, NO5 overskudd på årsbasis alle år | (iii) S0 > 0 | samme, sum_TWh: NO2 15,199 / 19,322 / 17,578; NO4 7,038 / 3,564 / 6,942; NO5 13,880 / 15,147 / 14,974 |
| NO4 andel timer S0 | 18,3 / 36,4 / 7,6 % | samme, NO4 S0 (18,25 / 36,38 / 7,59) |
| NO4 andel timer S3 | 34,5 / 60,0 / 30,1 % | samme, NO4 S3 (34,49 / 60,00 / 30,07) |
| NO4 årssum S3 | 1,5 / −1,9 / 1,6 TWh | samme, NO4 S3 sum_TWh (1,545 / −1,893 / 1,589) |
| Minste f, (iii) ≤ 0, NO4 | 0,43 / 0,22 / 0,44 | results/minste_f.csv, hoved |
| Minste f, (iii) ≤ 0, NO2 | 0,50 / 0,63 / 0,58 | samme |
| NO5 ikke nådd | – | samme |
| Sum av sonenes (iii), S0 | 17,9 / 18,6 / 22,9 TWh | Σ over soner av scenarier.csv sum_TWh (17,901 / 18,589 / 22,857); aritmetikk, ikke preregistrert |
| Sum av sonenes (iii), S3 | −12,3 / −11,1 / −5,6 TWh | (−12,315 / −11,107 / −5,580); samme forbehold |
| Sum av sonenes (iii), S4 | −69,2 / −68,1 / −62,5 TWh | (−69,189 / −68,137 / −62,454); samme forbehold |
| Samlet påslag S3, 2025 | 3 246 MW | Σ urundede L_MW for S3 2025 i scenarier.csv (avrundet per sone gir 812 + 1 168 + 384 + 611 + 272 = 3 247) |
| Kontroll: r | ≥ 0,985 (0,9854–0,9995) | results/kontroll.csv |
| Kontroll: avvik utenfor grensen | 6–14 % av middel abs NP (0,056–0,136), MAE 46–229 MW | results/kontroll.csv, rader med innenfor = False |
| Kontrollgrense | 0,05 | PREREG § 6 |
| R NO3 / E_ref/0,70 | 96 MW / 219,8 MW | params/parametre.json (96; 153,83 / 0,70) |
| Brukstid | 0,70 | NVE metodenotat 11.08.2026, s. 4 |
| Gyldige timer | 8 760 / 8 784 / 8 760, 120 serie-år | data/BYGGTELLING.json; results/RESULTATER (Timer-kolonnen) |
| Grenser | 15 grenser, 30 retninger | build/build_series.py BORDERS; A-DC0 inventar (lik entsoe-py NEIGHBOURS) |
| A75-forbruksserier utelatt | B10 i NO2, NO3, NO5; B18 i NO2; bare 2025 | data/BYGGTELLING.json (forbruksserier_utelatt) + metadata-sjekk i STATE |
| NVE 37: reservert datasenter i S4 | 3,6 GW | NVE Rapport 37/2026, s. 27 |
| NVE 37: reservert / kø | om lag 4 GW / om lag 9 GW | NVE Rapport 37/2026, s. 27 |
| NVE 37: 30 værår | 30 | NVE Rapport 37/2026 (modellert over værårene 1991–2020) og LA25 s. 6 |
| De Facto: dato, periode | 7. august 2025; 2021–2025 | De Facto 4:2025, s. 3 og figur 8–12 (s. 17–21) |
| Riksrevisjonen: 8 400 MW; s. 10; s. 52 | sep. 2024 | Dokument 3:7 (2024–2025), Rapport s. 10 (PDF s. 11) og s. 52 (PDF s. 100) |
| 161 TWh, 23 TWh, 15 TWh | 2025 / normalår | NVE Rapport 17/2026, s. 2 |
| Statnett R og Q (datasenter) | NO1 1 398 / 2 220; NO2 1 950 / 3 092; NO3 96 / 1 646; NO4 477 / 2 258; NO5 270 / 894; Norge 4 190 / 10 109 MW | arkiv/STATNETT_ARKIV_KHEPRI-DC_v1_2026-11-02.md |
| Elhub E_ref nasjonalt 2025 | 358,6 MW (3,14 TWh) | build/elhub_ey.py på Elhub-fila (sha256 i DECISIONS D1) |
| Næringskode | 63.100 | Elhub dashbord «Forbehold» (gjengitt i ~/khepri-data/datasenter-v0/README.md) |
| Statnett avlesningsdato | 2. november 2026 | arkiv/STATNETT_ARKIV_… |
| NVE 37: kraftbalanse og priser per budområde | s. 16–20 | NVE Rapport 37/2026, s. 16 (fotnote 26: «Kraftbalansen i NO5 er noe høyere i scenarioet Høy Datasenter …») og s. 19–20 (priser) |
| Tabellen i TILLEGG-ENERGIOGMILJOKOMITEEN (S0- og S3-andeler, S3-årssum per sone) | se tabell | results/scenarier.csv, hoved, S0 og S3 (andel_under0_pct, sum_TWh), avrundet til én desimal; identisk med manusets tabell 2 og 3 |
| NO4 årssum S0 i TILLEGG-NAERINGSKOMITEEN | 7,0 / 3,6 / 6,9 TWh | results/scenarier.csv, NO4 S0 sum_TWh (7,038 / 3,564 / 6,942) |
| Dok. 8:6 S: «en tredjedel» (s. 2); 12 GW og 120 prosjekter per oktober 2026 (s. 1) | – | dok8-202627-006s.pdf (truth/SOURCES K3) |
| Høringsinnspill til Dok. 8:321 S sendt | 20. oktober 2026 | ~/khepri-data/stortinget/dok8-321/KVITTERING_2026-10-20.txt (KJENTGRUNNLAG K6) |

## A-DC2 (utforskende, ikke preregistrert)
| Tall i teksten | Verdi | Kilde |
|---|---|---|
| Manus § 5: NO2 / NO5 A75 − A65 over netto flyt | 0,9–1,8 / 0,2–0,4 TWh/år | diagnose/ut/avvik_D.csv, −sum_D_TWh (NO2 1,77 / 1,36 / 0,86; NO5 0,33 / 0,43 / 0,17) |
| Manus § 5: NO1, NO3, NO4 under netto flyt | 0,1–0,5 TWh/år | samme (NO1 0,41 / 0,49 / 0,06; NO3 0,52 / 0,43 / 0,30; NO4 0,35 / 0,18 / 0,27) |
| Manus tabell 7 | generert | results/scenarier.csv + results/tillegg_a11_*.csv via build/lag_manustabeller.py |
| Komitéutkast: NO4 S0-andel, spenn | 18,3–16,4 / 36,4–35,2 / 7,6–6,8 % | scenarier.csv (hoved) / tillegg_a11_scenarier.csv, S0 andel_under0_pct |
| Komitéutkast: NO4 S3-andel, spenn | 34,5–33,3 / 60,0–59,4 / 30,1–27,7 % | samme, S3 |
| Komitéutkast: NO4 S0-årssum, spenn | 7,0–7,4 / 3,6–3,7 / 6,9–7,2 TWh | samme, S0 sum_TWh |
| Komitéutkast: NO4 S3-årssum, spenn | 1,5–1,9 / −1,9 til −1,7 / 1,6–1,9 TWh | samme, S3 sum_TWh |
| Komitéutkast: minste f NO4 / NO2, spenn | 43–46 / 22–23 / 44–45 %; 50–44 / 63–59 / 58–55 % | results/minste_f.csv (hoved) / tillegg_a11_minste_f.csv |
| Energikomité: NO2 S0 → S3 andel, spenn | 16,1–20,2 / 10,8–12,4 / 16,5–18,1 → 33,6–36,7 / 23,2–25,3 / 28,8–29,6 % | samme CSV-er |
| Energikomité: NO2 S3-årssum, spenn | 4,8–3,1 / 9,0–7,6 / 7,3–6,5 TWh | samme CSV-er |
| DIAGNOSE: alle tall | – | diagnose/ut/*.csv (avvik_D, pumpe_2025, dekning_elhub, dekomponering) |
