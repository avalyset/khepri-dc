# SOURCES — KHEPRI-DC v0 (2026-11-02)

Alle kilder lastet ned 2026-11-02 med ærlig UA `KHEPRI-DC-roykttest/0.1 (eirik@ecodeco.no)` til
`/Volumes/Vault/khepri-dc/kilder/<nøkkel>/` (ikke i repoet), konvertert med `pdftotext -layout` og søkt med
`/usr/bin/grep`. sha256 i `SHA256_KILDER_KHEPRI-DC_v0_2026-11-02.txt`. Sitater under er ordrett fra den
nedlastede teksten (fil:linje), ikke fra søkesammendrag. To nedlastinger ga 404 (Elhub-analysene
`norske_datasentre_forbruksanalyse.pdf` og `Norske-datasentre-1.pdf`); filene i `elhub_dc1/` er 404-sider.

## Verifisering av KJENTGRUNNLAG

| # | Status | Primærkilde (fil:linje) | Merknad |
|---|---|---|---|
| K1 NVE metodenotat | **Verifisert** | nve_metode.txt:125–126 «Per mars 2026 var det reservert 3 500 MW strøm i kraftnettet til nye datasentre ifølge Tilknytningsregisteret til Statnett.»; :121 3,3 TWh 2025 (Elhub); :68–73 brukstid 70 %; tabell 1 :99–103 75/50/25 %; :148–149 «fra 3,3 TWh i 2025 til rundt 8 TWh i 2030» | Ingen soneinndeling eller timeprofil i notatet (eneste «timer» er 8 760 i formelen :135). 3 500 MW = **kun reservert**, kun datasentre. |
| K2 Riksrevisjonen Dok 3:7 | **Verifisert** | dok3_7.txt:365–371 «Per september 2024 … reservert i overkant av 8 400 MW til forbrukskunder»; «datasentre (ca 1500 MW)»; :4633 «Det finnes ikke aggregert informasjon om den faktiske utnyttelsen av nettet.» | Sitatet gjelder utnyttelse av **nettet**, ikke datasentre spesielt. |
| K3 Dok 8:6 S (Rødt) | **Verifisert** | dok8_6s.raw.txt:49–55 «Per oktober 2026 har Statnett reservert eller køsatt om lag 12 GW nettkapasitet til datasenterprosjekter, fordelt på rundt 120 prosjekter.»; :59 «Hvis bare en tredjedel av disse prosjektene realiseres, vil kraftoverskuddet forsvinne» | Kilden for 12 GW er ikke oppgitt i forslaget. Riktig URL: stortinget.no/globalassets/pdf/representantforslag/2026-2027/dok8-202627-006s.pdf |
| K4 TU 19.05.2026 (NVE) | **Verifisert mot NVE-primærkilden** (NVE Rapport 17/2026), ikke mot TU | nve_r2026_17.txt:9–11 161 TWh, 23 TWh, ~15 TWh normalår; :362 «om lag 4 TWh i 2030» | TU-artikkelen ikke hentet; primærkilden er bedre. |
| K5 TU 05.05.2026 | **Verifisert** | tu_571604 (datePublished 2026-05-05T11:13:27Z): «Dagens forbruk fra Salten og nordover er i dag omtrent 1500 megawatt (MW)… reservert nettkapasitet til 1150 MW nytt forbruk, omtrent 1100 MW står i kø.»; tu_571210 (2026-04-22): stans i reservasjoner >5 MW nord for Svartisen | 1150 MW bekreftet i Statnett-brev 15.06.2026 (statnett_rme_svartisen.txt:87). 1100 MW kø kun fra TU. TU 05.05 oppgir også datasentre 334 MW reservert nord for Svartisen. |
| K6 Dok 8:321 S | Ikke rørt | ~/khepri-data/stortinget/dok8-321/ (lokal) | Utenfor røyktestens behov. |

## Øvrige primærkilder brukt

| Nøkkel | Kilde | URL |
|---|---|---|
| nve_r2026_17 | NVE Rapport 17/2026 «Status og utvikling i kraftsystemet 2025-2030» | https://publikasjoner.nve.no/rapport/2026/rapport2026_17.pdf |
| nve_r2026_37 | NVE Rapport 37/2026 «Scenarioer for kraftmarkedet 2026. Utfallsrom for kraftbalansen mot 2035» | https://publikasjoner.nve.no/rapport/2026/rapport2026_37.pdf |
| dok15_2086 | Energiministerens svar på skriftlig spørsmål 2086 (2024–2025), 08.05.2025, vedlegg med tabell per kommune | https://www.stortinget.no/globalassets/pdf/dokumentserien/2024-2025/dok15-202425-2086-vedlegg.pdf |
| statnett_web | Statnett «Statistikk om tilknytningssaker» (Power BI), avlest 02.11.2026 | https://www.statnett.no/nettkapasitet-til-produksjon-og-forbruk/foresporsler-og-reservasjon-i-nettet/ (avlesning: kilder/statnett_web/POWERBI_AVLESNING_2026-11-02.md, kopiert til repo/analyse/) |
| statnett_nordnorge_nve | Statnett, svarbrev til NVE om forsyningssikkerhet i Nord-Norge, 15.06.2026 | statnett.no/globalassets/…/svarbrev-nve-om-utredninger-av-forsyningssikkerhet-i-nord-norge-15.06.2026.pdf |
| statnett_rme_svartisen | Statnett, svarbrev til RME om tilknytningsplikt nord for Svartisen, 15.06.2026 | statnett.no/globalassets/…/svarbrev-rme---tilknytningsplikt-nord-for-svartisen-15.06.2026.pdf |
| statnett_sorvaranger | Statnett, brev til Barents Nett: grensen for vanlig forbruk 1 MW i Sør-Varanger | statnett.no/contentassets/3a3ca2827b494b94b9f4d5c25970a76c/… |
| statnett_kvu_helg | Statnett, dialogmøte KVU Helgeland–Sverige, 12.03.2026 | statnett.no/globalassets/her-er-vare-prosjekter/region-nord/kvu-helgeland-sverige/… |
| statnett_sup2025 | Statnett Systemutviklingsplan 2025 | statnett.no/globalassets/…/sup/systemutviklingsplan-2025.pdf |
| statnett_lma2024 | Statnett Langsiktig markedsanalyse 2024–2050 | statnett.no/globalassets/…/lma/langsiktig-markedsanalyse-2024-50.pdf |
| statnett_atk | Statnett Analyse av transportkanaler 2025–2050 | statnett.no/globalassets/…/atk/analyse-av-transportkanaler-2025-2050.pdf |
| omr_* | Statnett områdeplaner 2025 (Midt, Helgeland og Salten, Sør-Rogaland og Agder, Telemark og Vestfold, Innlandet, Hallingdal og Ringerike, Sogn til Sunnmøre) | statnett.no/globalassets/…/omradeplaner/… |
| menon2026 | Menon-publikasjon 129/2026 «Økonomiske aspekter ved den norske datasenternæringen» (for DFD, publisert 29.10.2026) | regjeringen.no/contentassets/7d1bb1a439c049adbbad8073f5b3e10f/… |
| thema2035 | THEMA (for Elvia), «Strømforsyningen 2035», 12.08.2026 | elvia.no/siteassets/dokumenter/rapporter/… |
| defacto_hvemtar | De Facto-rapport 4:2025, Isak Lekve, «Hvem tar kraften?» | https://de-facto.no/wp-content/uploads/2025/09/Hvem-tar-kraften.pdf |
| arxiv_2608_19622 | Khanal et al., «Shift or curtail?…», arXiv:2608.19622 | https://arxiv.org/pdf/2608.19622 (PJM, ikke Norge) |
| tu_debatt | TU debatt, Sivert Ø. Hamar (Octave), 21.10.2026 | https://www.tu.no/debatt/norge-har-kraften-men-kan-ikke-si-nar-den-er-tilgjengelig/7147089 |

## Ikke funnet
- CIGRE C1-11880 (2026): to søk, ingen treff på papirnummeret. Ikke vurdert.
- Statnett Kortsiktig markedsanalyse: nyeste funnet er 2021–2026 (des. 2021); ingen nyere i søk.
- Elhubs datasenteranalyser (to PDF-er): 404.

---

# A-DC1 (2026-11-02): ordrette kilder før tagg prereg-v1

Sidetall er PDF-sidenummer (`pdftotext`, skilt på sideskift); for NVE 37, De Facto og NVE-notatet er de lik trykt
sidenummer. Søkeskript: $V/inventar/sidesok.py.

## NVE Rapport 37/2026 «Scenarioer for kraftmarkedet 2026. Utfallsrom for kraftbalansen mot 2035»
- **Effektbalansen er ikke modellert** (s. 17): «I denne analysen har vi ikke gjort egne analyser av hvordan
  endrede utviklingsbaner for forbruk og produksjon mot 2035 vil kunne påvirke utviklingen i effektbalanse.»
- **Datasenterlast antatt flat** (s. 17): «Særlig gjelder dette datasentre, der vi har antatt en jevn
  forbruksprofil over året.» Også s. 27: «Det økte forbruket til datasentre antas å gi en jevn økning i
  kraftforbruket over året.»
- **Scenarioene** (s. 11): «S3 Datasenter: En raskere vekst i datasentre, som gir 6 TWh høyere forbruk i 2035 enn i
  LA25. S4 Høy datasenter: Øvre utfallsrom for datasentre mot 2035, som gir 17 TWh økning fra LA25. S5 Datasenter
  Klimaplan: Virkemidlene i Klimaplan, med forbruksbanen Datasenter lagt til grunn.» S4 bygger på «en reservert
  kapasitet til datasentre på 3,6 GW» (s. 27); S5 gir «om lag 9 TWh høyere forbruk i 2035, sammenlignet med Basis»
  (s. 28).
- **Kapasitet og brukstid** (s. 27): «Per august 2026 er det reservert om lag 4 GW kapasitet til datasentre i
  eksisterende og planlagt nett fram mot 2035.» «Med en antatt brukstid på 70 prosent, tilsvarer dette et totalt
  årlig kraftforbruk på rundt 25 TWh.» «Per mai 2026 viste Statnetts tilknytningsregister totalt 120 saker fra
  datasenteraktører som ønsker nettilknytning, med en total kapasitet på om lag 9 GW.»
- NB: KHEPRI-DC v1 måler heller ikke effektbalanse. Den legger flat last på observerte timer per sone. Den
  ordrette «hullet»-formuleringen er derfor at NVE 37 ikke analyserer effektbalanse og antar flat datasenterlast,
  ikke at NVE har latt et timevis sonemål stå åpent.

## De Facto-rapport 4:2025 «Hvem tar kraften?» (Isak Lekve)
- **Dato og oppdragsgiver** (s. 3): «Arbeidet er utført på oppdrag for Rødt.» «Side, 7.august 2025 Isak Lekve».
- **Metode** (s. 18, fotnote 2): «Alt tallmaterialet i den følgende gjennomgangen kommer fra Elhub, som er et heleid
  datterselskap av Statnett med ansvar for å overvåke og samle inn statistikk om det norske kraftmarkedet.»
  Oppløsningen er måned: (s. 20) «I tallmaterialet skiller mars 2025 seg ut med et ekstremt høyt forbruk som er
  nesten tre ganger høyere enn både i februar, men også tre ganger høyere enn mars i 2024.» Figurer 8–12
  «Kraftbalanse NOx 2021-2025. Kilde: Elhub.», figur 13 for 1.04.24–31.03.25. Ingen data eller kode publisert.
- **Soneresultater (år)**: NO1 (s. 17–18): «NO1 er et underskuddsområde med en negativ kraftbalanse som riktignok
  er blitt noe redusert fra om lag 15 TWh til 11 TWh de siste årene». NO2 (s. 18): «positiv kraftbalanse som
  riktignok varierer mye, men som likevel ligger på over 16 TWh i gjennomsnitt». NO3 (s. 19): «produserer omtrent
  like mye som det forbruker, men tenderer mot å gå med et lite underskudd på rundt 2 TWh». NO4 (s. 20): «Om vi tar
  det for gitt og fjerner mars 2025, ser vi at også NO4 er et område som over tid har et solide overskudd, som
  riktignok har vært noe synkende, fra nesten 12 TWh i 2022 til under 5 TWh i 2024.» NO5 (s. 21): «NO5 er en solid
  overskuddregion med årlige overskudd på mellom 12 og 16 TWh.»
- Merk: Elhub-balanse (målt forbruk og produksjon i Elhub) er en annen datakilde enn ENTSO-E A75/A65.

## NVE metodenotat 11.08.2026 og Rapport 17/2026
- Notatet: brukstid 70 % (s. 4: «en brukstid på 70 prosent var en rimelig gjennomsnittsverdi for norske
  datasentre»); sannsynligheter (s. 5, tabell 1: «Startet å bygge Ja 75 % Tatt investeringsbeslutning Ja 50 %
  Reservert kapasitet Ja 25 %»); 3,3 TWh 2025 (s. 6: «Statistikk fra Elhub viste at det ble brukt 3,3 TWh strøm i
  norske datasentre i 2025.»); 3 500 MW (s. 6: «Per mars 2026 var det reservert 3 500 MW strøm i kraftnettet til
  nye datasentre ifølge Tilknytningsregisteret til Statnett.»); ~8 TWh 2030 (s. 6).
- Rapport 17/2026: «I 2025 hadde Norge en historisk høy kraftproduksjon på 161 TWh, og et rekordhøyt kraftoverskudd
  på 23 TWh.» og «om lag 15 TWh i et gjennomsnittsår» (s. 2); «Bare i 2025 økte kraftforbruket til datasentre i
  Norge med over 1 TWh, til 3 TWh.» (s. 4); fotnote «* Antatt brukstid på 70%» ved figur 29.
- Alle tall i KJENTGRUNNLAG K1 og K4 stemmer med kildene; ingen rettelse.

## Statnett Kortsiktig markedsanalyse — nyeste funnet: KMA 2024–2029 (sept. 2024)
- Hentet fra https://www.statnett.no/globalassets/for-aktorer-i-kraftsystemet/planer-og-analyser/kma/kortsiktig-markedsanalyse-2024-2029.pdf
  (også via NTB). KMA 2025–2030 er nevnt i søk (Statnett-nyhet 01.09.2025), men ingen PDF ble funnet (4 URL-forsøk
  ga 404).
- **Timevise resultater per prisområde med datasentre? Nei.** Datasentre omtales bare generelt (s. 15: «KI og
  digitalisering gir høy vekst innen datasentre, og i IEAs siste prognose øker det globale kraftforbruket til
  datasentre med 4-500 TWh de neste tre årene.»). Modellene er framoverskuende optimeringsmodeller (s. 47: «Disse er
  optimeringsmodeller med algoritmer som minimerer de samlede produksjonskostnadene time for time i det samlede
  kraftsystemet i Norden og Europa»).

## arXiv:2604.26634 (Phan mfl., v2 3. juni 2026)
- **Gjør det samme som oss? Nei.** Prisprognoser: «Here we present a comprehensive evaluation of one-step-ahead
  forecasting of the Nord Pool market across all five Norwegian bidding zones. We constructed a multimodal hourly
  dataset spanning 2019–2025» (s. 1). Ingen nettoposisjon, ingen datasenterlast, ingen kø.

## NVE LA25 (Rapport 15/2025, «Langsiktig kraftmarkedsanalyse 2025»)
- **Gjør det samme som oss? Nei.** Modell av framtiden over 30 værår: «Framtidige priser er modellerte og viser
  gjennomsnittlig kraftpris over et år basert på 30 ulike værår.» (s. 6). R37 bruker samme modellapparat (R37 s. 11
  og fotnote 18). Ingen observert timebalanse per sone koblet til kø.

## Konklusjon steg 1
Ingen funnet kilde gjør steg 5 (åpent, etterprøvbart, i ettertid, time for time per budområde, med kø-tall lagt på).
Analysen fortsetter.

## Forordning (EU) 543/2013 (EUR-Lex, lest i nettleser 2026-11-02, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32013R0543)
- Art. 2 nr. 27: «‘total load’, including losses without power used for energy storage, means a load equal to
  generation and any imports deducting any exports and power used for energy storage».
- Art. 16 nr. 1 b: «aggregated generation output per market time unit and per production type».
- Merk: curl mot EUR-Lex ga HTTP 202 uten innhold; teksten ble lest i Claude-nettleserpanelet (DOM-tekst, ordrett).

## Elhub
- `consumption_datacenter_per_mba_hour` (CC BY 4.0), https://data.elhub.no/download/consumption_datacenter_per_mba_hour/consumption_datacenter_per_mba_hour-all-no-0000-00-00.csv
  (gzip), lastet ned 2026-11-02; utpakket sha256 f03d3098c728c64a846a70c610de52afb6d06ee1cfbee60cc0e8cbc58ec1d79f.

---

# A-DC2 (2026-11-02): Elhub-datasett (CC BY 4.0)

Lisens (Elhub, ordrett gjengitt i ~/khepri-data/datasenter-v0/README.md): «Våre datasett er tilgjengelige under
Creative Commons Attribution 4.0 International (CC BY 4.0).» Definisjonene under er lest i nettleserpanelet
2026-11-02 fra Elhubs Confluence (DOM-tekst, ordrett). Nedlastinger med UA «KHEPRI-DC/1.0 (eirik@ecodeco.no)»;
filene er gzip-komprimert CSV (semikolon, desimalkomma). Rådata ligger i $V/kilder/elhub*/ og committes ikke;
sha256 også i truth/SHA256_ELHUB_KHEPRI-DC_v1_2026-11-02.txt (+ .ots).

## E_y: datasenterforbruk (brukt i preregistrert analyse)
- Datasett: `consumption_datacenter_per_mba_hour`. URL:
  https://data.elhub.no/download/consumption_datacenter_per_mba_hour/consumption_datacenter_per_mba_hour-all-no-0000-00-00.csv
- Uttak: 2026-11-02 ca. 12:32 UTC. sha256 gzip `d8959cddc0803ceac10afc3ea2fc3945ff8c558df5feb33637a396e506a6ebea`,
  utpakket CSV `f03d3098c728c64a846a70c610de52afb6d06ee1cfbee60cc0e8cbc58ec1d79f`.
- Definisjon (https://elhub.atlassian.net/wiki/spaces/Data/pages/2566717544/Forbruk+i+datasentre+per+prisomr+de+og+time,
  «Updated Jun 18»): «Forbruk for norske datasentre i kWh per time og prisområde.» «Med datasentre mener vi her alle
  målepunkt som er registrert i Elhub med næringskodene 63.100og 63.110 i Standard for næringsgruppering
  (SN2025-09)» (sic, manglende mellomrom i kilden). STARTTID: «Timen forbruket er brukt på i norsk tid».
- Forbehold (dashbordet, gjengitt i datasenter-v0/README): næringskode 63.100 er bredere enn datasentre, og Elhub
  verifiserer ikke næringskoder.

## Diagnose DEV-1 (utforskende)
- `production_per_group_mba_hour`, https://data.elhub.no/download/production_per_group_mba_hour/production_per_group_mba_hour-all-no-0000-00-00.csv
  — definisjon (…/pages/834174980/Produksjon+per+prisomr+de+gruppe+og+time, «Updated Jun 10»): «Produksjon i MWh per
  time, prisområde og produksjonsgruppe»; kolonnen heter likevel VOLUM_KWH («Det aggregerte volumet»). Verdiene er
  behandlet som kWh (gir årssummer på linje med A75). Grupper: Sol, Termisk, Vann, Vind uspesifisert, og «*»
  (7 777 rader, udokumentert). sha256 gzip `fea1897e0e226e66674a2bd827590d3e1939e3e63efacb29a44eaf7eb74aa830`.
- `consumption_per_group_mba_hour`, …/consumption_per_group_mba_hour-all-no-0000-00-00.csv — definisjon
  (…/pages/836108294/Forbruk+per+prisomr+de+gruppe+og+time): «Forbruk i kWh per time, prisområde og forbruksgruppe».
  Om pumpeforbruk inngår, er ikke oppgitt. sha256 gzip `0eb2df92ac27b75f3d1bdcc10270f0df66d97e1d77b02ef8bc5625c5a4b148c2`.
- `gridloss_per_hour_mba`, …/gridloss_per_hour_mba-all-no-0000-00-00.csv — definisjon (…/pages/2132836353/Nettap+per+time+og+prisomr+de,
  «Updated May 11»): «Nettapet er definert som summen av tap som følge av fysiske begrensninger i nettet og
  administrativt tap, dvs. tap der det ikke er noen sluttbruker.» Enhet MWh. sha256 gzip
  `cc9757082378a1922a884760f54a4d39ec2c5f964703007a8f78effef081fab1`.
- Uttak for de tre: 2026-11-02, ferdig 13:31 UTC.

---

# A-DC2 steg 9 (2026-11-02): datavilkår for ENTSO-E-seriene

## (a) Egne tidligere notater (kun lesing)
- LICENSE-DATA i dette repoet: CC BY 4.0 (legal code, hentet fra creativecommons.org i A-DC1).
- Khepri (~/khepri, gren v2-dev-dk-fi), eds/revisjon/khepri-eds-R1.txt:2137–2138 (innsendt manus, ordrett): «Raw
  ENTSO-E generation extracts are not redistributed, because the ENTSO-E Transparency Platform terms do not permit
  it; they are retrieved reproducibly through the documented API queries in the repository.» Samme i
  eds/REVISION-NOTES.md:28–30. Khepri v1.5 la derfor ikke ut rå A75.
- khepri-consumption-2025 (~/dev/khepri-consumption-2025) README § Licence: «Code Apache-2.0 (`LICENSE`). Data and
  documentation CC BY 4.0 (`LICENSE-DATA`), as v1.» Ingen egen vurdering av ENTSO-E-vilkår funnet der.

## (b) Gjeldende ENTSO-E-vilkår (lest 2026-11-02)
- Vilkårsside: https://transparencyplatform.zendesk.com/hc/en-us/articles/40921911218961-Legal-Terms-and-Conditions
  (lenket fra transparency.entsoe.eu som «Platform Terms & Conditions»). Gjeldende versjoner: Terms of Use 29.03.2023
  (gjelder fra 01.11.2023) og «List of Data available for free re-use» 18.10.2023.
- Lastet ned (UA «KHEPRI-DC/1.0 (eirik@ecodeco.no)») til $V/kilder/entsoe_vilkaar/:
  `vilkaar_230329.pdf` (…/article_attachments/40921869376401) sha256
  665d08621f711e3c0971581b15b2572e69054d4a017f693e32c20924d476352b; `liste_231018.pdf`
  (…/article_attachments/40921869379729) sha256 b21717e8a5a41b9b8544db730d11c2a717abc9b07f89704437a89332b708ff9a.
- Terms of Use 2.5 (s. 5): «ENTSO-E currently publishes a subset of the Transparency Platform data available under an
  open source license (CC-BY 4.0) for the free use of Data Users (hereinafter ‘’Open Data’’).»
- Terms of Use 3.1 (s. 6): Data User skal «mention the ENTSO-E Transparency Platform as the source of publication of
  the data» og «not cause prejudice to the copyright or related right on a Transparency Platform Data, which may be
  owned by the concerned Primary Owner of Data. In case of a risk to cause prejudice to said right, the Data User
  shall seek the prior agreement of the holder of the copyright or related right.» Listen over fritt gjenbrukbare
  data gjør at man slipper å «seek for the prior agreement of the respective Primary Owner of Data».
- Terms of Use 5.1 (s. 8–9): «Transparency Platform Data may be subject to copyright owned by the Primary Owner of
  Data.» Rettighetene til bruk av plattformen er «not sub-licensable or transferrable».
- Listen 18.10.2023 (s. 1): data på listen «can be freely re-used … under a Creative Commons Attribution 4.0
  International License (CC-BY 4.0). Data Users may freely copy, redistribute, and adapt the listed data for any
  purpose, by giving appropriate credit (attribution) to its source and indicating if they have made any changes».
  Unntak gjelder MD, TR, enkelte UA-poster og tre interconnectorer; **Norge er ikke unntatt**.
- **Hva som står på listen (s. 1–5):** post 1–4 er 6.1.b–e (lastprognoser); post 18 er «Physical flows» 12.1.g
  (= A11). **6.1.a (faktisk totallast, A65) og 16.1.b/c (faktisk produksjon per type, A75) står ikke på listen.**
  Listen er per dataelement, ikke per land, så dette gjelder også NO1–NO5.
- Om plattformens grensesnitt merker enkeltserier som «open data»: ikke sjekket.

## Vurdering (til RAPPORT; tarballen er ikke endret)
- `data/flyt_A11.parquet` (fra 12.1.g): **ja**, kan ligge i Zenodo-pakken under CC BY 4.0 med kildeangivelse og
  merknad om endringer (timemiddel, A03-ekspansjon).
- `data/produksjon_A75.parquet` og `data/last_A65.parquet` (fra 16.1.b/c og 6.1.a): **uavklart**, med helning mot
  nei. Dataene er ikke på listen over åpne data, Primary Owner (for Norge trolig Statnett) kan ha rettigheter, og
  vilkårene gir ingen rett til å lisensiere dem videre under CC BY 4.0. Det tryggeste er Statnetts skriftlige
  samtykke, eller å la pakken bare inneholde kode og sha256, slik Khepri gjorde. Om sum per sone og time er et
  nytt verk som ikke berører rettighetene, er et rettslig spørsmål som ikke er avklart her.

---

# A-DC3 (2026-11-02): Elhubs lisens
- https://data.elhub.no/ (datakatalog, hentet 2026-11-02, $V/kilder/elhub_pf/dataset_index_adc3.html), ordrett:
  «Alle datasett er gratis å bruke og tilgjengelige under CC BY 4.0 – du kan fritt kopiere, distribuere og bearbeide
  dataene, også kommersielt, så lenge du viser til Elhub som kilde.» og «Våre datasett er tilgjengelige under
  Creative Commons Attribution 4.0 International (CC BY 4.0) . Lisensen gir deg rett til å kopiere, distribuere og
  bearbeide dataene slik du måtte ønske, også i kommersiell sammenheng, så lenge du viser til Elhub som kilde.»
  Lenke til https://creativecommons.org/licenses/by/4.0/.
- Følge: lisensen er åpen; de fire Elhub-uttakene (sha256 i truth/SHA256_ELHUB_…) legges i pakken under data/elhub/
  med kildeangivelse «Kilde: Elhub».
