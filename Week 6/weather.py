import urllib.request
import urllib.parse
import json
# Adapted from Python for Everyone (Horstmann & Necaise)

# Sign up for an Open Weather account:
# https://home.openweathermap.org/users/sign_up
# go to API keys, copy and paste

# API stands for Application Programming Interface
# It is the way that data can be transferred between programs
# In this case, we are going to pull data from a website (Open Weater)
#   into our Python programming environment

# ask user for the name of the location
city = input("Enter the name of a city: ")

# write the URL
params = {"appid":"7d8615fc2e5e528e24c0a03e480f10e1", "q": city, "units": "imperial"}
arguments = urllib.parse.urlencode(params) # convert params to a URL encoding

print(arguments) # ever see this in a URL??? anything after a "?" is a parameter

# retrieve weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments # see!

print(url)

webData = urllib.request.urlopen(url) # Open a connection to URL
results2 = webData.read().decode('UTF-8')
webData.close() # CLOSE THE CONNECTION!

# convert JSON to a Python dictionary
data = json.loads(results2)

print(data)

# print results
current = data["main"]
degreeSym = chr(176) # this is a way to create the degree symbol!
print(f'The current weather in {city} is:')
print(f'Temperature: {current["temp"]}{degreeSym}F')
print(f'Humidity: {current["humidity"]}')

## CHALLENGE:
# figure out how to access the weather description
# you may want to jump into interactive Python mode in Terminal
#   and then copy-and-paste the dictionary output as a variable
# then try accessing the dictionary...
