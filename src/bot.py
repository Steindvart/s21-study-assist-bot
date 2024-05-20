import logging as log
import os
from dataclasses import dataclass

from aiogram import Bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from environs import Env
import utils

from models.section import get_sections

@dataclass
class BotConfig:
  _locale: str = 'ru'
  supportedLocales = ("ru",)
  sections = {}

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


# Global object
bot_config: BotConfig = BotConfig()

src_dir = os.path.dirname(os.path.abspath(__file__))
content_dir = os.path.join(src_dir, '../content')
bot_config.initialize_sections(content_dir)


env = Env()
env.read_env()

bot: Bot = Bot(env("BOT_TOKEN"), parse_mode="Markdown")

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