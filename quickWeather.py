#! python3
#quickWeather.py - Prints current weather(in Fahrenheit) for location 
#from cmd using openweather api
import json, sys, datetime

#Use app open weather api key
appid = #enter api key here

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
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, appid)
response = requests.get(url)
response.raise_for_status()

#Load JSON data into a Python variable
weatherData = json.loads(response.text)

#Assign json to variables
conditions = weatherData['weather']
temp = weatherData['main']
CurrentTemp = kToF(temp['temp'])

#Print out info
print('Current weather in %s:' % (location))
print('Current Time: %s' % (currentTime))
print('The weather is currently : ' + str(kToF(temp['temp'])) + ' *F')
print('Daily min: ' + str(kToF(temp['temp_min'])) + ' *F. Daily max: ' + str(kToF(temp['temp_max'])) + ' *F')
input()

