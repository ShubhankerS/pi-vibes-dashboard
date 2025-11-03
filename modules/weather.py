import requests

def get_weather():
    try:
        response = requests.get("https://wttr.in/?format=3", timeout=5)
        return response.text.strip()
    except requests.RequestException:
        return "Weather unavailable 🌐"
