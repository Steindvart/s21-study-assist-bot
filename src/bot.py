from dataclasses import dataclass

from aiogram import Bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from environs import Env
import utils


@dataclass
class BotConfig:
  @property
  def locale(self):
    return self._locale

  @locale.setter
  def locale(self, newVal):
    if newVal not in self.supportedLocales:
        raise f"{newVal} locale is not supported."
    self._locale = newVal

  # Methods
  def __init__(self) -> None:
    # TODO - find better way to define props
    # Data
    self.supportedLocales = ("ru")
    # self.resources: dict[str, Any]

    # NOTE - Default locale is "ru"
    # DEFECT - Get first locale from supported, no hard-code
    self.locale = "ru"
    self.resources = utils.get_locale_res(self.locale)

# Global obj
bot_config: BotConfig = BotConfig()

# TODO - ugly
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
