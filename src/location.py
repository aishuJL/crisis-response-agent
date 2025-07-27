import requests

def get_location():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        return {
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country")
        }
    except Exception:
        return {
            "city": None,
            "region": None,
            "country": None
        }
