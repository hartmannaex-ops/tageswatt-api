# Python

[`cheapest_hours.py`](cheapest_hours.py) finds the cheapest block of consecutive hours in the remaining prices of today and tomorrow. No packages needed, Python 3.9 or newer.

```bash
python3 cheapest_hours.py 3
```

The script prints the current price and when the cheapest 3-hour block starts and ends.

Load a range as CSV, for example with pandas:

```python
import pandas as pd
df = pd.read_csv("https://tageswatt.de/api/daten/preise.csv?von=2026-11-01&bis=2026-11-30")
print(df.groupby("uhrzeit")["ct_kwh"].mean().sort_values().head())
```
