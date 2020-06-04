import requests
import json

response = requests.get("http://api.aladhan.com/v1/timingsByCity?city=gothenburg&country=sweden&method=2")


jsonData = response.json()['data']['timings']
fajr = jsonData['Fajr']
duhar = jsonData['Dhuhr']
asar = jsonData['Asr']
maghrib = jsonData['Maghrib']
isha = jsonData['Isha']

# Print the status code of the response.
#print(response.status_code)
print(jsonData)
print(fajr)
print(duhar)
print(asar)
print(maghrib)
print(isha)
