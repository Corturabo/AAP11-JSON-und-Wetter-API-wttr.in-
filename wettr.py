import urllib.request
import json

url = "https://wttr.in/INNSBRUCK?format=j1"  
response = urllib.request.urlopen(url)
json_ = response.read().decode()

print(json_)
data = json.loads(json_)

temperatur = data['current_condition'][0]['temp_C']
print(f"\nTemperatur in Celsius: {temperatur}°C")
