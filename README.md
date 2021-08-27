# SIMPLE-TELE-WEATHER
Simple-tele-weather this is a bot for receiving current weather in the selected city. The bot is based on the pyTelegraBotAPI library for Python, it provides a bot, as well as on Pyowm, it provides weather information.

# PREPARATION FOR LAUNCH

You need to register your bot from [@BotFather](https://t.me/botfather#:~:text=BotFather%20is%20the%20one%20bot,BotFather%20right%20away.) to get a token. After that you need to register on [OpenWeatherMap](https://openweathermap.org/) to get a token for pyowm.

# HOW TO RUN IT
To start the bot you need to have: [Python](https://www.python.org/), [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) library, [pyowm](https://pypi.org/project/pyowm/) library 

After receiving the tokens, you need to cloning this repository (using Git or download the archive). In the repository you need to create a tokens.py file. There should be two variables in the created file: token (stores the token received from BotFather) and OWM _Token (stores the token is kept on OpenWeatherMap). They write the resulting tokens.

To start run main.py

# HOW TO RUN IT (FOR TERMUX)
Enter these commands to install and start the bot:

 1. `pkg upgrade`
 2. `pkg install python`
 3. `pip install pyTelegramBotAPI`
 4. `pip install pyowm`
 5. `pkg install git`
 6. `git clone https://github.com/wm-d-a/tele-weather`
 7. `cd tele-weather`
 8. `echo token="'YOUR TELEGRAM TOKEN'" >> tokens.py`
 9. `echo owm_token="'YOR OWM TOKEN'" >> tokens.py`
 10. `python3 main.py` 
