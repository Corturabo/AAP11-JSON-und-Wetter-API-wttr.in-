import requests

url = f"https://wttr.in/INNSBRUCK?format=j1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temperatur = data["current_condition"][0]["temp_C"]
    print(f"Aktuelle Temperatur in Innsbruck: {temperatur}°C")

        