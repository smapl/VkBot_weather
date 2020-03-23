import yandex_weather_api

import requests

from consts import YANDEX_KEY


req = requests.session()
access = yandex_weather_api.get(req, api_key=YANDEX_KEY,  lat=55.10, lon=60.10)
print(access)