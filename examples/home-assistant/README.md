# Home Assistant

## 1. Sensor

Add [`configuration.yaml`](configuration.yaml) to your own `configuration.yaml` and restart Home Assistant. You get two sensors:

- `sensor.borsenstrompreis`: price of the current quarter hour in ct/kWh, with the attributes `heute`, `morgen` and `werte` (all quarter hours until tomorrow 24:00)
- `sensor.borsenstrompreis_tiefstwert_morgen`: lowest price tomorrow, `unknown` until about 13:00
- `sensor.strompreis_brutto` (optional): estimated end-customer price with grid fee, levies and taxes. Put your own `netzentgelt` and `aufschlag` into the URL, or delete the block if you only want exchange prices.

The data refreshes every 5 minutes. With both blocks that is 4 requests per 10 minutes, well below the limit of 60.

## 2. Chart

With [ApexCharts Card](https://github.com/RomRider/apexcharts-card) (HACS) you can show today and tomorrow as a bar chart: add a manual card with [`apexcharts-card.yaml`](apexcharts-card.yaml).

## Auf Deutsch

Den Inhalt von `configuration.yaml` in deine eigene `configuration.yaml` einfügen und Home Assistant neu starten. Der erste Sensor zeigt den Börsenpreis der laufenden Viertelstunde, die Viertelstunden bis morgen 24 Uhr stehen im Attribut `werte`. Der Sensor „Strompreis brutto“ zeigt den geschätzten Endkundenpreis. Trag in der Adresse dein eigenes Netzentgelt und den Aufschlag deines Tarifs ein, oder lösch den Block, wenn dir der Börsenpreis reicht. Für das Diagramm brauchst du die ApexCharts Card aus HACS.

Die ersten beiden Sensoren zeigen Börsenpreise netto, ohne Netzentgelt, Umlagen und Steuern.
