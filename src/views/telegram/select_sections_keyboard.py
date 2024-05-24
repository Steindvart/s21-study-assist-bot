from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from controllers.telegram.sections.callbacks import SectionsCallbackFactory

# ---------------------------------------------


def get_select_sections_keyboard(sections: list[str]) -> InlineKeyboardMarkup:
  keyboard = InlineKeyboardBuilder()
  for section_name in sections:
    keyboard.button(text=section_name, callback_data=SectionsCallbackFactory(section_name=section_name))

  return keyboard.as_markup()