import os
import json
import urllib3
import requests
import pymongo

from typing import Any

TG_TOKEN = os.getenv("TG_TOKEN")
URL = f"https://api.telegram.org/bot{TG_TOKEN}/"

http = urllib3.PoolManager()


def send_message(text: str, chat_id: str) -> None:
    final_text = "Ваше сообщение было: " + text
    url = URL + f"sendMessage?text={final_text}&chat_id={chat_id}"
    http.request("GET", url)


def handler(event: dict[str, str], context: Any) -> dict[str, int]:
    # все сообщение
    message = json.loads(event['body'])
    # id чата, чтобы потом отправить в тот же диалог
    chat_id = message['message']['chat']['id']
    # сам текст
    reply = message['message']['text']
    send_message(reply, chat_id)
    # для отладки -- чтобы в логах посмотреть на структуру пришедшего события
    return {'statusCode': 200}
