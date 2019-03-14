#! python3
#quickWeather.py - Prints weather for location from cmd
import json, requests, sys, datetime
import numpy as np

#get current time
currentTime = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')

#convert kalvin to fahrenheit
def kToF(x):
    try:
        x = round(((x - 273.15) * 9/5 + 32), 2)
    except:
        x = 0
    return x

#Get location from cmd line
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

#Download the JSON data from OpenWeatherMap
#url = https://api.openweathermap.org/data/2.5/weather?q=Chicago,us&appid=524038e6c837861898129844f588104d
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=524038e6c837861898129844f588104d' % (location)
response = requests.get(url)
response.raise_for_status()

#Load JSON data into a Python variable
weatherData = json.loads(response.text)

#Assign json to variables
conditions = weatherData['weather']
temp = weatherData['main']
CurrentTemp = kToF(temp['temp'])
Min = kToF(temp['temp'])
Max = kToF(temp['temp'])

#rows = []
#columns = ['Date', 'Current', 'Min', 'Max', 'Location']
#row = [currentTime, CurrentTemp, Min, Max, location]
#rows.append(row)
#df = pd.DataFrame(rows, columns = columns)

#Print out info
print('Current weather in %s:' % (location))
print('Current Time: %s' % (currentTime))
print('The weather is currently : ' + str(kToF(temp['temp'])) + ' *F')
print('Daily min: ' + str(kToF(temp['temp_min'])) + ' *F. Daily max: ' + str(kToF(temp['temp_max'])) + ' *F')
#print('Current conditions: ' + conditions['description'])
input()
