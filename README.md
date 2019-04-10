# py-api
Short projects using APIs. 
 
quickWeather.py is a program to test my first API with in Python. I am using the OpenWeather API to receive current weather results.
The user needs an api key from OpenWeather to be able to run this program. This includes current temperature in degrees Fahrenheit, as well as the expected low and high of the given location. This program requires the user to enter a location from the command line which corresponds with the API location information. Please consult the OpenWeather API if searching for a specific location. 
Example: quickWeather.py Cincinnati, US. Enter this into the command line, and it will return current weather information for Cincinnati, OH. 

Brewery_Timeline.R is a program to pull the twitter timelines from two well-known breweries in the Cincinnati area using the Rtweet package. It is necessary to have a developer Twitter account to provide your username, key, and secret code. The packages Rtweet and httpuv make this process very simple and straight-forward, once you have acquired your developer credentials. This is part of my project looking at how two popular breweries in the area differentiate themselves based on their Twitter activity, not including any retweets. I set the number of tweets to look for at 3000 because I wanted to get enough Tweets from each brewery's official account in regards to examine data from the past 3 years. Rhinegeist has one official account, while MadTree has two accounts: one for the taproom they opened in 2017 and their brand Twitter account. 
