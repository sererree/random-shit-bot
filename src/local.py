from pathlib import Path
from os import path
import json


def root() -> Path:
    return Path(__file__).parent.parent


def filepath() -> Path:
    FILENAME: str = ".users.json"
    return root().joinpath(FILENAME)


def users() -> dict[str, dict[str, bool]]:
    if not path.exists(filepath()):
        return {}

    with open(filepath(), 'r', encoding='utf-8') as data_file:
        return json.load(data_file)


def add_user(user_id: int, subscribed: bool) -> None:
    user_data = users()
    user_data[str(user_id)] = {"subscribed": subscribed}

    with open(filepath(), "w", encoding="utf-8") as data_file:
        json.dump(user_data, data_file)


def subscribe(user_id: int) -> None:
    user_data = users()
    user_data[str(user_id)]["subscribed"] = True

    with open(filepath(), 'w', encoding='utf-8') as data_file:
        json.dump(user_data, data_file)















# for user_id, data in users().items():
#     subscribed = data["subscribed"]
#
#     if subscribed:
#         send_message(user_id)
