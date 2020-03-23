import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent

import random
import os

from datetime import datetime
from time import time, gmtime, sleep

from .consts import GROUP_ID, VK_KEY
from .yandex_api import weather_predict


class bot_logic:
    def __init__(self):

        api_token = VK_KEY
        vk_session = vk_api.VkApi(token=api_token)
        self.vk = vk_session.get_api()
        self.longpoll = VkBotLongPoll(vk=vk_session, group_id=GROUP_ID)

    def send_weather(self):
        while True:
            sec = time()
            now_hour = gmtime(sec)[2]
            now_minute = gmtime(sec)[3]
            now_sec = gmtime(sec)[4]

            if now_hour == 5 and now_minute == 0 and now_sec == 0:

                predict = weather_predict()
                predict_temp = predict.predict_temp()
                predict_weath = predict.predict_weath()

                self.vk.messages.send(
                    message="", random_id=random.getrandbits(32), peer_id=""
                )

            sleep(200000)

        return True

    def event_handling(self):
        for event in self.longpoll.listen():
            print(event)

        return True
