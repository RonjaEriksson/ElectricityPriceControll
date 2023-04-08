import requests
import json
from datetime import datetime, timedelta
hours_needed = 5
def takePrice(elem):
    return float(elem["SEK_per_kWh"])

last_hour = -1
now = datetime.now()
best_hours_today = []
best_hours_tomorrow = []
year = now.strftime("%Y")

month = now.strftime("%m")

day = now.strftime("%d")

url = 'https://www.elprisetjustnu.se/api/v1/prices/{current_year}/{current_month}-{current_day}_SE3.json'.format(current_year = year, current_month = month, current_day=day)
price = requests.get(url)
json_price = json.loads(price.text)
#print(json_price)
json_price.sort(key=takePrice)
for i in range(hours_needed):
    print(json_price[i]["SEK_per_kWh"])
    time = json_price[i]["time_start"]
    hours = time.split("T")[1]
    print(hours)
    time = int(hours.split(":")[0])
    print(time)
    best_hours_today.append(time)
print(best_hours_today)
while True:
    now = datetime.now()+timedelta(1)
    time = int(now.strftime("%H"))
    if last_hour != time:
        last_hour = time
        if(time == 0) :
            best_hours_today = best_hours_tomorrow
        if time in best_hours_today:
            print("on")
        else:
            print("off")
        if time == 14:
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
            best_hours_tomorrow = []
            json_price.sort(key=takePrice)
            for i in range(hours_needed):
                    time = json_price[i]["time_start"]
                    hours = time.split("T")[1]
                    time = int(hours.split(":")[0])
                    best_hours_tomorrow.append(time)
            print(best_hours_tomorrow)
