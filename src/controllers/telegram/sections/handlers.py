import logging as log

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

import views.telegram.sections

from .callbacks import SectionsCallbackFactory
from .states import FSMSection

# DEFECT: code duplicate in other scripts
from config import config

res = config.resources
sections = config.sections
router = Router()

# ---------------------------------------------

def get_inputs_list_sections(sections: dict) -> (str, InlineKeyboardMarkup):
  sections_list: str = "\n".join(sections.keys())
  text = (f"{res['sections']['available']}:\n"
          f'{sections_list}')

  keyboard = views.telegram.sections.select_section_keyboard(sections.keys())

  return (text, keyboard)


@router.message(Command(commands=['sections']))
async def process_list_sections_command(message: Message) -> None:
  log.info(sections)
  if not sections:
    await message.answer(f"{res['sections']['no_any']}.")
    return

  text, keyboard = get_inputs_list_sections(sections)
  await message.answer(text, reply_markup=keyboard)


@router.callback_query(SectionsCallbackFactory.filter(), StateFilter(default_state))
async def process_select_section_callback(callback: CallbackQuery, callback_data: SectionsCallbackFactory, state: FSMContext):
  section_name = callback_data.section_name
  section = sections.get(section_name)
  if not section:
    await callback.message.answer(res['sections']['not_found'] % section_name)
    return

  text = (f'📂 {res['sections']['section']}: *{section_name}*\n'
          f'📝 {res['sections']['tests_quantity']}: {section.get_tests_quantity()}\n\n'
          f'📚 {res['sections']['topics']}:\n- {"\n- ".join([str(topic) for topic in section.topics])}')

  keyboard = views.telegram.sections.interactive_section_keyboard()

  await callback.message.edit_text(text, reply_markup=keyboard)
  await state.set_state(FSMSection.section_selected)


@router.callback_query(F.data == 'back_to_select', StateFilter(FSMSection.section_selected))
async def process_back_section_callback(callback: CallbackQuery, state: FSMContext):
  text, keyboard = get_inputs_list_sections(sections)
  await callback.message.edit_text(text, reply_markup=keyboard)
  await state.set_state(default_state)