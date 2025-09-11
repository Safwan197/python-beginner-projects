import requests
import json
while True:
    
    city = input("Enter City Name : ")
    if city == "quit":
        break
    url = f"https://api.weatherapi.com/v1/current.json?key=cee73a5f178d44609a3171349252608&q={city}"

    r = requests.get(url)
    # print(r.text)     # To get full information regarding city (incl dimesions , weather and more)

    wdic = json.loads(r.text)  # written only to get weather in degrees
    w = wdic["current"]["temp_c"]
    print(f"Weather of {city} is {w} degrees ")
