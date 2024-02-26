# Python Weather App
### This Python script is a simple weather app that tells you the current weather in a city you choose. It uses OpenWeatherMap and asks for your city input until you provide a valid one. After inputting a city, it shows you the current temperature, "feels like" temperature, weather description, and wind speed.

<p align="center">
  <img src="/assets/images/responsive.png" alt="Responsive website" width="500">
</p>

[This is the link](https://python-weather-api-app-ed5b5d981766.herokuapp.com/) to the deployed webpage/URL.

[This is the link](https://github.com/markohautala/Python-Essentials-Project-PP3) to the GitHub repository for this project.

<hr>

## How to use it
- This app works in a terminal only. Users can interact with the application by running the script in a terminal environment, inputting information when prompted, and receiving output directly in the terminal.

- Enter City Name:
When prompted, enter the name of the city for which you want to check the weather.
View Weather Information:
The app will fetch and display the current temperature, "feels like" temperature, weather description, and wind speed for the specified city.

- Invalid City:
If you provide a city that doesn't exist or is misspelled, the app will notify you that the location was not found.
You'll be prompted to enter another location or correct the city name.

<hr>

## Features
Initially, this is the start-screen with a message saying that the user can input a location
in order to recieve weather information of that location.
<p align="center">
  <img src="/assets/images/start.png" alt="startup terminal state" width="400">
</p>
<hr>

The user can then input any location - either a city or even a country. It does not need to be 
capitalized - the input-text can be all lower-case.
<p align="center">
  <img src="/assets/images/input.png" alt="input to terminal" width="400">
</p>
<hr>

If the entered location is valid, the user will receive current weather information for that location. The output will include details such as the location name, temperature, "feels-like" temperature, the weather condition (sunny, cloudy, mist, etc.), and the wind speed. This provides a real-time snapshot of the current weather conditions in the specified area.
<p align="center">
  <img src="/assets/images/output-correct-value.png" alt="output of correct value" width="400">
</p>
<hr>

If the user inputs an invalid text, meaning a location that doesn't exist or is misspelled, the app will display a message stating that the location is not found.
<p align="center">
  <img src="/assets/images/input-wrong.png" alt="input wrong" width="400">
</p>

<p align="center">
  <img src="/assets/images/wrong-input-submit.png" alt="wrong input result" width="400">
</p>
<hr>

The user is then given another opportunity to enter a different location or correct any potential spelling mistakes. This feedback functionality ensures that the user can make adjustments and retry until a valid location is provided.
<p align="center">
  <img src="/assets/images/type-in-correct-again.png" alt="wrong input type in again" width="400">
</p>
<hr>

The user first typed in a wrong location, got an error message, but then entered a correct location and got the current weather info. This shows that the app can deal with mistakes and still give the right information when the user provides a valid location.
<p align="center">
  <img src="/assets/images/type-in-correct-again-result.png" alt="correct result from wrong input at first" width="400">
</p>

<hr>

## Future features
- Adding time for sunrise and sunset
- Once you get the weather info you want, the app can ask if you'd like to check another city. If you say 'YES,' the app starts over, letting you enter a new city for weather details without the need to "run the program" again.

<hr>

## Bugs or problems encountered
#### Solved Bugs
- Linter first warned about the url-line being too long. This was solved by declaring another
variable called "WEBPAGE" and giving it the value of the url to where the API is fetching data from.
Then the variable was added in the placeholder in the f-string - this removed the warning from the Linter.
- When the user got the output from a valid input, the terminal in opinion became too cluttered, so I added two print statements with empty strings one after another to create some 'space' in the terminal.

#### Unsolved Bugs
- No unsolved bugs encountered.

<hr>

## Testing
Code is tested in both CodeAnywhere therminal and in Code Institute Heroku terminal and code
is working as intended.

I have tried and put in wrong and miss-spelled values and the error-message is working as it should, 
giving the user another chance to re-write a location or city-name that is valid.

<hr>

## Validator testing
Python code passes Linter with "All clear, no errors found".
Python code passes PEP8 without issues.

<hr>

## Deployment procedure
This project was deployed using Code Institute's pre-deployed "mock" terminal on Heroku. Follow these steps for successful deployment:
- Clone or Fork the Repository:
- Copy the project's code from the GitHub repository (link provided in the README).
- Create a New Heroku App.
- Log in to Heroku and create a new app from the Heroku dashboard.
Add Buildpacks:
   - In the app settings, add the Python buildpack first, followed by the Node.js buildpack. Order matters.
- Link Heroku App to Repository:
- Connect your Heroku app to the GitHub repository where you cloned or forked the project.
Deploy:
   - Click on either manual deploy or set up automatic deployment in the Heroku app settings.

By following these steps, your project will be deployed on Heroku using Code Institute's pre-configured "mock" terminal environment.

Crucial Information:
Ensure the requirements.txt file includes the following line to specify the required dependency:
   - requests==2.26.0

<hr>

## Credits
- Code Institute provided the deployment terminal.
- API to webpage is recieved from [this webpage](https://openweathermap.org/api)


<hr>
