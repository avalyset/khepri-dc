# SMOKE — KHEPRI-DC v0 (2026-11-02)

Oppdrag A-DC0: røyktest for KHEPRI-DC (timevis balanse per budområde mot datasenterkøen).
Kun gjennomførbarhet. **Ingen balansestørrelse er beregnet** (produksjon − last, nettoposisjon, overskudd,
importtimer). Tidsseriene er ikke sett på eller plottet; datainventaret teller timer. Ett avvik er ført i
truth/STATE (A1: fire rader A75-verdier for NO1 sett ved formatsjekk).

Kilder og verifisering: truth/SOURCES_KHEPRI-DC_v0_2026-11-02.md. Rådata og nedlastede kilder ligger på Vault
utenfor repoet; sha256 i truth/.

## Vurdering

**GO.** Alle tre kriteriene holder, med forbeholdene i del 4: (a) det er ikke funnet noe åpent,
reproduserbart arbeid i ettertid, time for time per budområde, koblet til kø-tallene; (b) A75, A65 og A11 har
100 % av timene i alle NO-soner og grenser i 2023–2025; (c) Statnett publiserer reservert og køsatt forbruk med
definisjon per prisområde (også NO4) og for hele Norge, både for datasentre og for alt forbruk.

## 1 Tidligere arbeid

19 nettsøk (grense 25). Primærkildene er lastet ned og søkt i som tekst. «Kø» = kobler til Statnetts tall for
reservert kapasitet og/eller kapasitetskø.

| Verk | Tidsoppløsning | Romlig enhet | I ettertid / modell | Åpne data, reproduserbart | Kobler til kø-tall | Lenke |
|---|---|---|---|---|---|---|
| Statnett, Langsiktig markedsanalyse 2024–2050 (feb. 2025) | Modell time for time (teksten bruker «time for time» om priser og flyt) | Prisområde/region, Norden/Europa | Modell, framover | Nei (lukket modell) | Nei, forbruksbaner, ikke kø | statnett.no/…/lma/langsiktig-markedsanalyse-2024-50.pdf |
| Statnett, Kortsiktig markedsanalyse (siste funnet: 2021–2026, des. 2021) | År | Norge, Sør/Nord | Modell, framover | Nei | Nei | statnett.no/…/kortsiktig-markedsanalyse-2021-2026.pdf |
| NVE Rapport 17/2026, Status og utvikling i kraftsystemet 2025–2030 | År (energi) og effekt; 2025 i ettertid | Norge; kø vist per NO1–NO5 (fig. 30, bare grafisk) | Status 2025 + framskriving | Nei | Ja: 20 800 MW (7 800 reservert, 13 000 kø), mai 2026; per sone kun i figur | publikasjoner.nve.no/rapport/2026/rapport2026_17.pdf |
| NVE Rapport 37/2026, Scenarioer for kraftmarkedet 2026 (mot 2035) | Modell, 30 værår; datasenterlast antatt «jevn … over året» | Prisområde (priser) | Modell, framover | Nei | Ja: ~4 GW reservert (aug. 2026), ~9 GW kø (mai 2026), >20 GW forespurt; S4 bygger på 3,6 GW reservert | publikasjoner.nve.no/rapport/2026/rapport2026_37.pdf |
| NVE langsiktig kraftmarkedsanalyse (LA25) | Ikke hentet; R37 bruker samme modellapparat (R37:379, :422) | Prisområde | Modell, framover | Nei | Ikke verifisert | — |
| NVE metodenotat datasentre, 11.08.2026 | År | Norge | Framskriving | Formelen er gjengitt; data ikke | Ja: 3 500 MW reservert (mars 2026) | publikasjoner.nve.no/diverse/2026/Metode…2026.pdf |
| Statnett områdeplaner 2025 (7 hentet) | Ingen timebalanse; MW-status | Statnett-region | Status + planer | Nei | Ja (MW reservert/kø per område) | statnett.no/…/omradeplaner/… |
| Statnett, brev til NVE om Nord-Norge, 15.06.2026 | Simulert 2025 (varighetskurve for flyt over Kobbelvsnittet) og energibalanse | Nord for Svartisen / Nord-Norge | Modell | Nei | Ja: 1 150 MW reservert nord for Svartisen + ~1 000 MW Helgeland | statnett.no/…/svarbrev-nve-…-15.06.2026.pdf |
| Menon 129/2026 for DFD, «Økonomiske aspekter ved den norske datasenternæringen» (29.10.2026) | År, scenarier 2030/2035 | Forbruk og priser per prisområde; balanse nasjonal | Scenarier + markedsmodell (FRAM/JulES) | Nei | Ja: ~22 600 MW reservert eller i kø, om lag halvparten datasentre; fig. 4-4 per prisområde | regjeringen.no/…/menon-rapport-…pdf |
| THEMA for Elvia, «Strømforsyningen 2035» (12.08.2026) | Ingen timebalanse | Landsdel | Utfallsrom, framover | Nei | Ja (etterspørsel etter nettkapasitet) | elvia.no/…/stromforsyningen-2035…pdf |
| De Facto 4:2025, «Hvem tar kraften?» (Lekve) | **Ikke time.** Figurer for 2021–2025 (trolig måned; ikke verifisert) og for 01.04.24–31.03.25 | **Prisområde NO1–NO5** | **I ettertid** (Elhub) | Nei: bare figurer, ingen kode eller data | Delvis: kø per næring nasjonalt + liste over datasenterprosjekter i NO4 | de-facto.no/…/Hvem-tar-kraften.pdf |
| Riksrevisjonen Dok 3:7 (2024–2025) | — | Norge | Revisjon | — | Ja (8 400 MW reservert, sep. 2024) | stortinget.no/…/dok3-202425-007.pdf |
| CIGRE C1-11880 (2026) | Ikke funnet (2 søk) | — | — | — | — | — |
| Scholar/arXiv: arXiv:2608.19622 (Khanal mfl.) | Time | Noder, **PJM (USA)** | Modell | — | Nei (PJM-kø, ikke norsk) | arxiv.org/abs/2608.19622 |
| Scholar/arXiv: arXiv:2604.26634 | Time, NO1–NO5 2019–2025 | Budområde | Prisprognoser | Ikke sjekket | Nei (bare søkesammendrag; ikke hentet) | arxiv.org/abs/2604.26634 |
| Eget, upublisert: ~/khepri-data/datasenter-v0 (21.09.2026) | Time | Prisområde | I ettertid | Lokalt | Nei, **utslipp** fra Elhub-datasenterforbruk, ikke balanse | lokalt |

**Konklusjon del 1:** Det nærmeste i ettertid er De Facto 4:2025. Den viser balanse per prisområde fra
Elhub-data og har kø-tall ved siden av, men den er ikke time for time, publiserer verken data eller kode og
kobler køen bare nasjonalt og per næring. Arbeidene som er time for time per prisområde (Statnett LMA,
NVE R37, Menon/FRAM-JulES, Statnetts Nord-Norge-simulering) er modeller av framtiden med lukkede data.
**Det er ikke funnet noe åpent, reproduserbart arbeid i ettertid, time for time per budområde, koblet til
kø-tallene.** Forbehold: CIGRE C1-11880 ble ikke funnet og er ikke vurdert. LA25 og arXiv:2604.26634 er ikke
lest i fulltekst.

## 2 Datainventar

Full tabell (120 rader: serie × sone/grense × år): INVENTAR_KHEPRI-DC_v0_2026-11-02.md (utført av
Sonnet-subagent, kun tellinger). Rådata ligger på Vault utenfor repoet; 835 sha256-er i
truth/SHA256_RAADATA_KHEPRI-DC_v0_2026-11-02.txt.

| Serie | Sone/grense | 2023 | 2024 | 2025 | Kilde |
|---|---|---|---|---|---|
| A75 produksjon per type | NO1–NO5 (5) | 8 760/8 760 (100 %) | 8 784/8 784 (100 %) | 8 760/8 760 (100 %) | disk: ~/khepri-data/raw/entsoe-rest/ (alle år) |
| A65 faktisk totallast | NO1–NO5 (5) | 100 %, 0 mangler | 100 %, 0 mangler | 100 %, 0 mangler | 2023–24 hentet (ENTSO-E); 2025 disk: /Volumes/Vault/khepri-data/flowtracing/raw/2025/A65 |
| A11 fysisk flyt | 15 grenser × 2 retninger (30) | 100 %, 0 mangler | 100 %, 0 mangler | 100 %, 0 mangler | 2023–24 hentet; 2025 disk: …/flowtracing/raw/2025/A11 |

- Delvise timer (1–3 kvarter): 0 i alle rader. Grenselisten er identisk med entsoe-py `NEIGHBOURS` for NO_1–NO_5;
  NO4–RU ga «ingen data» (reason 999) og publiseres ikke.
- Henting: 317 P1M-kall + 44 P1Y-kall, alle HTTP 200, ingen 429, ingen «ingen data». P1Y er støttet av en
  sekundærkilde («1 year range limit applies») og av at alle kallene lyktes; API-guiden selv ga 403/400 og er
  **ikke** sitert ordrett.
- **Kryssjekk i hovedøkten** med egen parser (analyse/kryssjekk_dekning.py, bare tidsintervaller): A65 NO4 2024
  8 784/8 784 og A11 NO4→SE1 2023 8 760/8 760. Det stemmer med inventaret.
- Forbehold: (i) «til stede» betyr at timen er dekket av en Period med A03-semantikk (hold forrige verdi).
  A11 er i stor grad hold-verdier (flyt rapporteres ved endring); det er dekning, ikke kontroll av innhold.
  (ii) A03-håndteringen i disk-CSV-ene (A75 alle år, A65/A11 2025) er ikke dokumentert; full dekning tyder på
  ekspansjon, men det er ikke verifisert. (iii) A75 «alle typer har verdi» er under 100 % for enkelte sone-år
  (f.eks. NO1 2024: 5 738/8 784, NO2 2025: 2 183) fordi typesettet varierer gjennom året; kriteriet (b) er tolket
  som «minst én type per time».

## 3 Reservasjonstall per sone

Alle tall gjelder **forbruk** (uttak). «Reservert» = kapasitet Statnett har reservert i eksisterende eller
planlagt nett. «Kø» = modne saker i kapasitetskø («bestilt, men som Statnett ikke ennå kan reservere»).
Fra Statnett: der det er reservert kapasitet på særlige vilkår, står prosjektet **også** i kø på ordinære
vilkår, så reservert + kø kan telle samme MW to ganger.

### 3a Per budområde, Statnetts statistikk (avlest 02.11.2026)

Kilde: Statnett «Statistikk om tilknytningssaker», Power BI «Oversikt», filtre Prisområde og Næringstype
(analyse/POWERBI_AVLESNING_KHEPRI-DC_v0_2026-11-02.md). Budområdene kommer **direkte fra kilden**, ikke fra
vår antakelse. Sonesummene stemmer med landstallet (±1 MW avrunding).

| Område | Datasenter reservert | Datasenter kø | Alt forbruk reservert | Alt forbruk kø |
|---|---|---|---|---|
| NO1 | 1 398 | 2 220 | 1 801 | 2 748 |
| NO2 | 1 950 | 3 092 | 2 456 | 5 989 |
| NO3 | 96 | 1 646 | 963 | 2 782 |
| **NO4** | **477** | **2 258** | **1 831** | **3 864** |
| NO5 | 270 | 894 | 1 104 | 1 379 |
| **Norge** | **4 190** | **10 109** | **8 154** | **16 761** |

Svakheter: øyeblikksbilde i en Power BI-visning, uten versjonert nedlasting og uten historikk. Statnett tar
forbehold om «enkelte feil eller mangler». Avlesningen må gjentas og arkiveres (skjermbilde/eksport) før den
brukes i en preregistrering.

### 3b Andre tall med definisjon

| Verdi | Dato | Definisjon | Geografi | Kilde | Sitat (ordrett) |
|---|---|---|---|---|---|
| 3 500 MW | mars 2026 | Reservert, datasentre | Norge | NVE metodenotat 11.08.2026 | «Per mars 2026 var det reservert 3 500 MW strøm i kraftnettet til nye datasentre ifølge Tilknytningsregisteret til Statnett.» |
| ~4 GW | aug. 2026 | Reservert, datasentre, eksisterende og planlagt nett | Norge | NVE R37/2026 | «Per august 2026 er det reservert om lag 4 GW kapasitet til datasentre i eksisterende og planlagt nett» |
| ~9 GW, 120 saker | mai 2026 | Kø, datasentre | Norge | NVE R37/2026 | «Per mai 2026 viste Statnetts tilknytningsregister totalt 120 saker fra datasenteraktører som ønsker nettilknytning, med en total kapasitet på om lag 9 GW.» |
| >20 GW | sep. 2026 (uttrekk) | Forespurt (Tilko/ElBits), datasentre | Norge | NVE R37/2026 | «ytterligere over 20 GW er forespurt» |
| ~12 GW, ~120 prosjekter | okt. 2026 | Reservert **eller** kø, datasentre | Norge | Dok 8:6 S (Rødt) | «Per oktober 2026 har Statnett reservert eller køsatt om lag 12 GW nettkapasitet til datasenterprosjekter, fordelt på rundt 120 prosjekter.» |
| ~22 600 MW | 2026 (Menon) | Reservert eller kø, alt forbruk; om lag halvparten datasentre | Norge | Menon 129/2026 | «Datasentre står for om lag halvparten av de rundt 22 600 MW som har fått reservert kapasitet eller står i kapasitetskø hos Statnett.» |
| 20 800 MW (7 800 res. / 13 000 kø); datasentre ~10 200 MW | mai 2026 | Reservert + kø, alt forbruk | Norge (per NO1–NO5 i fig. 30, kun grafisk) | NVE R17/2026 | «Per mai 2026 venter til sammen rundt 20 800 MW på tilknytning, fordelt på 7800 MW reservert i eksisterende eller planlagt nett, og 13 000 MW i kapasitetskø.» |
| ~7 700 MW | 3. kv. 2025 | Reservert, alt forbruk | Norge | Statnett SUP 2025 | «Per tredje kvartal 2025 har Statnett reservert kapasitet til omtrent 7 700 MW nytt forbruk» |
| 8 400 MW; datasentre ~1 500 MW | sep. 2024 | Reservert, alt forbruk / datasentre | Norge | Riksrevisjonen Dok 3:7 | «reservert i overkant av 8 400 MW til forbrukskunder»; «datasentre (ca 1500 MW)» |
| 9 829 MW aktive saker; 2 362 res.; 4 210 kø | 08.05.2025 | Datasentre: reservert / kø / «andre saker» 3 257 MW | Norge + **tabell per kommune** | Dok 15:2086 (energiministerens svar) | «9 829 MW er saker knyttet til datasentre. Av disse er 2 362 MW reservert, mens 4 210 MW er plassert i kapasitetskø.» |
| 1 150 MW reservert | 15.06.2026 | Reservert, alt nytt forbruk | Nord for Svartisen (≈ nordlige NO4) | Statnett til RME | «Statnett har reservert kapasitet til ca. 1150 MW nytt forbruk.» |
| ~1 100 MW kø; 334 MW datasentre reservert | 05.05.2026 | Kø, alt forbruk; reservert, datasentre | Salten og nordover / nord for Svartisen | TU 05.05.2026 | «reservert nettkapasitet til 1150 MW nytt forbruk, omtrent 1100 MW står i kø»; «Nest etter Melkøya (350 MW) har datasentre flest reservasjoner nord for Svartisen, til sammen 334 MW.» |
| nærmere 1 000 MW | 15.06.2026 | Reservert, alt nytt forbruk | Helgeland (NO4 sør for Svartisen) | Statnett til NVE | «nærmere 1000 MW nytt forbruk på Helgeland» |

**Dok 15:2086 summert per budområde (mai 2025, datasentre).** Kommune → budområde er **vår antakelse**
(analyse/dok15_2086_per_budomraade.py; ti kommuner er markert som tvilsomme). Avskriften stemmer med
kildens totaler (2 362,2 / 4 209,6 MW).

| Antatt budområde | Reservert MW | Kø MW |
|---|---|---|
| NO1 | 297,7 | 1 333,3 |
| NO2 | 1 163,0 | 998,0 |
| NO3 | 225,0 | 198,8 |
| NO4 | 241,5 | 1 210,7 |
| NO5 | 435,0 | 468,8 |

### 3c Hvorfor 3 500 MW (NVE, mars 2026) og ~12 GW (Rødt, okt. 2026) er forskjellige

Forskjellen skyldes **definisjonene**, ikke en motsigelse:
1. NVEs 3 500 MW er **bare reservert** kapasitet til datasentre (Tilknytningsregisteret, mars 2026).
2. Rødts ~12 GW er «reservert **eller** køsatt». NVE R37 gir de to delene hver for seg: ~4 GW reservert
   (aug. 2026) og ~9 GW i kø fordelt på 120 saker (mai 2026). Til sammen blir det ~13 GW. Rødts «rundt 120
   prosjekter» passer med NVEs 120 **køsaker**, ikke med alle prosjektene; det er sannsynlig, men ikke
   bekreftet, at forslaget har brukt dette tallet for hele mengden.
3. Tidspunktene er forskjellige (mars → okt.), og reservert kapasitet økte fra 3 500 til ~4 000 MW.
4. Statnetts statistikk 02.11.2026 gir 4 190 MW reservert + 10 109 MW kø = 14 299 MW for datasentre. Det
   ligger nær Rødts størrelsesorden, men summen kan telle samme MW to ganger (særlige vilkår, se over).
Rødt oppgir ikke kilden for 12 GW. Avviket er altså forklart av definisjonene; det eksakte uttrekket bak Rødts
tall kan ikke etterprøves.

## 4 Konklusjon

**GO.**

| Kriterium | Holder? | Grunnlag |
|---|---|---|
| (a) intet eksisterende åpent, reproduserbart arbeid i ettertid, time for time per budområde, koblet til kø-tall | Ja | Del 1. Nærmeste er De Facto 4:2025 (i ettertid, per prisområde, ikke time, ikke åpent); alle timesoppløste verk er modeller av framtiden med lukkede data. |
| (b) ≥ 99 % timer til stede for A75, A65, A11, alle NO-soner, 2023–2025 | Ja | Del 2: 100 % i alle 120 rader. |
| (c) offentlige reservasjonstall med definisjon for minst NO4 og hele Norge | Ja | Del 3a: Statnett per prisområde, datasentre og alt forbruk, med Statnetts egne definisjoner. |

Forbehold som gjelder før en preregistrering:
1. (a) hviler på 19 søk. CIGRE C1-11880 ble ikke funnet, og LA25 og arXiv:2604.26634 er ikke lest i fulltekst.
2. (c) hviler på en Power BI-visning: øyeblikksbilde uten historikk og uten versjonert nedlasting. Tallene for
   NO4 per dato bakover (2023–2025) finnes bare spredt (Dok 15:2086 mai 2025 per kommune, med vår
   kommune→sone-antakelse; NVE R17 fig. 30 bare grafisk). Kø-tallene kan telle samme MW to ganger
   (særlige vilkår).
3. (b) gjelder dekning. A03-håndteringen i disk-CSV-ene er ikke dokumentert.
4. Ett avvik fra forbudet i hovedøkten (A1 i STATE: fire rader A75-verdier for NO1 sett ved formatsjekk). Ingen
   balansestørrelse er beregnet eller sett.

Et smalere design er ikke nødvendig ut fra kriteriene. Ingen anbefaling om hva funnet blir.
