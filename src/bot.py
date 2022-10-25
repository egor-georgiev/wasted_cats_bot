from telegram_client import TelegramClient
from utils import _get_cat_image_url
from constants import HANDLES


class Bot:
    def __init__(self, telegram_client: TelegramClient, message_text: str) -> None:
        self.telegram_client = telegram_client
        self.message_text = message_text

    def run(self):
        message_text = self.message_text
        if message_text == "/start":
            self.start()
        elif message_text == "/help":
            self.help()
        elif message_text == "/cat":
            self.cat()
        else:
            self.help()

    def start(self):
        self.telegram_client.send_message(
            "Welcome to Wasted Cats Bot! I am going to recommend you cats.\n*Let's start!*"
        )
        self.help()

    def help(self):
        self.telegram_client.send_message(
            "/help: show this message\n"
            "/cat: show a cat"
        )

    def cat(self):
        image_url = _get_cat_image_url(HANDLES[0])
        self.telegram_client.send_photo_with_keyboard(image_url)
