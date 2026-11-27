# evcc

Add [`evcc.yaml`](evcc.yaml) to your `evcc.yaml`. evcc then plans charging by the exchange price for today and, from about 13:00, tomorrow.

The prices are net exchange prices without grid fees, levies and taxes. For picking the cheapest hours that is enough as long as your surcharges are the same all day. To let evcc plan with the full price, use `aktuell.json?preis=brutto&netzentgelt=...&aufschlag=...` as `uri` with your own values. If your tariff has time-variable grid fees (§ 14a module 3), add them yourself or use your supplier's own integration.

## Auf Deutsch

Den Block aus `evcc.yaml` in deine `evcc.yaml` übernehmen. evcc plant das Laden dann nach dem Börsenpreis. Aufschläge deines Tarifs sind nicht enthalten. Das reicht für die Wahl der günstigsten Stunden, solange die Aufschläge den ganzen Tag gleich sind. Soll evcc mit dem vollen Preis rechnen, nimm als `uri` die Adresse mit `?preis=brutto` und deinen eigenen Werten für `netzentgelt` und `aufschlag`.
