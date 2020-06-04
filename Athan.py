import requests
import json

response = requests.get("http://api.aladhan.com/v1/timingsByCity?city=gothenburg&country=sweden&method=2")


jsonData = response.json()

# Print the status code of the response.
#print(response.status_code)
print(jsonData)