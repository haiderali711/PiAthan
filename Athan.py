import requests
import json
from datetime import datetime


response = requests.get("http://api.aladhan.com/v1/timingsByCity?city=gothenburg&country=sweden&method=2")

jsonData = response.json()['data']['timings']
fajr = jsonData['Fajr']
duhar = jsonData['Dhuhr']
asar = jsonData['Asr']
maghrib = jsonData['Maghrib']
isha = jsonData['Isha']

dailyTimings = [fajr,duhar,asar,maghrib,isha]

# Print the status code of the response.
#print(response.status_code)
print(dailyTimings)

for time in dailyTimings:
	print(time)



while true: 
	now = datetime.now() # current date and time
	current_time = now.strftime("%H:%M")

	if (current_time in dailyTimings): 
		print("turn on the TV and play azan")  

