# PREREG — KHEPRI-DC v1 (2026-11-02)

**Tittel:** Timevis nettoposisjon per norsk budområde 2023–2025 med datasenterlast lagt på etter Statnetts
reservasjons- og køtall.
**Forfatter:** Eirik Botten Nicolaysen, EcoDeco AS (eirik@ecodeco.no).
**Type:** Deskriptiv, deterministisk analyse i ettertid. Ikke en prognose. Ingen hypotesetesting.
**Status ved registrering:** Ingen balanse, nettoposisjon, importtimer eller summer av produksjon/last er beregnet
eller sett. Bearbeidede timeserier er bygget og committet; analysis.py er testet bare på syntetiske data.
Registreres som signert git-tagg `prereg-v1` (GPG C96D4E5C5636088C), tarball med sha256 og OpenTimestamps-bevis.

## 1 Spørsmål
Hvor ofte, hvor mye og hvor dypt ville produksjonen i hvert norsk budområde ha ligget under lasten i de
observerte timene i 2023, 2024 og 2025, hvis datasenterlasten som i dag er reservert eller står i kø hos Statnett,
hadde vært lagt på som flat last?

## 2 Data
- Budområder NO1–NO5. Timer i UTC. Årene 2023, 2024 og 2025 analyseres hver for seg.
- **Produksjon** = sum av ENTSO-E A75 (aggregert produksjon per type, processType A16) over alle typer.
- **Last** = ENTSO-E A65 faktisk totallast (processType A16).
- **Fysisk flyt** = ENTSO-E A11 over hver grense som berører sonen, begge retninger (15 grenser, 30 serier).
- Rå XML er hentet fra ENTSO-E Transparency Platform (sha256 i truth/). Bearbeidede timeserier i `data/*.parquet`
  (sha256 i prereg/SHA256_PREREG…). Rå XML committes ikke.
- Timeverdi = varighetsvektet middel av A03-ekspanderte intervaller («hold forrige verdi»); timen er manglende hvis
  intervallene ikke dekker 60 minutter (truth/DECISIONS D3).
- **Definisjon av A65** (forordning (EU) 543/2013 art. 2 nr. 27): «‘total load’, including losses without power
  used for energy storage, means a load equal to generation and any imports deducting any exports and power used
  for energy storage». A65 inkluderer nettap og ekskluderer pumpeforbruk. A75 rapporterer pumpekraft (B10) som
  produksjon. Forbruksserier i A75 (outBiddingZone_Domain) finnes bare i 2025 (B10 i NO2, NO3, NO5; B18 i NO2) og
  utelates fra produksjonen. Om norsk A65 i praksis ekskluderer pumping: ikke avklart.

## 3 Størrelser
- NP_t = produksjon_t − last_t (MW).
- Datasenterkapasitet per sone (Statnett, avlest 2026-11-02, forbruk, næringstype Datasenter):
  R = reservert, Q = kapasitetskø.

| Sone | R (MW) | Q (MW) | E_2023 | E_2024 | E_2025 = E_ref (MW) |
|---|---|---|---|---|---|
| NO1 | 1 398 | 2 220 | 15,73 | 40,60 | 96,97 |
| NO2 | 1 950 | 3 092 | 11,41 | 17,98 | 26,68 |
| NO3 | 96 | 1 646 | 60,47 | 93,71 | 153,83 |
| NO4 | 477 | 2 258 | 65,13 | 70,99 | 81,10 |
| NO5 | 270 | 894 | 2,70 | 0,89 | 0,06 |

  E_y = gjennomsnittlig eksisterende datasenterlast i år y (Elhub, per prisområde; nøyaktige verdier i
  params/parametre.json).
- Brukstid b = 0,70 (NVE, metodenotat 11.08.2026, s. 4).
- Ny reservert kapasitet: R_new = max(0, R − E_ref / 0,70).
- Lagt på flat last i år y og scenario s: **L_{s,y} = (E_ref − E_y) + 0,70 × (w_s × R_new + q_s × Q)**.

## 4 Scenarier
| Scenario | w | q | Beskrivelse |
|---|---|---|---|
| S0 | – | – | Observert, uten løft (L = 0) |
| S1 | 0,25 | 0 | NVE-vektet (25 % for reservert kapasitet) |
| S2 | 1 | 0 | All reservert kapasitet |
| S3 | 1/3 | 1/3 | En tredjedel av reservert + kø |
| S4 | 1 | 1 | Reservert + kø, øvre grense |

S4 kan telle samme kapasitet to ganger: Statnett oppgir at prosjekter med reservasjon på særlige vilkår også står i
kø på ordinære vilkår.
**Kurve:** w = q = f, f = 0,00–1,00 i steg 0,01 (løftet E_ref − E_y er med også ved f = 0).
**Sensitivitet:** E = 0 i alle soner og år (R_new = R, ingen løft).

## 5 Utfall (per sone, år, scenario)
1. Andel timer med NP − L < 0.
2. Samme andel for desember–februar (januar, februar og desember i samme UTC-år).
3. Årlig sum av NP − L (TWh) over gyldige timer.
4. Laveste timeverdi av NP − L (MW).
5. Endring mot S0 for 1–4.

Fra kurven: minste f der (3) ≤ 0, og minste f der (2) > 50 % (rapporteringspunkt, ikke en kriseterskel). Nås ingen
f: «ikke nådd». Timer uten gyldig NP utelates; antall timer rapporteres.

## 6 Kontroll
NP fra A11 = Σ flyt ut − Σ flyt inn over sonens egne grenser, sammenlignet med A75 − A65 per sone og år: middel
absolutt avvik (MAE), MAE / middel |NP| og Pearson-korrelasjon. **Grense: MAE / middel |NP| ≤ 0,05.** Begrunnelse i
truth/DECISIONS D4. Utenfor grensen rapporteres som funn i truth/DEVIATIONS; ingenting justeres.

## 7 Tolkningsregler (ordrett i PREREG og manus)
1. Netto import er ikke mangel eller rasjonering.
2. Vannkraft og import er normal drift.
3. Naboområdenes last holdes uendret.
4. Ingen kapasitet på enkeltlinjer inne i sonen er modellert (Svartisen-stoppen gjelder ikke hele NO4).
5. Kø og reservasjoner er et øyeblikksbilde fra 2026 lagt på observerte timer fra 2023–2025.
6. Tre observerte år, ikke 30 værår.
7. 2025 rapporteres for seg: det var et år med rekordhøy produksjon (161 TWh) og rekordhøyt kraftoverskudd
   (23 TWh), mot om lag 15 TWh i et normalår (NVE Rapport 17/2026, s. 2).

Resultatene sendes til Stortingets næringskomité (Dok. 8:321 S (2025–2026)) og energi- og miljøkomité (Dok. 8:6 S (2026–2027)) uansett utfall.

## 8 Analyse og avvik
- `khepri_dc/analysis.py` kjøres **uendret** på de committede parquet-filene og params/parametre.json.
- Resultater: results/RESULTATER_KHEPRI-DC_v1_2026-11-02.md + CSV + kurvefigur per sone.
- Ethvert avvik fra denne planen føres straks i truth/DEVIATIONS med sha256 og OpenTimestamps.
- Uavhengig reproduksjon: en fersk agent får bare Zenodo-tarballen, bygger ren venv, kjører pytest og analysis.py,
  og RESULTATER må bli byte-lik.

## 9 Hva studien ikke er
Ikke en prognose, ikke en modell av kraftmarkedet (ingen priser, ingen respons i produksjon eller import), ikke en
vurdering av effektbalanse eller forsyningssikkerhet, og ingen anbefaling for eller mot datasentre.
