# DECISIONS — KHEPRI-DC v1 (2026-11-02)

Alle valg under er tatt **før** tagg prereg-v1, uten at balanse, nettoposisjon, importtimer eller summer av
produksjon/last er beregnet eller vist.

## D1 Eksisterende datasenterlast E_y (steg 3)
- **Kilde:** Elhub `consumption_datacenter_per_mba_hour` (CC BY 4.0), timeforbruk per prisområde for målepunkt med
  næringskode 63.100 (Elhubs avgrensning; kan både over- og underdekke datasentre). Lastet ned 2026-11-02, sha256
  `f03d3098c728c64a846a70c610de52afb6d06ee1cfbee60cc0e8cbc58ec1d79f` (utpakket CSV). For 2023–2025 identisk med
  kopien fra 2026-09-21 (131 520 felles rader, 0 ulike verdier).
- **Valg:** Elhub gir tall **per prisområde**. Hovedvalget er derfor Elhub per sone, ikke nasjonal fordeling etter
  reservasjonsandel (oppdragets hovedvalg gjaldt bare hvis kun nasjonale tall fantes).
- E_y = Σ kWh i UTC-år y / (timer i året × 1000) (MW). E_ref = E_2025 (siste hele år).
- **Sensitivitet:** E = 0 i alle soner og år (da R_new = R og løftet er 0). Sensitiviteten «hele nasjonal last i hver
  sone» kjøres ikke, fordi sonetall finnes; den var definert for tilfellet med bare nasjonale tall.
- Avvik å kjenne: nasjonal sum 2025 fra denne fila er 3,14 TWh; NVE oppgir 3,3 TWh (Elhub) og Rapport 17/2026
  «til 3 TWh». Forskjellen kan skyldes datauttrekk eller næringskoder (63.100 vs 63.110); ikke løst.

| Sone | E_2023 (MW) | E_2024 (MW) | E_2025 = E_ref (MW) |
|---|---|---|---|
| NO1 | 15,73 | 40,60 | 96,97 |
| NO2 | 11,41 | 17,98 | 26,68 |
| NO3 | 60,47 | 93,71 | 153,83 |
| NO4 | 65,13 | 70,99 | 81,10 |
| NO5 | 2,70 | 0,89 | 0,06 |

## D2 Kapasitet R og Q (steg 2)
- Statnett, Statistikk om tilknytningssaker (Power BI), forbruk, næringstype Datasenter, avlest to ganger 2026-11-02
  (identisk). R = reservert, Q = kapasitetskø. Arkiv: arkiv/STATNETT_ARKIV_KHEPRI-DC_v1_2026-11-02.md.
- R: NO1 1 398, NO2 1 950, NO3 96, NO4 477, NO5 270 MW. Q: NO1 2 220, NO2 3 092, NO3 1 646, NO4 2 258, NO5 894 MW.
- R_new = max(0, R − E_ref/0,70) som i oppdraget. Merknad: Statnett skiller «tilknyttet» fra «reservert», så
  fratrekket kan være konservativt (trekker fra last som ikke ligger i R). Formelen beholdes som spesifisert.

## D3 Produksjon og last (A75, A65)
- Produksjon = sum over alle produksjonstyper i A75 (TimeSeries med inBiddingZone_Domain). En type uten verdi i en
  time bidrar 0; timen er manglende bare hvis ingen type har verdi. Antall typer per time lagres (n_typer).
- A75-forbruksserier (TimeSeries med outBiddingZone_Domain) utelates fra produksjonen. Byggetellingen (kun metadata)
  viser at slike finnes bare i 2025: B10 (pumpekraft) i NO2, NO3 og NO5, og B18 (havvind) i NO2. I 2023 og 2024 har
  A75 ingen forbruksserier i noen sone. Pumpeforbruket ligger dermed verken i produksjonen eller (etter definisjonen)
  i A65; det kan bidra til avviket i kontrollen for 2025.
- Last = A65 faktisk totallast, processType A16, outBiddingZone_Domain = sonen.
- **Definisjon (forordning (EU) 543/2013, art. 2 nr. 27, ordrett fra EUR-Lex, lest 2026-11-02):** «‘total load’,
  including losses without power used for energy storage, means a load equal to generation and any imports
  deducting any exports and power used for energy storage». A65 **inkluderer nettap** og **ekskluderer kraft brukt
  til energilagring (pumping)**. A75 er «aggregated generation output per market time unit and per production type»
  (art. 16 nr. 1 b); pumpekraftverk (B10) rapporteres som produksjon. Følgelig: A75 − A65 = netto eksport +
  pumpeforbruk (hvis seriene er komplette). Om norsk A65 i praksis følger definisjonen for pumping: **ikke avklart**.
- Timeverdi = varighetsvektet middel av A03-ekspanderte intervaller (15/30/60 min); timen er manglende hvis
  intervallene ikke dekker 60 minutter. Overlappende filer (måned + år) slås sammen; ulike verdier på samme tidspunkt
  telles som konflikt og første forekomst beholdes.

## D4 Kontrollgrense
- **MAE(NP_A11 − NP) / middel |NP| ≤ 0,05** per sone og år.
- Begrunnelse: Etter art. 2 nr. 27 er produksjon − total last = netto eksport + pumpeforbruk, og A11 måler netto
  eksport direkte over sonens grenser. Avviket skal derfor bare skyldes pumpeforbruk, ufullstendig A75 (små
  anlegg), måle-/estimeringsforskjeller og A03-holdverdier i A11. 5 % av middel |NP| er lite nok til at et
  systematisk avvik som kan flytte andelen timer under null, blir oppdaget, og stort nok til å tåle tilfeldig
  måleavvik. Utenfor grensen rapporteres som funn; ingenting justeres (steg 5).

## D5 Utfallsdefinisjoner
- Timer uten gyldig NP (produksjon eller last mangler) utelates fra alle utfall; antall timer rapporteres.
- (ii) desember–februar = januar, februar og desember **i samme UTC-år** y.
- (iii) TWh = Σ (NP − L) × 1 h / 10⁶ over gyldige timer.
- Kurve: f = 0,00–1,00 i steg 0,01, w = q = f, løftet (E_ref − E_y) er med også ved f = 0.

## D6 Data som bygges før taggen
- Fra rå XML (alle tre serier, alle tre år) med khepri_dc/entsoe_xml.py. A75 2023–2025, A65 2025 og A11 2025 er
  hentet på nytt som rå XML (P1Y) i A-DC1, slik at alle serier bygges med samme dokumenterte A03-parser
  (diskfilene fra A-DC0 var allerede parset CSV med ukjent A03-håndtering).
