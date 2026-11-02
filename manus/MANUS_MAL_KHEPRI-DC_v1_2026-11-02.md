---
title: "Timevis nettoposisjon per budområde 2023–2025 med datasenterkøen lagt på"
subtitle: "KHEPRI-DC v1 — preregistrert, deskriptiv analyse i ettertid"
author: "Eirik Botten Nicolaysen, EcoDeco AS (eirik@ecodeco.no)"
date: "2. november 2026"
lang: nb
---

**Sammendrag.** Vi bruker ENTSO-E-data for produksjon (A75) og last (A65) per time i de fem norske budområdene for
2023, 2024 og 2025. På de observerte timene legger vi flat last tilsvarende datasenterkapasiteten som Statnett per
2. november 2026 har reservert eller satt i kø. Vi rapporterer hvor ofte, hvor mye og hvor dypt produksjonen ligger
under lasten. Analysen er preregistrert (signert git-tagg `prereg-v1`), deterministisk og ikke en prognose. Uten
påslag lå produksjonen under lasten i 76–99 % av timene i NO1 og 65–88 % i NO3, mens NO2, NO4 og NO5 hadde
overskudd på årsbasis alle tre år. Med en tredjedel av reservert og køsatt datasenterkapasitet (S3) stiger andelen
timer med produksjon under last i NO4 fra 18,3 / 36,4 / 7,6 % til 34,5 / 60,0 / 30,1 % (2023 / 2024 / 2025).
Netto import er ikke mangel eller rasjonering; tolkningsreglene i avsnitt 6 gjelder alle tall.

# 1 Bakgrunn

NVEs scenarioanalyse for 2026 legger 3,6 GW reservert datasenterkapasitet til grunn i sitt høyeste
datasenterscenario og skriver at «I denne analysen har vi ikke gjort egne analyser av hvordan endrede
utviklingsbaner for forbruk og produksjon mot 2035 vil kunne påvirke utviklingen i effektbalanse», og at «Særlig
gjelder dette datasentre, der vi har antatt en jevn forbruksprofil over året» (NVE Rapport 37/2026, s. 17 og 27).
NVE oppgir samtidig om lag 4 GW reservert og om lag 9 GW i kø for datasentre (s. 27). Analysen er en modell av
framtiden over 30 værår, med kraftbalanse og priser også per budområde (s. 16–20).

De Facto-rapport 4:2025 (Lekve, 7. august 2025, utført på oppdrag for Rødt) viser kraftbalanse per prisområde for
2021–2025 fra Elhub-data, med månedsoppløsning; rapporten viser figurer, og vi fant ikke data eller kode publisert
sammen med den. Riksrevisjonen fant at «Det
finnes ikke aggregert informasjon om den faktiske utnyttelsen av nettet» (Dokument 3:7 (2024–2025), s. 52), og at
det per september 2024 var reservert i overkant av 8 400 MW til forbrukskunder (s. 10).

Vi fant ikke noe åpent, etterprøvbart arbeid som i ettertid, time for time og per budområde, legger Statnetts
reservasjons- og køtall på observerte timer (kildegjennomgang i `truth/SOURCES`). Denne notaten gjør det, og stopper
der: vi modellerer ikke priser, nett inne i sonene, respons i produksjon eller import, eller effektbalanse.

# 2 Data

- **Produksjon:** ENTSO-E A75 (aggregert produksjon per type), sum over alle typer. Forbruksserier i A75 (B10 i
  NO2, NO3 og NO5 og B18 i NO2, bare i 2025) er utelatt.
- **Last:** ENTSO-E A65 faktisk totallast. Etter forordning (EU) 543/2013 art. 2 nr. 27 inkluderer «total load»
  nettap og ekskluderer kraft brukt til energilagring.
- **Fysisk flyt:** ENTSO-E A11 over de 15 grensene som berører NO1–NO5, begge retninger (kontroll).
- Rå XML (ENTSO-E Transparency Platform) er parset med «hold forrige verdi» (A03) og aggregert til varighetsvektet
  timemiddel i UTC. Alle 120 serie-år har 8 760 / 8 784 / 8 760 gyldige timer.
- **Datasenterkapasitet:** Statnett, «Statistikk om tilknytningssaker», forbruk, næringstype Datasenter, avlest
  2. november 2026 (arkivert med skjermbilder, sha256 og OpenTimestamps). R = reservert, Q = kapasitetskø.
- **Eksisterende datasenterlast:** Elhub `consumption_datacenter_per_mba_hour` (CC BY 4.0), per prisområde.
  E_y = gjennomsnittlig MW i år y; E_ref = E_2025.
- **Datatilgang:** A75- og A65-seriene distribueres ikke, fordi de ikke står på ENTSO-Es liste over åpne data
  (18.10.2023); med egen ENTSO-E-token bygges de byte-likt med `rebuild_data_KHEPRI-DC_v1.py`.

# 3 Metode

NP_t = produksjon_t − last_t (MW). Påslaget er flat last i år y og scenario s:
L = (E_ref − E_y) + 0,70 × (w × R_new + q × Q), der R_new = max(0, R − E_ref / 0,70) og 0,70 er NVEs brukstid.
Scenariene er S0 observert (L = 0), S1 (w = 0,25, q = 0), S2 (1, 0), S3 (1/3, 1/3) og S4 (1, 1). S4 er en øvre
grense og kan telle samme kapasitet to ganger, fordi prosjekter med reservasjon på særlige vilkår også står i kø.
Kurven setter w = q = f for f = 0,00–1,00. Utfall per sone og år: (i) andel timer med NP − L < 0, (ii) samme for
desember–februar, (iii) årlig sum av NP − L (TWh), (iv) laveste timeverdi (MW), og endring mot S0. Kontrollen
sammenligner NP med netto fysisk flyt ut av sonen (A11), med preregistrert grense MAE / middel |NP| ≤ 0,05.

Tabell 1 viser kapasitet og påslag (MW, 2025; for 2023 og 2024 kommer løftet E_ref − E_y i tillegg).

{{TABELL_LAST}}

# 4 Resultater

**Observert (S0).** Tabell 2: andel timer, sum og laveste verdi av NP uten påslag (2023 / 2024 / 2025).

{{TABELL_S0}}

**S3: en tredjedel av reservert og køsatt kapasitet.** Tabell 3 (2023 / 2024 / 2025).

{{TABELL_S3}}

**S4: all reservert og køsatt kapasitet (øvre grense).** Tabell 4 (2023 / 2024 / 2025).

{{TABELL_S4}}

S1 og S2 står i `results/scenarier.csv`. I NO3 er R (96 MW) mindre enn E_ref / 0,70, så R_new = 0 og S1 = S2.
Summen av de fem sonenes (iii) er 17,9 / 18,6 / 22,9 TWh observert, −12,3 / −11,1 / −5,6 TWh i S3 og
−69,2 / −68,1 / −62,5 TWh i S4. Disse summene er aritmetikk på de preregistrerte sonetallene, ikke egne
preregistrerte utfall.

**Kurve.** Tabell 5 viser minste f der årssummen blir ≤ 0 og der over halvparten av vintertimene har NP − L < 0.
Det andre punktet er et rapporteringspunkt, ikke en terskel for noe annet.

{{TABELL_F}}

![Kurve over f per sone: (iii) årlig sum NP − L og (ii) andel vintertimer med NP − L < 0, 2023–2025.](fig_kurver.png){width=100%}

**Kontroll.** Tabell 6. NP fra A75 − A65 følger netto fysisk flyt tett (r ≥ 0,985), men avviket er over den
preregistrerte grensen i NO2, NO3 og NO4 alle tre år (6–14 % av middel |NP|). Det er ført som avvik og ikke justert.
Årsaken er ikke undersøkt; mulige bidrag er pumpeforbruk, ufullstendig produksjonsrapportering og holdverdier i A11.

{{TABELL_KONTROLL}}

# 5 Begrensninger

Tolkningsreglene under er preregistrert og gjelder alle tall. I tillegg: Elhubs datasenterutvalg er målepunkt med
næringskode 63.100 og kan både over- og underdekke datasentre; Statnetts tall er en Power BI-visning uten historikk;
og kontrollen viser at A75 − A65 avviker fra netto fysisk flyt i tre av fem soner.

*Utforskende, ikke preregistrert (truth/DIAGNOSE_DEV1).* Avviket har en retning. I NO2 og NO5 ligger A75 − A65 over
netto fysisk flyt med 0,9–1,8 og 0,2–0,4 TWh per år, forenlig med pumpeforbruk som A65 etter definisjonen utelater.
I NO1, NO3 og NO4 ligger det under med 0,1–0,5 TWh per år, forenlig med at A75 ligger under Elhubs produksjonstall.
Hovedmålet viser dermed trolig for få timer under null i NO2 og NO5 og for mange i NO1, NO3 og NO4. Tabell 7 viser
hovedtallene regnet på nytt med NP fra A11 (hovedmål / A11).

{{TABELL_A11}}

# 6 Tolkningsregler (ordrett fra PREREG)

1. Netto import er ikke mangel eller rasjonering.
2. Vannkraft og import er normal drift.
3. Naboområdenes last holdes uendret.
4. Ingen kapasitet på enkeltlinjer inne i sonen er modellert (Svartisen-stoppen gjelder ikke hele NO4).
5. Kø og reservasjoner er et øyeblikksbilde fra 2026 lagt på observerte timer fra 2023–2025.
6. Tre observerte år, ikke 30 værår.
7. 2025 rapporteres for seg: det var et år med rekordhøy produksjon (161 TWh) og rekordhøyt kraftoverskudd
   (23 TWh), mot om lag 15 TWh i et normalår (NVE Rapport 17/2026, s. 2).

# 7 Konklusjon

I de observerte timene 2023–2025 hadde NO1 og NO3 produksjon under last i de fleste timer, og NO2, NO4 og NO5 hadde
overskudd på årsbasis. Når Statnetts reserverte og køsatte datasenterkapasitet legges på som flat last, endres
fortegnet på årssummen i NO4 ved f = 0,43 / 0,22 / 0,44 og i NO2 ved f = 0,50 / 0,63 / 0,58; i NO5 skjer det ikke for
noen f. Tallene beskriver observerte timer med et påslag. De sier ikke hva som vil skje, og de er ikke en anbefaling
for eller mot datasentre.

**Data og kode:** [ZENODO-DOI]. Kode Apache-2.0, data CC BY 4.0. Kilder: ENTSO-E Transparency Platform; Elhub
(CC BY 4.0); Statnett. **KI-bruk:** analysen er utført med Claude Code som verktøy under forfatterens styring
(AIUSE.md).
