# DEVIATIONS — KHEPRI-DC v1 (2026-11-02)

Ført straks etter første kjøring av analysis.py på taggen prereg-v1 (commit e160f44, tagg-objekt 034095e7).
Ingen kode, data eller parametre er endret etter taggen.

## DEV-1 Kontrollen er utenfor den preregistrerte grensen for NO2, NO3 og NO4 (alle tre år)
- Preregistrert grense: MAE(NP_A11 − NP) / middel |NP| ≤ 0,05 (PREREG § 6, DECISIONS D4).
- Utfall (results/kontroll.csv): innenfor for NO1 og NO5 alle år (0,015–0,044). Utenfor for
  NO2 (0,113 / 0,072 / 0,061), NO3 (0,136 / 0,113 / 0,113) og NO4 (0,089 / 0,103 / 0,056) for 2023 / 2024 / 2025.
  Pearson r er 0,9854–0,9995 i de 15 sone-årene (0,9854–0,9948 i de ni som er utenfor grensen).
- **Ingenting er justert.** Hovedtallene står som preregistrert. Manus og sammendrag skal si at NP fra A75 − A65 i
  NO2, NO3 og NO4 avviker fra netto fysisk flyt med 6–14 % av middel |NP| (MAE 46–229 MW).
- Mulige forklaringer, **ikke testet**: pumpeforbruk (A65 ekskluderer det etter art. 2 nr. 27; A75-forbruksseriene
  for 2025 er utelatt), ufullstendig A75 for små anlegg, nettap i A65 versus målepunkt for A11, og A03-holdverdier i
  A11. En undersøkelse av årsaken er ikke del av PREREG og er ikke gjort.

## Tilleggskontroll utenfor PREREG (post hoc, ikke et avvik i analysen)
- Summen av (iii) S0 over de fem sonene er 17,9 TWh (2023), 18,6 TWh (2024) og 22,9 TWh (2025). NVE Rapport
  17/2026 oppgir et kraftoverskudd på 23 TWh i 2025 (s. 2). Kontrollen er gjort etter taggen, er ikke preregistrert
  og brukes bare som ytre konsistenssjekk.

## Merknader om utfall som følger direkte av formelen (ikke avvik)
- NO3: R (96 MW) er mindre enn E_ref/0,70 (219,8 MW), så R_new = 0. S1 og S2 gir da bare løftet (E_ref − E_y); i
  2025 er løftet 0, så S1 = S2 = S0 for NO3 i 2025.
