import requests
import json
from datetime import datetime, timedelta
last_hour = -1
now = datetime.now()
acceptable_price = []
tomorrows_price = []
year = now.strftime("%Y")

month = now.strftime("%m")

day = now.strftime("%d")

url = 'https://www.elprisetjustnu.se/api/v1/prices/{current_year}/{current_month}-{current_day}_SE3.json'.format(current_year = year, current_month = month, current_day=day)
price = requests.get(url)
json_price = json.loads(price.text)
#print(json_price)
for i in range(24):
    #print(item["SEK_per_kWh"])
    if json_price[i]["SEK_per_kWh"] < 0.7 :
        acceptable_price.append(i)
        print(acceptable_price)
while True:
    now = datetime.now()+timedelta(1)
    time = int(now.strftime("%H"))
    if last_hour != time:
        last_hour = time
        if(time == 0) :
            acceptable_price = tomorrows_price
        if time in acceptable_price:
            print("on")
        else:
            print("off")
        if time == 13:
            year = now.strftime("%Y")
            print("year:", year)

            month = now.strftime("%m")
            print("month:", month)

            day = now.strftime("%d")
            print("day:", day)

            url = 'https://www.elprisetjustnu.se/api/v1/prices/{current_year}/{current_month}-{current_day}_SE3.json'.format(current_year = year, current_month = month, current_day=day)
            price = requests.get(url)
            json_price = json.loads(price.text)
#print(json_price)
            tomorrows_price = []
            for i in range(24):
    #print(item["SEK_per_kWh"])
                if json_price[i]["SEK_per_kWh"] < 0.7 :
                    tomorrows_price.append(i)
                print(tomorrows_price)
