import requests
import json

locations = {
    "66534": {"name": "Sabetha", "lat": 39.93, "lon": -95.80},
    "50501": {"name": "Fort Dodge", "lat": 42.50, "lon": -94.18},
    "37347": {"name": "South Pittsburg", "lat": 35.01, "lon": -85.71},
    "66092": {"name": "Paola", "lat": 38.58, "lon": -94.88}
}

forecast = {}

for zip_code, info in locations.items():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={info['lat']}&longitude={info['lon']}&daily=temperature_2m_max&timezone=auto"
    res = requests.get(url)
    data = res.json()
    days = data['daily']['time']
    temps = data['daily']['temperature_2m_max']
    forecast[zip_code] = {
        "name": info["name"],
        "daily": [
            {"day": d[:10], "high": round(t)}
            for d, t in zip(days, temps)
        ]
    }

with open("forecast.json", "w") as f:
    json.dump(forecast, f, indent=2)

print("Updated forecast.json")
