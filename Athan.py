import requests
import json
from datetime import datetime
import subprocess
import time
import pygame

#import shlex
#subprocess.call(shlex.split('./test.sh param1 param2'))


#Contains all the request relating information about the api and the populating of the times in the LIST
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
    
    #ReFetching the new times when the time is like 00:01
    if ('00:01' == current_time):
        dailyTimings=[]
        fetchTimes()
        time.sleep(50)

    #If any time in the daily timing matches the current time do the following things
    if ('22:12' in dailyTimings): 
#    if (current_time in dailyTimings): 
        print("turn on the TV and play azan")
        status = subprocess.run(['./status.sh'],capture_output=True)
        status = status.stdout
        status = status.decode('utf-8')
        print(type(status))
        print(status)
        subprocess.run(['./on.sh'])
        file = 'normal/1.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(1)
        time.sleep(180)
        if 'standby' in status:
            subprocess.run(['./off.sh'])
            time.sleep(10)
        

    print('just looping every 2 secs')
    time.sleep(2)

