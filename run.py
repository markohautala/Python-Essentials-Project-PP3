import requests

API = '93746a98d57a67a21efa064b49cecea4'

while True:
    CITY = input('Enter a name on a city or location: ')

    # Validate user input
    if not CITY:
        print('Location not found.. ')
        print('Please enter another location or city name.. ')
        continue

    HTTP_LOCATION = 'http://api.openweathermap.org/data/2.5/weather?q='

    url = HTTP_LOCATION + CITY + '&appid=' + API

    # Make the request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        break
    else:
        print('Could not find the location you were looking for.')
        print('Please try again to enter a valid city name:')

# Rest of your code for processing the weather data
if response.status_code == 200:
    data = response.json()
    current_temperature_kelvin = data['main']['temp']
    current_temperature_celsius = current_temperature_kelvin - 273.15
    feels_like_temperature_kelvin = data['main']['feels_like']
    feels_like_temperature_celsius = feels_like_temperature_kelvin - 273.15
    weather_description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']

    print(f'Current Temperature: {current_temperature_celsius:.0f} °C')
    print(f'Feels Like: {feels_like_temperature_celsius:.0f} °C')
    print(f'Weather Type: {weather_description}')
    print(f'Wind Speed: {wind_speed:.1f} m/s')
else:
    print('Cannot find the specific city')
