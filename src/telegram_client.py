import requests
import json


class TelegramClient:
    def __init__(self, token: str, chat_id: str) -> None:
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{token}"

    def _send_request(
            self,
            endpoint: str,
            method: str = "POST",
            headers: dict = None,
            params: dict = None,
            data: dict = None
    ):
        return requests.request(
            method=method,
            url=f"{self.api_url}/{endpoint}",
            headers=headers,
            params=params,
            data=data,
        ).json()

    def send_message(self, message: str) -> None:
        self._send_request(
            endpoint="sendMessage",
            params={
                "text": message,
                "chat_id": self.chat_id,
                "parse_mode": "Markdown",
            },
        )

    def send_photo_with_keyboard(self, photo_url: str) -> None:
        bandit_id = 1
        self._send_request(
            endpoint="sendPhoto",
            params={
                "photo": photo_url,
                "chat_id": self.chat_id,
                "reply_markup": json.dumps({
                    "inline_keyboard": [[
                        {"text": "👍", "callback_data": f"{bandit_id}:1"},
                        {"text": "👎", "callback_data": f"{bandit_id}:0"},
                    ]],
                    "resize_keyboard": True,
                    "one_time_keyboard": True,
                })
            },
        )

    def answer_callback(self, query_id):
        self._send_request(
            endpoint="answerCallbackQuery",
            params={
                "callback_query_id": query_id
            }
        )
