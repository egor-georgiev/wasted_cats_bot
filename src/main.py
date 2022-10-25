import os
import json
import logging

from telegram_client import TelegramClient
from bot import Bot
from typing import Any, Union

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel("DEBUG")


def handler(event: dict[str, str], context: Any) -> dict[str, Union[str, int]]:
    try:
        message = json.loads(event["body"])
        LOGGER.debug(message)

        if "callback_query" in message.keys():
            tg = TelegramClient(
                chat_id=message["callback_query"]["message"]["chat"]["id"],
                token=os.getenv("TG_TOKEN"),
            )
            tg.answer_callback(query_id=message["callback_query"]["id"])
            return {"statusCode": 200}
        else:
            tg = TelegramClient(
                chat_id=message["message"]["chat"]["id"],
                token=os.getenv("TG_TOKEN"),
            )
            message_text = message["message"]["text"]
            Bot(telegram_client=tg, message_text=message_text).run()
            return {"statusCode": 200}

    except Exception as e:
        LOGGER.error(repr(e))
        return {
            "statusCode": 500,
        }
