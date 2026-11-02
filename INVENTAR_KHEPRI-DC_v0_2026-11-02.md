# INVENTAR KHEPRI-DC v0 (2026-11-02): datainventar ENTSO-E NO1–NO5, 2023–2025 (UTC)

Kun telling av timer. Ingen verdier er lest ut, skrevet ut eller regnet på (ingen produksjon–last, netto, import/eksport, summer, gjennomsnitt). Verdikolonner er kun brukt som maske «har verdi / mangler verdi».

Definisjoner: forventet = timer i kalenderåret UTC (2023: 8760, 2024: 8784, 2025: 8760). **Til stede** = timen er dekket (60 min: ett punkt; 15 min: alle fire kvarter). **Delvis** = 1–3 av 4 kvarter. **Manglende** = forventet − til stede, for de månedene som faktisk er hentet/lest. **Ikke hentet** = timer i måneder som ikke ble forsøkt hentet (status «ikke hentet», ikke «manglende»); de er ikke med i «manglende». % til stede = til stede / forventet for hele året (for delvis hentede serier står % av hentet del i seksjon «Ikke hentet»). A75 «til stede» = minst én produksjonstype har full time; «alle typer» står i egen tabell.

## Tabell: serie × sone/grense × år

| Serie | Sone/grense (retning) | År | Oppløsning(er) funnet | Forventet | Til stede | Delvis | Manglende | Ikke hentet | % til stede | Kilde | A03 |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| A75 | NO1 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO1_generation_2023.csv | A03-håndtering ukjent (disk) |
| A75 | NO1 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO1_generation_2024.csv | A03-håndtering ukjent (disk) |
| A75 | NO1 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO1_generation_2025.csv | A03-håndtering ukjent (disk) |
| A75 | NO2 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO2_generation_2023.csv | A03-håndtering ukjent (disk) |
| A75 | NO2 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO2_generation_2024.csv | A03-håndtering ukjent (disk) |
| A75 | NO2 | 2025 | 15 min/60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO2_generation_2025.csv | A03-håndtering ukjent (disk) |
| A75 | NO3 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO3_generation_2023.csv | A03-håndtering ukjent (disk) |
| A75 | NO3 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO3_generation_2024.csv | A03-håndtering ukjent (disk) |
| A75 | NO3 | 2025 | 15 min/60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO3_generation_2025.csv | A03-håndtering ukjent (disk) |
| A75 | NO4 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO4_generation_2023.csv | A03-håndtering ukjent (disk) |
| A75 | NO4 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO4_generation_2024.csv | A03-håndtering ukjent (disk) |
| A75 | NO4 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO4_generation_2025.csv | A03-håndtering ukjent (disk) |
| A75 | NO5 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO5_generation_2023.csv | A03-håndtering ukjent (disk) |
| A75 | NO5 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO5_generation_2024.csv | A03-håndtering ukjent (disk) |
| A75 | NO5 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:~/khepri-data/raw/entsoe-rest/NO5_generation_2025.csv | A03-håndtering ukjent (disk) |
| A65 | NO1 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A65/ | ekspandert; hold-t(min.1 slot)=0, kun-hold=0; curve=A03 |
| A65 | NO1 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A65/ | ekspandert; hold-t(min.1 slot)=0, kun-hold=0; curve=A03 |
| A65 | NO1 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A65/A65_NO_1_2025-MM.csv | A03-håndtering ukjent (disk) |
| A65 | NO2 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A65/ | ekspandert; hold-t(min.1 slot)=0, kun-hold=0; curve=A03 |
| A65 | NO2 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A65/ | ekspandert; hold-t(min.1 slot)=0, kun-hold=0; curve=A03 |
| A65 | NO2 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A65/A65_NO_2_2025-MM.csv | A03-håndtering ukjent (disk) |
| A65 | NO3 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A65/ | ekspandert; hold-t(min.1 slot)=1, kun-hold=1; curve=A03 |
| A65 | NO3 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A65/ | ekspandert; hold-t(min.1 slot)=0, kun-hold=0; curve=A03 |
| A65 | NO3 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A65/A65_NO_3_2025-MM.csv | A03-håndtering ukjent (disk) |
| A65 | NO4 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A65/ | ekspandert; hold-t(min.1 slot)=0, kun-hold=0; curve=A03 |
| A65 | NO4 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A65/ | ekspandert; hold-t(min.1 slot)=0, kun-hold=0; curve=A03 |
| A65 | NO4 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A65/A65_NO_4_2025-MM.csv | A03-håndtering ukjent (disk) |
| A65 | NO5 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A65/ | ekspandert; hold-t(min.1 slot)=0, kun-hold=0; curve=A03 |
| A65 | NO5 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A65/ | ekspandert; hold-t(min.1 slot)=0, kun-hold=0; curve=A03 |
| A65 | NO5 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A65/A65_NO_5_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO1->NO2 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=3298, kun-hold=3298; curve=A03 |
| A11 | NO1->NO2 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=2907, kun-hold=2700; curve=A03 |
| A11 | NO1->NO2 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_1__NO_2_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO2->NO1 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=5044, kun-hold=5044; curve=A03 |
| A11 | NO2->NO1 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=5833, kun-hold=5592; curve=A03 |
| A11 | NO2->NO1 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_2__NO_1_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO1->NO3 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=7177, kun-hold=7177; curve=A03 |
| A11 | NO1->NO3 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=6688, kun-hold=6217; curve=A03 |
| A11 | NO1->NO3 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_1__NO_3_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO3->NO1 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=1221, kun-hold=1221; curve=A03 |
| A11 | NO3->NO1 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=2591, kun-hold=2111; curve=A03 |
| A11 | NO3->NO1 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_3__NO_1_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO1->NO5 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=7790, kun-hold=7790; curve=A03 |
| A11 | NO1->NO5 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=8312, kun-hold=8158; curve=A03 |
| A11 | NO1->NO5 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_1__NO_5_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO5->NO1 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=677, kun-hold=677; curve=A03 |
| A11 | NO5->NO1 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=513, kun-hold=357; curve=A03 |
| A11 | NO5->NO1 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_5__NO_1_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO1->SE3 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=4738, kun-hold=4738; curve=A03 |
| A11 | NO1->SE3 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=5732, kun-hold=5732; curve=A03 |
| A11 | NO1->SE3 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_1__SE_3_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | SE3->NO1 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=3237, kun-hold=3237; curve=A03 |
| A11 | SE3->NO1 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=1986, kun-hold=1986; curve=A03 |
| A11 | SE3->NO1 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_SE_3__NO_1_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO2->NO5 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=7316, kun-hold=7316; curve=A03 |
| A11 | NO2->NO5 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=7680, kun-hold=7536; curve=A03 |
| A11 | NO2->NO5 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_2__NO_5_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO5->NO2 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=1367, kun-hold=1367; curve=A03 |
| A11 | NO5->NO2 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=1078, kun-hold=938; curve=A03 |
| A11 | NO5->NO2 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_5__NO_2_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO2->DK1 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=2483, kun-hold=2483; curve=A03 |
| A11 | NO2->DK1 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=1557, kun-hold=1557; curve=A03 |
| A11 | NO2->DK1 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_2__DK_1_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | DK1->NO2 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=5217, kun-hold=5217; curve=A03 |
| A11 | DK1->NO2 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=6405, kun-hold=6405; curve=A03 |
| A11 | DK1->NO2 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_DK_1__NO_2_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO2->DELU | 2023 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=5595, kun-hold=1794; curve=A03 |
| A11 | NO2->DELU | 2024 | 15 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=5390, kun-hold=1477; curve=A03 |
| A11 | NO2->DELU | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_2__DE_LU_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | DELU->NO2 | 2023 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=6980, kun-hold=6487; curve=A03 |
| A11 | DELU->NO2 | 2024 | 15 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=7380, kun-hold=6999; curve=A03 |
| A11 | DELU->NO2 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_DE_LU__NO_2_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO2->NL | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=2462, kun-hold=2462; curve=A03 |
| A11 | NO2->NL | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=5095, kun-hold=1966; curve=A03 |
| A11 | NO2->NL | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_2__NL_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NL->NO2 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=7156, kun-hold=7156; curve=A03 |
| A11 | NL->NO2 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=8121, kun-hold=7212; curve=A03 |
| A11 | NL->NO2 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NL__NO_2_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO2->GB | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=5651, kun-hold=5651; curve=A03 |
| A11 | NO2->GB | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=2182, kun-hold=1704; curve=A03 |
| A11 | NO2->GB | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_2__GB_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | GB->NO2 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=7896, kun-hold=7896; curve=A03 |
| A11 | GB->NO2 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=8273, kun-hold=8173; curve=A03 |
| A11 | GB->NO2 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_GB__NO_2_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO3->NO4 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=7940, kun-hold=7940; curve=A03 |
| A11 | NO3->NO4 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=8302, kun-hold=8074; curve=A03 |
| A11 | NO3->NO4 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_3__NO_4_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO4->NO3 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=641, kun-hold=641; curve=A03 |
| A11 | NO4->NO3 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=611, kun-hold=378; curve=A03 |
| A11 | NO4->NO3 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_4__NO_3_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO3->NO5 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=2627, kun-hold=2627; curve=A03 |
| A11 | NO3->NO5 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=3323, kun-hold=3067; curve=A03 |
| A11 | NO3->NO5 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_3__NO_5_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO5->NO3 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=5723, kun-hold=5723; curve=A03 |
| A11 | NO5->NO3 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=5488, kun-hold=5164; curve=A03 |
| A11 | NO5->NO3 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_5__NO_3_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO3->SE2 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=4804, kun-hold=4804; curve=A03 |
| A11 | NO3->SE2 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=6493, kun-hold=6493; curve=A03 |
| A11 | NO3->SE2 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_3__SE_2_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | SE2->NO3 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=3405, kun-hold=3405; curve=A03 |
| A11 | SE2->NO3 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=1722, kun-hold=1722; curve=A03 |
| A11 | SE2->NO3 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_SE_2__NO_3_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO4->SE1 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=2461, kun-hold=2461; curve=A03 |
| A11 | NO4->SE1 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=4678, kun-hold=4678; curve=A03 |
| A11 | NO4->SE1 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_4__SE_1_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | SE1->NO4 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=5876, kun-hold=5876; curve=A03 |
| A11 | SE1->NO4 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=3352, kun-hold=3352; curve=A03 |
| A11 | SE1->NO4 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_SE_1__NO_4_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO4->SE2 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=2451, kun-hold=2451; curve=A03 |
| A11 | NO4->SE2 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=4973, kun-hold=4973; curve=A03 |
| A11 | NO4->SE2 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_4__SE_2_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | SE2->NO4 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=6024, kun-hold=6024; curve=A03 |
| A11 | SE2->NO4 | 2024 | 60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=3208, kun-hold=3208; curve=A03 |
| A11 | SE2->NO4 | 2025 | 60+15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_SE_2__NO_4_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | NO4->FI | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=1170, kun-hold=1170; curve=A03 |
| A11 | NO4->FI | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=3679, kun-hold=3161; curve=A03 |
| A11 | NO4->FI | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_NO_4__FI_2025-MM.csv | A03-håndtering ukjent (disk) |
| A11 | FI->NO4 | 2023 | 60 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=7889, kun-hold=7889; curve=A03 |
| A11 | FI->NO4 | 2024 | 15+60 min | 8784 | 8784 | 0 | 0 | 0 | 100.00 | hentet:$V/raw/A11/ | ekspandert; hold-t(min.1 slot)=6976, kun-hold=5564; curve=A03 |
| A11 | FI->NO4 | 2025 | 15 min | 8760 | 8760 | 0 | 0 | 0 | 100.00 | disk:/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/A11_FI__NO_4_2025-MM.csv | A03-håndtering ukjent (disk) |

## A75: timer der alle typer som finnes i året har full verdi

«Typer i året» = kolonner med minst én verdi i året i CSV-en. Antallet er altså betinget av hvilke typer ENTSO-E rapporterte det året, ikke av en fast typeliste.

| Sone | År | Typer i året (n) | Timer med alle typer | Forventet | Typer med færre enn forventet hele timer (full/delvis) |
|---|---|---:|---:|---:|---|
| NO1 | 2023 | 6 | 8760 | 8760 | – |
| NO1 | 2024 | 7 | 5738 | 8784 | Solar: 5738/0 |
| NO1 | 2025 | 7 | 8760 | 8760 | – |
| NO2 | 2023 | 6 | 8760 | 8760 | – |
| NO2 | 2024 | 6 | 8784 | 8784 | – |
| NO2 | 2025 | 7 | 2183 | 8760 | Hydro Pumped Storage: 7869/61, Wind Offshore: 3074/0 |
| NO3 | 2023 | 8 | 5618 | 8760 | Biomass: 5618/0 |
| NO3 | 2024 | 8 | 8784 | 8784 | – |
| NO3 | 2025 | 9 | 1880 | 8760 | Hydro Pumped Storage: 8310/39, Solar: 2330/0 |
| NO4 | 2023 | 5 | 8760 | 8760 | – |
| NO4 | 2024 | 5 | 8784 | 8784 | – |
| NO4 | 2025 | 5 | 8760 | 8760 | – |
| NO5 | 2023 | 5 | 8760 | 8760 | – |
| NO5 | 2024 | 5 | 8784 | 8784 | – |
| NO5 | 2025 | 5 | 8281 | 8760 | Hydro Pumped Storage: 8281/58 |

Typer per sone og år: NO1 2023: Biomass, Fossil Gas, Hydro Run-of-river and poundage, Hydro Water Reservoir, Waste, Wind Onshore; NO1 2024: Biomass, Fossil Gas, Hydro Run-of-river and poundage, Hydro Water Reservoir, Solar, Waste, Wind Onshore; NO1 2025: Biomass, Fossil Gas, Hydro Run-of-river and poundage, Hydro Water Reservoir, Solar, Waste, Wind Onshore; NO2 2023: Fossil Gas, Hydro Pumped Storage, Hydro Run-of-river and poundage, Hydro Water Reservoir, Waste, Wind Onshore; NO2 2024: Fossil Gas, Hydro Pumped Storage, Hydro Run-of-river and poundage, Hydro Water Reservoir, Waste, Wind Onshore; NO2 2025: Fossil Gas, Hydro Pumped Storage, Hydro Run-of-river and poundage, Hydro Water Reservoir, Waste, Wind Offshore, Wind Onshore; NO3 2023: Biomass, Hydro Pumped Storage, Hydro Run-of-river and poundage, Hydro Water Reservoir, Other, Other renewable, Waste, Wind Onshore; NO3 2024: Biomass, Hydro Pumped Storage, Hydro Run-of-river and poundage, Hydro Water Reservoir, Other, Other renewable, Waste, Wind Onshore; NO3 2025: Biomass, Hydro Pumped Storage, Hydro Run-of-river and poundage, Hydro Water Reservoir, Other, Other renewable, Solar, Waste, Wind Onshore; NO4 2023: Fossil Gas, Hydro Run-of-river and poundage, Hydro Water Reservoir, Other renewable, Wind Onshore; NO4 2024: Fossil Gas, Hydro Run-of-river and poundage, Hydro Water Reservoir, Other renewable, Wind Onshore; NO4 2025: Fossil Gas, Hydro Run-of-river and poundage, Hydro Water Reservoir, Other renewable, Wind Onshore; NO5 2023: Fossil Gas, Hydro Pumped Storage, Hydro Run-of-river and poundage, Hydro Water Reservoir, Waste; NO5 2024: Fossil Gas, Hydro Pumped Storage, Hydro Run-of-river and poundage, Hydro Water Reservoir, Waste; NO5 2025: Fossil Gas, Hydro Pumped Storage, Hydro Run-of-river and poundage, Hydro Water Reservoir, Waste

## Serier under 99 % til stede

Ingen.

## Hentet fra ENTSO-E vs lest fra disk

- **Lest fra disk (ikke hentet på nytt):** A75 NO1–NO5 2023, 2024, 2025 (15 CSV, `~/khepri-data/raw/entsoe-rest/`; byte-identiske med kopiene i `/Volumes/Vault/khepri-tsfm/prosp/current_raw/` og `…/data/raw/merged/`, sha256 sammenlignet); A65 NO1–NO5 2025 (60 månedsfiler, `/Volumes/Vault/khepri-data/flowtracing/raw/2025/A65/`; kryssjekket mot `~/khepri-data/v2-dk-fi/NO{1..5}_load_2025.csv`: identisk timemaske); A11 2025, alle 30 retninger (360 månedsfiler, `/Volumes/Vault/khepri-data/flowtracing/raw/2025/A11/`, manifest `MANIFEST.tsv`).
- **Hentet nå:** A65 NO1–NO5 2023+2024 og A11 alle 30 retninger 2023+2024 (rå XML under `/Volumes/Vault/khepri-dc/raw/A65/` og `/Volumes/Vault/khepri-dc/raw/A11/`, manifest `/Volumes/Vault/khepri-dc/raw/MANIFEST_HENTET.tsv`). Fase 1: 317 månedskall (P1M) til eier trakk tilbake 60-minuttersgrensen; fase 2: 44 årskall (P1Y, UTC-årsgrenser) for resten. Ingen_data (reason 999) i de 361 dokumentene: 0; feil: 0. Alle HTTP 200; ingen 429.
- **Ikke hentet:** ingenting. Alle 120 serie×år-rader er dekket (de to NO4–RU-probene ga reason 999, se under).

## Maks tidsintervall per forespørsel (A65 6.1.A, A11 12.1.G)

- **Primærkilden kunne ikke leses.** ENTSO-E Transparency Platform RESTful API user guide (`transparencyplatform.zendesk.com/hc/en-us/articles/15692855254548` → HTTP 403; `transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html` → HTTP 400; også WebFetch fikk 403/400). Jeg har ikke forsøkt å omgå dette. Jeg har derfor *ikke* et ordrett sitat fra selve guiden.
- **Sekundærkilde som gjengir guidens feltbeskrivelser** (R-pakken `entsoeapi` 1.3.1, referansesider): Actual total load, `https://krose.github.io/entsoeapi/reference/load_actual_total.html`: «One year range limit applies». Cross-border physical flows, `https://krose.github.io/entsoeapi/reference/cross_border_physical_flows.html`: «Minimum time interval in query response is an MTU period, but 1 year range limit applies.» (Sitatene er hentet via WebFetch-sammendrag, ikke råtekst, jf. at slike sammendrag ikke er ordrette; behandle dem som sekundære.)
- **entsoe-py 0.8.1** markerer både `query_load` og `query_crossborder_flows` med `@month_limited` (`entsoe/entsoe.py`, linje ca. 1468 og 1701), dvs. biblioteket deler i måneder. Det er et bibliotekvalg, ikke en kilde til grensen.
- **Hentekoden i khepri-consumption-2025:** repoet har ingen hentekode og ingen rå A11/A65 (kun avledede timeserier og validering; `build.py` leser fra `~/khepri-data/flowtracing` via `kryssjekk_tracing.bygg_input`). Rådataene bak det er de samme `flowtracing/raw/2025`-filene som er brukt her; de ble hentet av `~/khepri-data/flowtracing/fetch_region_2025.py` med entsoe-py, én måned per kall.
- **Empirisk:** 44 P1Y-kall (UTC-årsgrenser, `periodStart=YYYY01010000`, `periodEnd=(YYYY+1)01010000`) ga alle HTTP 200 og fullt dekkende dokumenter (timetellingene i tabellen); for den ene serie-årskombinasjonen med både måneds- og årsfiler (A11 NO2→NO5 2023) var timemasken identisk i overlappet (`kryss_aar_vs_maaned.py`). Konklusjon: P1Y ble brukt for resten; grensen «ett år» er støttet av sekundærkilden og av at alle kallene lyktes, men ikke bekreftet ordrett mot guiden.

## Usikkerheter og valg

1. **A03-håndtering i disk-CSV-ene er ukjent.** Filene er allerede parset av entsoe-py. entsoe-py 0.8.x forward-fyller manglende posisjoner innen hver Period (`series_parsers.py`, `_parse_timeseries_generic`, kommentar «with A03 its possible that positions are missing»), men CSV-en skiller ikke eksplisitte punkter fra fyllte; hvilken entsoe-py-versjon som parset A75-filene (2019–2026) er ikke loggført. Indirekte støtte for ekspansjon: A11 2025 på disk er 100 % dekket, mens de rå XML-ene for 2023/2024 viser at et stort antall timer bare er dekket av hold-forrige (kolonnen A03 i tabellen), så en parser uten ekspansjon ville gitt store hull. Dette er en slutning, ikke en verifikasjon. Antall hold-forrige-timer kan derfor ikke oppgis for disk-seriene.
2. **Hold-forrige-timer (hentede serier, kun tellinger):** «hold-t(min.1 slot)» = timer der minst én slot kommer fra hold-forrige; «kun-hold» = timer der alle tilstedeværende slots er hold-forrige (ingen eksplisitt punkt i timen). For A65 er tallene 0–1 (A03 brukes, men praktisk talt alle posisjoner er eksplisitte). For A11 er tallene store: flyt rapporteres bare ved endring.
3. **Definisjon av «til stede» i blandet oppløsning (disk):** CSV bærer ikke oppløsning. Per kolonne regnes alt før første time med et tidsstempel med minutt ≠ 0 som 60 min (1 punkt = full time), derfra som 15 min (4 kvarter = full, 1–3 = delvis). Antakelsen kan gi «delvis» for timer rett etter et bytte hvis kvarter mangler; det ga ingen utslag her (delvis = 0 i alle disk-rader utenom enkelte A75-typer, se tabell for A75-typer). XML-seriene bruker Periodens oppløsning direkte. Dublette tidsstempler: 0 i alle brukte filer.
4. **A75 «til stede»:** minst én produksjonstype har full time. «Alle typer» bruker kolonnene som har minst én verdi i året i CSV-en; typemengden varierer mellom år (f.eks. Solar fra midt i 2024 i NO1), så «alle typer» er en strengere og typeavhengig størrelse. Forbruk av pumpekraft (A75 consumption) er ikke med i CSV-ene.
5. **A75 2025 oppløsning:** blandet 60/15 min per type; bytte til 15 min fra 2025-04-10 00:00 UTC for de fleste typer (andre datoer for enkelte typer, se `tellinger_disk.json`). A65 2025 byttet i mars; A11 2025 er 15 min hele året for de fleste grenser, 60+15 for grensene mot SE3, SE1, SE2 og DK1.
6. **A65 forespørsel:** parametrene er de samme som entsoe-py (`documentType=A65`, `processType=A16`, `outBiddingZone_Domain` og `out_Domain` = sonens EIC). **A11:** `out_Domain` = fra, `in_Domain` = til, samme semantikk som entsoe-py `query_crossborder_flows(fra, til)`.
7. **Grenseliste:** 15 grenser × 2 retninger = 30 serier per år, identisk med `entsoe.mappings.NEIGHBOURS` (entsoe-py 0.8.1) for NO_1–NO_5 (verifisert programmatisk, ingen avvik). NO4–RU finnes ikke i NEIGHBOURS. To prober (januar 2024, begge retninger, EIC fra `Area['RU']`) ga Acknowledgement med reason 999 (ingen data): NO4–RU publiseres ikke og er ikke med i tabellen. EIC: NO1 10YNO-1--------2, NO2 10YNO-2--------T, NO3 10YNO-3--------J, NO4 10YNO-4--------9, NO5 10Y1001A1001A48H; nabo-EIC fra entsoe-py (SE_1 10Y1001A1001A44P, SE_2 …45N, SE_3 …46L, DK_1 10YDK-1--------W, NL 10YNL----------L, DE_LU 10Y1001A1001A82H, GB 10YGB----------A, FI 10YFI-1--------U).
8. **Idriftsettelse:** forventede timer er satt til hele året for alle kabler (NordLink 2020/21, North Sea Link 2021 er i drift hele perioden 2023–2025), så ingen kabelspesifikk idriftsettelse påvirker tellingen.
9. **Tidssone:** alle tidsstempler konvertert til UTC; forventet = 8760 / 8784 / 8760. Periodegrenser for hentede data er UTC (`yyyyMMddHHmm`). Tidsstempler utenfor kalenderåret ble ikke funnet i A75-filene (utenfor_aar = 0).
10. **Token:** kun lest inne i Python; lengde sjekket, verdi aldri skrevet ut, URL-er aldri logget (unntakstekst saneres).

## Avvik fra forbudet

Ingen verdier er sett, skrevet ut eller regnet på i denne kjøringen. Kun overskriftsrader (kolonnenavn) og tidsstempel-ytterpunkter er skrevet ut. Merk: `STATE_KHEPRI-DC_v0_2026-11-02.md` (hovedøkten) dokumenterer et tidligere avvik A1 (head -5 av NO1_generation_2025.csv); det er ikke mitt.

## Filer

`/Volumes/Vault/khepri-dc/inventar/`: `hent_entsoe.py` (fase 1, P1M), `hent_entsoe_p1y.py` (fase 2, P1Y), `tellelib.py`, `test_tellelib.py` (syntetisk), `tell_disk.py`, `tell_hentet.py`, `kryss_aar_vs_maaned.py`, `lag_inventar.py`, `tellinger_disk.json`, `tellinger_hentet.json`, `hent_entsoe.log`; manifest `/Volumes/Vault/khepri-dc/raw/MANIFEST_HENTET.tsv`.
