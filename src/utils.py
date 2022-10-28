import os
import random
import re
from typing import Any

import requests

from constants import *
from mab import EpsilonGreedy
from telegram_client import TelegramClient

CALLBACK_PARSER = re.compile("([0-9]):([0-9])")


def process_callback(message: dict[Any]):
    chat_id = message["callback_query"]["message"]["chat"]["id"]

    tg = TelegramClient(
        chat_id=chat_id,
        token=os.getenv("TG_TOKEN"),
    )
    eg = EpsilonGreedy(user_id=str(chat_id), n_arms=len(HANDLES))

    arm_id, reward = CALLBACK_PARSER.match(message["callback_query"]["data"]).groups()
    eg.update(arm_id=int(arm_id), reward=int(reward))

    tg.answer_callback(query_id=message["callback_query"]["id"])
    tg.clear_inline_keyboard(message_id=message["callback_query"]["message"]["message_id"])

    _send_cat(chat_id, tg)


def process_message(message: dict[Any]):
    chat_id = message["message"]["chat"]["id"]
    tg = TelegramClient(
        chat_id=chat_id,
        token=os.getenv("TG_TOKEN"),
    )

    message_text = message["message"]["text"]

    if message_text == "/start":
        tg.send_message(
            "Hi! I am Wasted Cats Bot. I am going to *recommend you cats*.\n"
            "You can let me know, whether you like them or not, and I will adjust my recommendations.\n"
            "To let me know about your preferences, please press 👍 or 👎 that appear under a cat picture.\n\n"
            "Let's start!\n"
            "To get a cat, press /cat."
        )
        _send_cat(chat_id, tg)
    elif message_text == "/cat":
        _send_cat(chat_id, tg)
    else:
        tg.send_message(message="to get a cat press /cat")


def _send_cat(chat_id: int, tg: TelegramClient):
    arm_id = EpsilonGreedy(user_id=str(chat_id), n_arms=len(HANDLES)).decide()
    image_url = _get_cat_image_url(HANDLES[arm_id])
    tg.send_photo_with_keyboard(image_url, arm_id)


def _get_cat_image_url(breeds: tuple) -> str:
    breed = random.choice(breeds)
    return requests.request(
        method="GET",
        url=f"{CAT_API_URL}{CAT_API_SEARCH_ENDPOINT}",
        params={
            "limit": 1,
            "order": "RAND",
            "has_breeds": 1,
            "breed_ids": breed,
        },
        headers={
            "x-api-key": os.environ.get(CAT_API_KEY),
            "mime_types": "png,jpg",
        },
    ).json()[0]["url"]
