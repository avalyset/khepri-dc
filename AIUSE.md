# KI-bruk (AIUSE)

KI er brukt som verktøy under forfatterens styring, ikke som forfatter. Claude Code (Anthropic, modell Claude Opus
5.5) ble brukt 2. november 2026 til kildesøk og ordrett sitatkontroll, henting av ENTSO-E- og Elhub-data, skriving
og testing av kode (khepri_dc/, build/, tests/), kjøring av den preregistrerte analysen og utkast til tekst.
Datainventaret i røyktesten (A-DC0) ble gjort av en Claude Sonnet-underagent, og den uavhengige reproduksjonen
(A-DC1 steg 7) av en fersk Claude Opus-underagent som bare fikk Zenodo-tarballen.

Forfatteren har bestemt problemstilling, scenarier, tolkningsregler og kontrollgrense i oppdragsteksten, og har
ansvaret for innholdet. Alle tall i løpende tekst er sporet i truth/NUMBERS, alle sitater i truth/SOURCES.
Forbudet mot å beregne eller se balansestørrelser før tagg prereg-v1 og det ene registrerte avviket fra det
(A1, A-DC0) er dokumentert i truth/STATE.

KI-erklæring: implementert med Claude Code.
