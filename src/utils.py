import json

from aiogram.types import User, Message


def get_locale_res(locale: str):
  with open(f"res/locales/{locale}.json", "r", encoding="utf8") as file:
    return json.load(file)


def get_all_info(botInfo: User, msg: Message) -> dict[str, object]:
  return {
    "bot": json.loads(botInfo.json()),
    "user": json.loads(msg.from_user.json()),
    "chat": json.loads(msg.chat.json())
  }


def get_log_str(source: str, usr: User) -> str:
  return  f"{source} - User_id: {usr.id}, " \
          f"first_name: {usr.first_name}, " \
          f"language_code: {usr.language_code}"
