#Author: Mike Sisson
#Created Aug 9, 2021
#This is a weather checking app. It prompts the user for the zip code and returns the weather after retrieving information from the server

#sets api key and web addresses for pulling data requests
import requests

api = "f8647affb7675ef8cd050e699a5d22e8"
website = "http://api.openweathermap.org/"

webByCityState1 = 'http://api.openweathermap.org/data/2.5/weather?q='
#enter city and state separated by comma between two strings city name,state code
webByCityState2 = ',us&units=imperial&appid=f8647affb7675ef8cd050e699a5d22e8'

webByZip1 = "http://api.openweathermap.org/data/2.5/weather?zip="
#enter zip code between two strings zip code
webByZip2 = "&units=imperial&appid=f8647affb7675ef8cd050e699a5d22e8"
#Display welcome message

#passes in strings for web address then grabs data from server
def getWeather(webString1, webString2, userLocation):
  print('Connecting to server...')
  try:
    response1 = requests.get(webString1 + userLocation + webString2)
    rawWeather = response1.json()
    print("Connection successful.")
    return rawWeather
  except:
    print("Something went wrong.")
    print("Connection unsuccessful.")

#Display weather info
def displayWeather(rawWeather):
  try:
    currentTemperature = rawWeather['main']['temp']
    highTemp = rawWeather['main']['temp_min']
    lowTemp = rawWeather['main']['temp_max']
    feelsLike = rawWeather['main']['feels_like']
    print("Currently, it is " + str(currentTemperature) + " degrees.")
    print("It feels like " + str(feelsLike) + " degrees.")
    print("Low: " + str(lowTemp))
    print("High: " + str(highTemp))
  except:
    print("Something went wrong.")

def main():
#Prompt for zip code or city. If City prompt for state
  looping = True
  while looping == True:
    choice = input("Press 1 to use zip code, press 2 to choose city, or 3 to exit: ")
    if choice == '1':
      zip = input("What is your 5 digit zip code?: ")
      rawWeather = getWeather(webByZip1, webByZip2, zip)
      displayWeather(rawWeather)
    elif choice == '2':
      city = input("What city are you from?: ")
      state = input("What state are you from?: ")
      location = (city + "," + state)
      rawWeather = getWeather(webByCityState1, webByCityState2, location)
      displayWeather(rawWeather)
    elif choice == '3':
      exit(0)
    else:
      print('Please enter 1 or 2')




#running code
main()