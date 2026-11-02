# KHEPRI-DC v1.0.0

**Timevis nettoposisjon per norsk budområde 2023–2025 med datasenterkøen lagt på.**
Preregistrert, deskriptiv og deterministisk analyse i ettertid. Ikke en prognose.

DOI: [ZENODO-DOI] · Forfatter: Eirik Botten Nicolaysen, EcoDeco AS · Kode Apache-2.0 (LICENSE) · Data og tekst
CC BY 4.0 (LICENSE-DATA)

## Hva som er målt
For hvert budområde NO1–NO5 og hver UTC-time i 2023, 2024 og 2025: NP = produksjon (ENTSO-E A75, sum alle typer)
− last (ENTSO-E A65). På de observerte timene legges flat last
L = (E_ref − E_y) + 0,70 × (w × R_new + q × Q), der R og Q er datasenterkapasitet som Statnett har reservert og
satt i kø (avlest 2. november 2026), og E er eksisterende datasenterlast fra Elhub. Scenarier S0–S4 og en kurve over
f = w = q. Utfall: andel timer med NP − L < 0 (hele året og desember–februar), årssum (TWh), laveste time (MW).

## Tolkningsregler
1. Netto import er ikke mangel eller rasjonering.
2. Vannkraft og import er normal drift.
3. Naboområdenes last holdes uendret.
4. Ingen kapasitet på enkeltlinjer inne i sonen er modellert (Svartisen-stoppen gjelder ikke hele NO4).
5. Kø og reservasjoner er et øyeblikksbilde fra 2026 lagt på observerte timer fra 2023–2025.
6. Tre observerte år, ikke 30 værår.
7. 2025 rapporteres for seg: det var et år med rekordhøy produksjon (161 TWh) og rekordhøyt kraftoverskudd
   (23 TWh), mot om lag 15 TWh i et normalår (NVE Rapport 17/2026, s. 2).

## Hovedtall (fra results/RESULTATER_KHEPRI-DC_v1_2026-11-02.md)
- Observert hadde NO1 produksjon under last i 76–99 % av timene og NO3 i 65–88 %; NO2, NO4 og NO5 hadde overskudd
  på årsbasis alle tre år.
- Med en tredjedel av reservert og køsatt datasenterkapasitet (S3) stiger andelen timer med NP − L < 0 i NO4 fra
  18,3 / 36,4 / 7,6 % til 34,5 / 60,0 / 30,1 % (2023 / 2024 / 2025).
- Årssummen i NO4 blir ≤ 0 ved f = 0,43 / 0,22 / 0,44 og i NO2 ved f = 0,50 / 0,63 / 0,58; i NO5 ikke for noen f.
- Kontrollen (A11) er utenfor den preregistrerte grensen i NO2, NO3 og NO4 (truth/DEVIATIONS, DEV-1).

## Datatilgang
Pakken inneholder **ikke** de bearbeidede A75- og A65-seriene (`data/produksjon_A75.parquet`, `data/last_A65.parquet`).
ENTSO-E publiserer bare et utvalg data under CC BY 4.0 (Terms of Use 29.03.2023, pkt. 2.5), og «List of Data available
for free re-use» (18.10.2023) omfatter fysisk flyt (art. 12.1.g, A11), men ikke faktisk last (6.1.a, A65) eller faktisk
produksjon per type (16.1.b/c, A75). Med i pakken: kode, `data/flyt_A11.parquet` (Kilde: ENTSO-E Transparency
Platform, data element 12.1.g; CC BY 4.0; endret: aggregert til timemiddel per UTC-time og forutfylt etter A03),
Elhub-uttakene i `data/elhub/` (CC BY 4.0), aggregerte resultater, TILLEGG, sha256 for A75/A65
(`data/SHA256_A75_A65_KHEPRI-DC_v1.txt`) og prereg-bevis (`prereg-bevis/`).

To veier: (a) **med egen ENTSO-E-token**: `ENTSOE_API_TOKEN=… python rebuild_data_KHEPRI-DC_v1.py --fetch --raw-dir raw`
bygger de to filene; skriptet sjekker sha256 og innholdshash mot manifestet, og deretter gir `analysis.py` RESULTATER
byte-likt (sha256 af658266…f8ee). Har du rå XML fra før, bruk `--raw-dir`. (b) **uten token**: kontroller A11-delen
(`diagnose/sens_a11_KHEPRI-DC_v1.py` gir results/TILLEGG) og de aggregerte tallene i results/.

Prereg-tarballen publiseres ikke fordi den inneholder A75/A65. OTS-beviset (forankret i Bitcoin-blokk 974257) gjelder
tarballens sha256 (`prereg-bevis/*.sha256`), og `prereg-bevis/PREREG-MANIFEST_…txt` gir sti og sha256 for hvert medlem.
Den fulle utviklingshistorikken og den signerte taggen prereg-v1 (commit e160f44) ligger i forfatterens private arkiv.

## Reproduser
```bash
python3.12 -m venv venv && venv/bin/pip install -r requirements.txt
venv/bin/python -m pytest -q tests
venv/bin/python rebuild_data_KHEPRI-DC_v1.py --raw-dir raw     # eller --fetch med ENTSOE_API_TOKEN, se Datatilgang
venv/bin/python -m khepri_dc.analysis --data data --params params/parametre.json --out results
shasum -a 256 results/RESULTATER_KHEPRI-DC_v1_2026-11-02.md   # skal være lik SHA256SUMS
```
Rå XML er ikke med (sha256 i truth/SHA256_RAADATA_…). `build/build_series.py` bygger data/*.parquet fra rå XML;
`build/lag_parametre.py` bygger params/parametre.json fra Elhub-fila.

## Filer
| Sti | Innhold |
|---|---|
| `prereg/` | PREREG, sha256 for alle filer i taggen |
| `prereg-bevis/` | OTS-bevis og sha256 for prereg-tarballen, manifest over medlemmene, tagg-teksten (tarballen publiseres ikke) |
| `rebuild_data_KHEPRI-DC_v1.py` | bygger A75/A65-parquet fra rå XML (egen token eller `--raw-dir`) |
| `khepri_dc/` | `entsoe_xml.py` (A03-parser, timeaggregering), `analysis.py` (preregistrert analyse) |
| `build/` | bygging av parquet, parametre, manustabeller og samlefigur |
| `data/` | flyt_A11 (parquet, UTC-timer), sha256 for A75/A65 (ikke distribuert), byggetelling, `elhub/` (Elhub-uttak, CC BY 4.0) |
| `params/parametre.json` | R, Q (Statnett), E_y (Elhub), brukstid |
| `results/` | RESULTATER (md), CSV, kurvefigurer |
| `results/TILLEGG_…`, `results/tillegg_a11_*.csv` | sensitivitet med NP fra A11 (utforskende, ikke preregistrert) |
| `diagnose/` | diagnose av DEV-1 (utforskende, ikke preregistrert); tall i `diagnose/ut/`, tekst i truth/DIAGNOSE_DEV1 |
| `manus/` | manus (md + pdf ≤ 6 sider) |
| `arkiv/` | Statnett Power BI-skjermbilder, energiministerens svar 08.05.2025, sha256 + OTS |
| `truth/` | KJENTGRUNNLAG, SOURCES, DECISIONS, DEVIATIONS, NUMBERS, STATE |
| `tests/` | tester på syntetiske data |

## Kilder og kildeangivelse
- Produksjon, last og fysisk flyt: **Kilde: ENTSO-E Transparency Platform** (https://transparency.entsoe.eu).
- Datasenterforbruk, produksjon, forbruk og nettap: **Kilde: Elhub**, CC BY 4.0 (datasettene i `data/elhub/`).
- Reservert kapasitet og kapasitetskø: Statnett, «Statistikk om tilknytningssaker», avlest 2. november 2026.

## KI-bruk
Se AIUSE.md. KI-erklæring: implementert med Claude Code.
