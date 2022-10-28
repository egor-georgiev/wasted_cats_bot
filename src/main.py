import json
import logging
import traceback
from typing import Any, Union

from utils import process_callback, process_message

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel("DEBUG")


def handler(event: dict[str, str], context: Any) -> dict[str, Union[str, int]]:
    try:
        message = json.loads(event["body"])
        LOGGER.debug(message)

        if "callback_query" in message.keys():
            process_callback(message)
            return {"statusCode": 200}
        else:
            process_message(message)
            return {"statusCode": 200}

    except Exception:  # noqa
        LOGGER.error(traceback.format_exc())
        return {
            "statusCode": 500,
        }
