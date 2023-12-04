import requests
import json

# This code above imports the requests library for making HTTP requests 
# and the json library for handling JSON data in a Python script.

# This code reads information from a file named 'creds.json' 
# and stores it in a variable called 'creds'.
with open('creds.json', 'r') as file:
    creds = json.load(file)

# This code retrieves an API key named 'API_KEY' from a dictionary 
# called creds and assigns it to the variable API.
API_KEY= creds.get('API_KEY')

# This code prompts the user for a city name, fetches weather 
# data from OpenWeatherMap, and repeats until a valid city is entered, 
# stopping only if the API request is successful; otherwise, it informs 
# the user to enter a valid city.

while True:
    CITY = input('Enter a city-name or location:\n')

    if not CITY:
        print('Location not found.. ')
        print('Please enter another location or city name.. ')
        continue

    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        break
    else:
        print('Could not find the location you were looking for.')
        print('Please try again to enter a valid city-name:')

# This code checks if the weather request was successful 
# (status code 200) and, if so, prints key weather information for 
# a specified city; otherwise, it prints an error message 
# for a city not found.

if response.status_code == 200:
    data = response.json()
    current_temperature_kelvin = data['main']['temp']
    current_temperature_celsius = current_temperature_kelvin - 273.15
    feels_like_temperature_kelvin = data['main']['feels_like']
    celsius_feel_like = feels_like_temperature_kelvin - 273.15
    weather_description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    print(' ')
    print(' ')
    print(f'Here is your requested weather information for {CITY}!')
    print(f'Current temperature is {current_temperature_celsius:.0f} °C')
    print(f'But, the temperature feels like {celsius_feel_like:.0f} °C')
    print(f'Weather type is {weather_description}')
    print(f'The wind speed is {wind_speed:.1f} m/s')
else:
    print('Cannot find the specific city')
