# Simple tele-weather
Simple-tele-weather this is a bot for receiving current weather in the selected city. The bot is based on the pyTelegraBotAPI library for Python, it provides a bot, as well as on Pyowm, it provides weather information.

# Before the start

You need to register your bot from [@BotFather](https://t.me/botfather#:~:text=BotFather%20is%20the%20one%20bot,BotFather%20right%20away.) to get a token. After that you need to register on [OpenWeatherMap](https://openweathermap.org/) to get a token for pyowm.

# How to run it
To start the bot you need to have: [Python](https://www.python.org/), [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) library, [pyowm](https://pypi.org/project/pyowm/) library 

After receiving the tokens, you need to clone this repository to the root directory (using Git or download the archive). Tokens need to be recorded in `tokens.py` to the corresponding variables. That is, in `tele_token`, you write to the token received from the telegram, and in the `owm_token`, write token from OpenWeatherMap.

To start run main.py

# How to run it (for termux)
Enter these commands to install and start the bot:

 1. `pkg upgrade`
 2. `pkg install python`
 3. `pip install pyTelegramBotAPI`
 4. `pip install pyowm`
 5. `pkg install git`
 6. `git clone https://github.com/wm-d-a/tele-weather`
 7. `cd tele-weather`
 8. `rm tokens.py`
 9. `echo token="'YOUR TELEGRAM TOKEN'" >> tokens.py`
 10. `echo owm_token="'YOR OWM TOKEN'" >> tokens.py`
 11. `python3 main.py` 
