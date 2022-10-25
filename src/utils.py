import os
import random

from pymongo import MongoClient
from pymongo.database import Database
import requests

from constants import (
    DATABASE_NAME,
    MONGO_SRV,
    MONGO_USER,
    MONGO_PASSWORD,
    CAT_API_URL,
    CAT_API_SEARCH_ENDPOINT,
)


def _get_mongo_db() -> Database:
    return MongoClient(
        host=os.getenv(MONGO_SRV),
        username=os.getenv(MONGO_USER),
        password=os.getenv(MONGO_PASSWORD),
    )[DATABASE_NAME]


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
            'x-api-key': os.environ.get('CAT_API_KEY'),
            'mime_types': 'png,jpg',
        },
    ).json()[0]["url"]
