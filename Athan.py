import requests
import json
from datetime import datetime

now = datetime.now() # current date and time
current_time = now.strftime("%H:%M")


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

print(current_time)

