from pyowm import OWM
from tokens import owm_token


owm = OWM(str(owm_token))
mgr = owm.weather_manager()


def current_weather(place):
    observation = mgr.weather_at_place(f'{place}')
    w = observation.weather
    temp_dict_celsius = w.temperature('celsius')
    result = w.detailed_status + ' ' + f'\nLowest temperature: {temp_dict_celsius["temp_min"]}' + \
             f'\nHigher temperature: {temp_dict_celsius["temp_max"]}' + \
             f'\nFeels like: {temp_dict_celsius["feels_like"]}'
    return result
