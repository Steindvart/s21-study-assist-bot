from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from controllers.telegram.sections.callbacks import SectionsCallbackFactory, SectonCallbacks

from models.section import Section

from config import config
res = config.resources

# ---------------------------------------------


def select_section_keyboard(sections: list[str]) -> InlineKeyboardMarkup:
  keyboard = InlineKeyboardBuilder()
  for section_name in sections:
    keyboard.button(text=section_name, callback_data=SectionsCallbackFactory(section_name=section_name))

  return keyboard.as_markup()


def get_interactive_section_keyboard() -> InlineKeyboardMarkup:
  keyboard = InlineKeyboardBuilder([
    [InlineKeyboardButton(text=res['testing']['start'], callback_data=SectonCallbacks.start_testing)],
    [InlineKeyboardButton(text=res['sections']['back_to_select'], callback_data=SectonCallbacks.back_to_select)]
  ])

  return keyboard.as_markup()


def get_body_list_sections(sections: dict) -> (str, InlineKeyboardMarkup):
  sections_list: str = "\n- ".join(sections.keys())
  text = (f"{res['sections']['available']}:\n"
          f'- {sections_list}')

  keyboard = select_section_keyboard(sections.keys())

  return (text, keyboard)


def get_body_select_section(section: Section) -> (str, InlineKeyboardMarkup):
  text = (f'📂 {res['sections']['section']}: *{section.name}*\n'
          f'📝 {res['sections']['tests_quantity']}: {section.get_tests_quantity()}\n\n'
          f'📚 {res['sections']['topics']}:\n- {"\n- ".join([str(topic) for topic in section.topics])}')

  keyboard = get_interactive_section_keyboard()

  return (text, keyboard)