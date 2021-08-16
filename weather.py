from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from tokens import owm_token

# ---------- FREE API KEY examples ---------------------

owm = OWM(str(owm_token))
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details


def current_weather(place):
    observation = mgr.weather_at_place(f'{place}')
    w = observation.weather
    result = w.detail_status
    return result.text
