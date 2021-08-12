#Author: Mike Sisson
#Created Aug 9, 2021
#This is a weather checking app. It prompts the user for the zip code and returns the weather after retrieving information from the server

api = "f8647affb7675ef8cd050e699a5d22e8"
website = "http://api.openweathermap.org/"

#Display welcome message


#Prompt for zip code or city. If City prompt for state
looping = True
while looping == True:
  choice = input("Press 1 to use zip code or press 2 to choose city: ")
  if choice == '1':
   zip = input("What is your 5 digit zip code?: ")
  elif choice == '2':
    city = input("What city are you from?: ")
    state = input("What state are you from?: ")
  else:
    print('Please enter 1 or 2')

#Connect to server to retrieve information. Display connecting during process
print('Connecting to server...')

#If unable to connect ask to retry. 

#Once connected, retrieve and store the weather info
#highTemp = 
#lowTemp = 
#currentTemp = 




#Display weather info

#Prompt to Refresh, quit program or try a new location
