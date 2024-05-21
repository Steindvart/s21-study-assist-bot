import logging as log
from environs import Env

env = Env()
env.read_env()

# #NOTE - configure immediately after import is IMPORTANT!
log.basicConfig(filename='app.log',
                level=log._nameToLevel[env('LOG_LEVEL')],
                format='[{asctime}] {levelname:8} {filename}: {lineno} - {name} - {message}',
                style='{'
)

import os
from dataclasses import dataclass

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import utils
from models.section import get_sections

# ---------------------------------------------

@dataclass
class Config:
  _locale: str = 'ru'
  supportedLocales: tuple = ("ru")
  sections = {}
  bot_token: str = ''

  @property
  def locale(self):
    return self._locale

  @locale.setter
  def locale(self, val):
    if val not in self.supportedLocales:
      raise ValueError(f"{val} locale is not supported.")
    self._locale = val
    self.resources = utils.get_locale_res(val)

  def initialize_sections(self, directory: str):
    self.sections = {section.name: section for section in get_sections(directory)}
    log.info(self.sections)

  def __init__(self) -> None:
    self.resources = utils.get_locale_res(self.locale)
    self.sections = {}
    self.bot_token = env("BOT_TOKEN")


# Global object
config: Config = Config()

src_dir = os.path.dirname(os.path.abspath(__file__))
content_dir = os.path.join(src_dir, '../content')
config.initialize_sections(content_dir)


main_buttons = [
  [],
]

main_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
  keyboard=main_buttons,
  resize_keyboard=True
)

cancel_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
  keyboard=[[KeyboardButton(text="Отмена")]],
  resize_keyboard=True
)