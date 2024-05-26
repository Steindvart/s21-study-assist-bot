from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from controllers.telegram.sections.callbacks import SectionsCallbackFactory

from config import config
res = config.resources

# ---------------------------------------------


def select_section_keyboard(sections: list[str]) -> InlineKeyboardMarkup:
  keyboard = InlineKeyboardBuilder()
  for section_name in sections:
    keyboard.button(text=section_name, callback_data=SectionsCallbackFactory(section_name=section_name))

  return keyboard.as_markup()


def interactive_section_keyboard() -> InlineKeyboardMarkup:
  keyboard = InlineKeyboardBuilder([
    [InlineKeyboardButton(text=res['testing']['start'], callback_data='start_testing')],
    [InlineKeyboardButton(text=res['sections']['back_to_select'], callback_data='back_to_select')]
  ])

  return keyboard.as_markup()