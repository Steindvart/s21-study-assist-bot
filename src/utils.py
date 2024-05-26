import json
import os

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


def get_formated_main_commands_desc(obj) -> list[str]:
  formatted_list = []
  for key, value in obj.items():
    if key == "_prev":
      formatted_list.append(f'{value}:')
      continue
    formatted_list.append(f"{key} - {value}")
  return formatted_list


def get_only_filename(path: str) -> str:
  filename_with_extension = os.path.basename(path)
  filename, _ = os.path.splitext(filename_with_extension)
  return filename