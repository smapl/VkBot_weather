import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent



import random
import os

from consts import GROUP_ID, YANDEX_KEY

api_token = os.environ["vk_token"]
vk_session = vk_api.VkApi(token=api_token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk=vk_session, group_id=GROUP_ID)


if __name__ == "__main__":
    vk.messages.send(
        message="", random_id=random.getrandbits(32), peer_id="",
    )
