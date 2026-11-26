"""Find the cheapest block of consecutive hours today and tomorrow.

Usage: python3 cheapest_hours.py [hours]   (default: 3)
Only uses the Python standard library.

Data: Bundesnetzagentur | SMARD.de, aufbereitet von tageswatt.de (CC BY 4.0)
"""
import json
import sys
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

URL = "https://tageswatt.de/api/daten/aktuell.json"
BERLIN = ZoneInfo("Europe/Berlin")


def load():
    req = urllib.request.Request(URL, headers={"User-Agent": "tageswatt-api-example"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def parse(ts):
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def main():
    hours = float(sys.argv[1]) if len(sys.argv) > 1 else 3
    data = load()
    now = datetime.now(BERLIN)
    slots = [w for w in data["werte"] if parse(w["ende"]) > now]
    if not slots:
        sys.exit("No prices available.")
    minutes = (parse(slots[0]["ende"]) - parse(slots[0]["start"])).seconds // 60
    n = max(1, round(hours * 60 / minutes))
    if len(slots) < n:
        sys.exit(f"Only {len(slots)} slots left, need {n}.")

    best = min(range(len(slots) - n + 1), key=lambda i: sum(w["ct_kwh"] for w in slots[i:i + n]))
    block = slots[best:best + n]
    avg = sum(w["ct_kwh"] for w in block) / n
    start = parse(block[0]["start"]).astimezone(BERLIN)
    end = parse(block[-1]["ende"]).astimezone(BERLIN)

    if data["jetzt"]:
        print(f"Now:      {data['jetzt']['ct_kwh']:.2f} ct/kWh")
    print(f"Cheapest {hours:g} h: {start:%a %d.%m. %H:%M} to {end:%H:%M}, average {avg:.2f} ct/kWh")
    if not data["morgen"]["verfuegbar"]:
        print("Tomorrow's prices are published around 13:00.")


if __name__ == "__main__":
    main()
