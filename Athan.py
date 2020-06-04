import requests
import json
from datetime import datetime

def fetchTimes():
	response = requests.get("http://api.aladhan.com/v1/timingsByCity?city=gothenburg&country=sweden&method=2")

	jsonData = response.json()['data']['timings']
	fajr = jsonData['Fajr']
	duhar = jsonData['Dhuhr']
	asar = jsonData['Asr']
	maghrib = jsonData['Maghrib']
	isha = jsonData['Isha']
	dailyTimings.append(fajr)
	dailyTimings.append(duhar)
	dailyTimings.append(asar)
	dailyTimings.append(maghrib)
	dailyTimings.append(isha)
	print(dailyTimings)

dailyTimings = []

fetchTimes()

while (1<2): 
	now = datetime.now() # current date and time
	current_time = now.strftime("%H:%M")

	if ('00:01' == current_time):
		fetchTimes()
	if (current_time in dailyTimings): 
		print("turn on the TV and play azan")

