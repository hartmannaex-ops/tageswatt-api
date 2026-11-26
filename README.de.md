# Tageswatt API

Kostenlose Schnittstelle für die Börsenstrompreise in Deutschland (Day-Ahead, Gebotszone DE-LU) in Viertelstunden. Ohne Anmeldung, ohne Token, CORS offen. Daten seit 1. Oktober 2025, die Preise für morgen ab etwa 13 Uhr.

Website: [tageswatt.de/daten](https://tageswatt.de/daten/) · [English version](README.md)

| Adresse | Inhalt |
|---|---|
| [`/api/daten/aktuell.json`](https://tageswatt.de/api/daten/aktuell.json) | Preis jetzt, Kennzahlen für heute und morgen, alle Viertelstunden von heute 0 Uhr bis morgen 24 Uhr |
| [`/api/daten/preise.json?datum=2026-11-20`](https://tageswatt.de/api/daten/preise.json?datum=2026-11-20) | Ein Tag oder ein Zeitraum als JSON |
| [`/api/daten/preise.csv?von=2026-11-01&bis=2026-11-15`](https://tageswatt.de/api/daten/preise.csv?von=2026-11-01&bis=2026-11-15) | Ein Tag oder ein Zeitraum als CSV |

Basisadresse: `https://tageswatt.de`

## Fertige Konfigurationen

- [Home Assistant](examples/home-assistant/) (REST-Sensor und ApexCharts-Karte)
- [evcc](examples/evcc/) (dynamischer Netztarif)
- [Python](examples/python/) (günstigste Stunden des Tages)

## `/api/daten/aktuell.json`

Die feste Adresse für Smart Home. Ohne Datum in der URL.

| Feld | Bedeutung |
|---|---|
| `jetzt` | Laufende Viertelstunde, `null` wenn keine Daten da sind |
| `heute`, `morgen` | Mittel, Tiefst- und Höchstwert in ct/kWh, Minuten mit negativem Preis. Vor etwa 13 Uhr steht bei `morgen` nur `{"datum": "...", "verfuegbar": false}` |
| `werte` | Alle Viertelstunden, Zeiten in UTC, Preise in ct/kWh mit 2 Nachkommastellen |

Die Antwort wird bis zur nächsten Viertelstunde zwischengespeichert, `jetzt` stimmt also immer. Ein Beispiel der Antwort steht in der [englischen README](README.md#apidatenaktuelljson).

## `/api/daten/preise.json` und `/api/daten/preise.csv`

Parameter: `datum=JJJJ-MM-TT` für einen Tag, oder `von` und `bis` für einen Zeitraum. Ohne Parameter kommt der heutige Tag.

CSV-Spalten: `start_utc, datum, uhrzeit, minuten, eur_mwh, ct_kwh`. `datum` und `uhrzeit` sind deutsche Zeit.

## Grenzen

- Höchstens 31 Tage pro Abruf, vom 01.10.2025 bis morgen.
- 60 Abrufe in 10 Minuten je IP-Adresse, darüber kommt HTTP 429. `aktuell.json` alle 5 Minuten abzufragen ist kein Problem.
- Fehler kommen als `{"fehler": "..."}` mit HTTP 400 oder 429.

## Was der Preis ist

Das sind Börsenpreise, netto. Auf deinen Tarif kommen Netzentgelt, Umlagen, Steuern und die Marge des Anbieters. Für die Wahl der günstigsten Stunden reicht der Börsenpreis, solange deine Aufschläge den ganzen Tag gleich sind.

## Verfügbarkeit

Die Schnittstelle ist kostenlos und ohne Gewähr. Sie kann ausfallen oder verspätet Daten liefern. Änderungen am Format kündigen wir vorher auf [tageswatt.de/daten](https://tageswatt.de/daten/) an. Wenn ein Ausfall Kosten verursachen kann, plane einen Ersatz ein, etwa einen festen Ladezeitraum.

## Lizenz und Quelle

- **Daten:** Bundesnetzagentur | SMARD.de, bereitgestellt über Energy-Charts des Fraunhofer ISE, Lizenz [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de). Bitte nenne als Quelle: **Bundesnetzagentur | SMARD.de, aufbereitet von tageswatt.de**.
- **Code und Beispiele in diesem Repository:** [MIT](LICENSE).

Fragen oder größerer Datenbedarf: gern als Issue.
