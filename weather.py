from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from googletrans import Translator


# ---------- FREE API KEY examples ---------------------

owm = OWM('c5115b02740f5ac8db830af5047643ef')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details


def current_weather(place):
    translator = Translator()
    observation = mgr.weather_at_place(f'{place}')
    w = observation.weather
    result = translator.translate('cloud', src='en', dest='ru')
    return result.text

