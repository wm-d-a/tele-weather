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
    temp_dict_celsius = w.temperature('celsius')  # guess?
    # print(temp_dict_celsius)
    result = w.detailed_status + ' ' + f'\nМиниманльная температура: {temp_dict_celsius["temp_min"]}' + \
             f'\nМаксимальная температура: {temp_dict_celsius["temp_max"]}' + \
             f'\nЧувствется как: {temp_dict_celsius["feels_like"]}'
    return result
