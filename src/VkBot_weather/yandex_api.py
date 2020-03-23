import yandex_weather_api
import requests

from .consts import YANDEX_KEY


class weather_predict:
    def __init__(self):
        req = requests.session()
        access = yandex_weather_api.get(req, api_key=YANDEX_KEY, lat=55.10, lon=60.10)

    def predict_temp(self):
        return True

    def predict_weath(self):
        return True
