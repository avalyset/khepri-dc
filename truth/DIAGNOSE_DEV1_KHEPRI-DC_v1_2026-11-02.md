# DIAGNOSE av DEV-1 — KHEPRI-DC v1 (A-DC2, 2026-11-02)

**Utforskende, ikke preregistrert.** Gjort i etterkant av den preregistrerte analysen. analysis.py, PREREG og
RESULTATER er ikke endret (sha256 før: analysis.py ae46ae17c49ebf17aa62bf58ddcc6f0e96000aad198d3a20542cdd893959c095,
PREREG cb66dabd…98fc2, RESULTATER af658266…f8ee).

## Steg 1 — B10/B18 i koden (bekreftet)
- `build/build_series.py`, keyfn i A75-blokken: en TimeSeries utelates bare hvis den har `outBiddingZone_Domain.mRID`
  og **ikke** `inBiddingZone_Domain.mRID`. Alle andre summeres per psrType. Samme funksjon for 2023, 2024 og 2025.
- Rå XML (diagnose/sjekk_a75_serier.txt, kun metadata): ingen TimeSeries har både inn- og ut-domene, ingen har
  ingen av dem. Forbruksserier finnes bare i 2025: NO2 (B10, B18), NO3 (B10), NO5 (B10). I 2023–2024 finnes ingen
  forbruksserier, så ingen er feilaktig tatt med. B10-**produksjon** er med alle tre år i NO2, NO3 og NO5; B18-
  produksjon er med i NO2 2025.

## Steg 2 — Avvik D_t = NP(A11) − NP(A75−A65)
NP(A11) = Σ flyt ut − Σ flyt inn over sonens egne grenser (khepri_dc.analysis.np_a11).

### Forventet fortegn (skrevet og committet FØR tallene ble regnet)
- **Pumpeforbruk som mangler i A65** (art. 2 nr. 27: total load ekskluderer kraft til energilagring) gjør
  A75 − A65 for stor med pumpeforbruket, mens netto flyt ut ikke inneholder det. Da blir **D < 0**.
- **Produksjon som mangler i A75** (ufullstendig rapportering av små anlegg) gjør A75 − A65 for liten, mens netto
  flyt ut er målt. Da blir **D > 0**.
- Nettap: A65 inkluderer nettap (art. 2 nr. 27), og A11 måles på grensen. Hvis A65 også inneholder tap som ikke
  hører til sonens eget forbruk, eller mangler tap, kan det trekke begge veier; ingen forventet retning.
- Hvis begge de to første virker, kan de oppheve hverandre i middel og likevel gi stor middel |D| (spredning).

### Tall (regnet etter commit eba8147; diagnose/avvik_d.py, diagnose/ut/avvik_D.csv)

| Sone | År | Middel D = skjevhet (MW) | Median D (MW) | Andel D > 0 (%) | Årssum D (TWh) | Middel abs D (MW, = DEV-1) | Std D (MW) |
|---|---|---|---|---|---|---|---|
| NO1 | 2023 | 46,8 | 45,1 | 87,8 | 0,41 | 56,8 | 61,8 |
| NO1 | 2024 | 55,4 | 55,8 | 91,7 | 0,49 | 61,6 | 49,3 |
| NO1 | 2025 | 7,0 | 1,0 | 66,9 | 0,06 | 24,9 | 55,2 |
| NO2 | 2023 | −201,7 | −159,2 | 10,6 | −1,77 | 228,6 | 232,8 |
| NO2 | 2024 | −155,3 | −129,3 | 10,8 | −1,36 | 170,9 | 157,3 |
| NO2 | 2025 | −98,0 | −81,6 | 11,1 | −0,86 | 140,8 | 198,4 |
| NO3 | 2023 | 59,1 | 58,6 | 79,2 | 0,52 | 85,1 | 92,1 |
| NO3 | 2024 | 48,9 | 50,9 | 75,4 | 0,43 | 79,2 | 89,5 |
| NO3 | 2025 | 33,8 | 0,0 | 56,9 | 0,30 | 48,9 | 78,6 |
| NO4 | 2023 | 39,9 | 21,9 | 61,1 | 0,35 | 82,9 | 107,3 |
| NO4 | 2024 | 20,2 | 19,4 | 60,6 | 0,18 | 67,1 | 88,1 |
| NO4 | 2025 | 30,3 | 0,7 | 58,0 | 0,27 | 46,3 | 66,4 |
| NO5 | 2023 | −37,9 | −9,6 | 40,7 | −0,33 | 71,5 | 114,2 |
| NO5 | 2024 | −48,7 | −13,9 | 38,2 | −0,43 | 78,2 | 110,2 |
| NO5 | 2025 | −19,1 | 0,0 | 50,4 | −0,17 | 48,4 | 92,3 |

## Steg 3a — Pumpekraft (A75-forbruksserier, bare 2025; diagnose/ut/pumpe_2025.csv)

| Sone | psrType | Timer med verdi | Årssum pumpeforbruk (TWh) | Sum D i de samme timene (TWh) | r(D, pumpe) | Middel D når pumpe > 0 (MW) | Årssum D hele 2025 (TWh) |
|---|---|---|---|---|---|---|---|
| NO2 | B10 | 830 | 0,139 | −0,197 | −0,742 | −237,7 | −0,86 |
| NO2 | B18 | 0 | 0,000 | 0,000 | – | – | −0,86 |
| NO3 | B10 | 411 | 0,009 | −0,009 | −0,999 | −23,0 | 0,30 |
| NO5 | B10 | 421 | 0,042 | −0,041 | −0,995 | −97,4 | −0,17 |

## Steg 3b — Dekning mot Elhub (diagnose/dekning_elhub.py, diagnose/ut/dekning_elhub.csv; TWh, UTC-år)

| Sone | År | A75 | Elhub prod. | A75 − Elhub | A65 | Elhub forbruk | Elhub nettap | A65 − Elhub forbruk | A65 − (forbruk + nettap) |
|---|---|---|---|---|---|---|---|---|---|
| NO1 | 2023 | 20,53 | 20,84 | −0,31 | 34,27 | 32,01 | 2,25 | 2,27 | 0,01 |
| NO1 | 2024 | 21,19 | 21,66 | −0,47 | 35,08 | 32,89 | 2,19 | 2,19 | 0,01 |
| NO1 | 2025 | 19,52 | 19,72 | −0,19 | 34,26 | 32,42 | 1,98 | 1,84 | −0,14 |
| NO2 | 2023 | 50,35 | 50,55 | −0,20 | 35,15 | 34,35 | 2,22 | 0,80 | −1,42 |
| NO2 | 2024 | 55,40 | 55,62 | −0,22 | 36,08 | 34,94 | 2,36 | 1,14 | −1,22 |
| NO2 | 2025 | 53,94 | 54,42 | −0,47 | 36,37 | 35,32 | 2,11 | 1,05 | −1,07 |
| NO3 | 2023 | 23,50 | 24,24 | −0,74 | 27,97 | 26,88 | 1,38 | 1,10 | −0,29 |
| NO3 | 2024 | 22,87 | 23,55 | −0,68 | 28,42 | 27,42 | 1,32 | 1,00 | −0,31 |
| NO3 | 2025 | 27,05 | 27,77 | −0,72 | 28,95 | 28,10 | 1,35 | 0,84 | −0,50 |
| NO4 | 2023 | 27,81 | 28,05 | −0,23 | 20,77 | 19,38 | 1,26 | 1,39 | 0,13 |
| NO4 | 2024 | 23,73 | 23,91 | −0,18 | 20,16 | 19,01 | 1,17 | 1,15 | −0,02 |
| NO4 | 2025 | 26,97 | 27,61 | −0,64 | 20,02 | 19,21 | 1,23 | 0,81 | −0,41 |
| NO5 | 2023 | 30,20 | 30,37 | −0,17 | 16,32 | 15,67 | 0,99 | 0,65 | −0,35 |
| NO5 | 2024 | 32,23 | 32,48 | −0,25 | 17,09 | 16,63 | 1,02 | 0,46 | −0,56 |
| NO5 | 2025 | 32,11 | 32,41 | −0,30 | 17,13 | 16,46 | 1,01 | 0,67 | −0,34 |

### Elhubs definisjoner (truth/SOURCES, A-DC2)
- Forbruk (`consumption_per_group_mba_hour`): «Forbruk i kWh per time, prisområde og forbruksgruppe». Grupper:
  Husholdning, Hytter og fritidseiendommer, Primær Industri, Sekundær Industri, Tertiære Tjenester, Annen
  uspesifisert. **Om pumpeforbruk inngår: ikke oppgitt (ikke avklart).** Nettap er et eget datasett
  (`gridloss_per_hour_mba`: «summen av tap som følge av fysiske begrensninger i nettet og administrativt tap»), så
  forbruket regnes her som uten nettap.
- A65 inkluderer nettap etter art. 2 nr. 27. Lastavviket tolkes derfor mot Elhub forbruk + nettap, ikke som
  dekningsfeil: A65 − Elhub-forbruk (0,5–2,3 TWh) er i hovedsak nettap.

### Dekomponering (grov, utforskende; diagnose/ut/dekomponering.csv)
Hvis netto flyt ut ≈ Elhub-produksjon − Elhub-forbruk − nettap, er D ≈ (Elhub-prod − A75) + (A65 − forbruk − nettap):

| Sone | Årssum D 2023 / 2024 / 2025 (TWh) | Produksjonsledd | Lastledd | Sum av leddene |
|---|---|---|---|---|
| NO1 | 0,41 / 0,49 / 0,06 | 0,31 / 0,47 / 0,19 | 0,01 / 0,01 / −0,14 | 0,33 / 0,48 / 0,05 |
| NO2 | −1,77 / −1,36 / −0,86 | 0,20 / 0,22 / 0,47 | −1,42 / −1,22 / −1,07 | −1,23 / −1,00 / −0,59 |
| NO3 | 0,52 / 0,43 / 0,30 | 0,74 / 0,68 / 0,72 | −0,29 / −0,31 / −0,50 | 0,45 / 0,36 / 0,22 |
| NO4 | 0,35 / 0,18 / 0,27 | 0,23 / 0,18 / 0,64 | 0,13 / −0,02 / −0,41 | 0,36 / 0,17 / 0,23 |
| NO5 | −0,33 / −0,43 / −0,17 | 0,17 / 0,25 / 0,30 | −0,35 / −0,56 / −0,34 | −0,18 / −0,31 / −0,04 |

Leddene forklarer fortegnet i alle 15 sone-år og størrelsen godt i NO1, NO3 og NO4; i NO2 og NO5 forklarer de
53–73 % av årssummen i 2023–2024 (NO2 2025: 69 %, NO5 2025: 25 %).

### Observasjon (ikke testet)
I 2025 er |D| < 1 MW i 27 / 32 / 21 / 39 % av timene i NO1 / NO3 / NO4 / NO5 (53–75 % fra oktober 2025), mot
under 2 % i 2023–2024 og i NO2 alle år. Det tyder på at A65 eller A75 i 2025 delvis er avledet slik at identiteten
produksjon − last = netto flyt holder. Ikke undersøkt videre.

## Konklusjon per sone (utforskende)
D = NP(A11) − NP(hovedmål). D < 0: hovedmålet viser for høy nettoposisjon (for få timer under null). D > 0:
hovedmålet viser for lav nettoposisjon (for mange timer under null).

| Sone | Retning på skjevheten i hovedmålet | Grov størrelse | Trolig årsak |
|---|---|---|---|
| NO1 | NP for lav (D > 0) | 0,1–0,5 TWh/år | A75 under Elhub-produksjon (0,2–0,5 TWh) |
| NO2 | NP for høy (D < 0) | 0,9–1,8 TWh/år | A65 under Elhub forbruk + nettap (1,1–1,4 TWh); forenlig med pumpeforbruk som A65 utelater. A75-pumpeserien 2025 (830 timer, 0,14 TWh) følger D (r = −0,74), men dekker bare en liten del. At Elhub-forbruket inneholder pumping er ikke avklart. |
| NO3 | NP for lav (D > 0) | 0,3–0,5 TWh/år | A75 under Elhub-produksjon (~0,7 TWh), delvis motvirket av lastleddet |
| NO4 | NP for lav (D > 0) | 0,2–0,35 TWh/år | A75 under Elhub-produksjon (0,2–0,6 TWh) |
| NO5 | NP for høy (D < 0) | 0,2–0,4 TWh/år | Som NO2: lastleddet (−0,3 til −0,6 TWh); A75-pumpeserien 2025 følger D (r = −0,995) |

Betydning for hovedtallene: se results/TILLEGG_KHEPRI-DC_v1_2026-11-02.md (sensitivitet med NP fra A11). Størst
flytting i NO2 (S3-årssum 4,84 / 8,99 / 7,35 → 3,07 / 7,63 / 6,49 TWh; minste f 0,50 / 0,63 / 0,58 → 0,44 / 0,59 /
0,55). I NO4 flytter S3-andelen 34,5 / 60,0 / 30,1 % → 33,3 / 59,4 / 27,7 % og minste f 0,43 / 0,22 / 0,44 → 0,46 /
0,23 / 0,45.
