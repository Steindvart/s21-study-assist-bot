import logging as log

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from views.telegram.select_sections_keyboard import get_select_sections_keyboard

# DEFECT: code duplicate in other scripts
from config import config
from .callbacks import SectionsCallbackFactory

res = config.resources
sections = config.sections
router = Router()

# ---------------------------------------------


@router.message(Command(commands=['sections']))
async def process_list_sections_command(message: Message) -> None:
  log.info(sections)
  if not sections:
    await message.answer(f"{res['sections']['no_any']}.")
    return

  sections_list = "\n".join(sections.keys())
  text = (f"{res['sections']['available']}:\n"
          f'{sections_list}')

  keyboard = get_select_sections_keyboard(sections.keys())

  await message.answer(text, reply_markup=keyboard)


@router.callback_query(SectionsCallbackFactory.filter())
async def process_section_callback(callback: CallbackQuery, callback_data: SectionsCallbackFactory):
    test = sections.get(callback_data.section_name).topics[0].tests[0]
    await callback.message.answer(str(test))
    await callback.answer()


@router.message(Command(commands=['topics']))
async def process_list_topics_command(message: Message):
  command_parts = message.text.split()
  if len(command_parts) < 2:
    await message.answer(f"{res['topics']['specify']}.\n{res['topics']['format']}")
    return

  section_name = command_parts[1]
  section = sections.get(section_name)
  if not section:
    await message.answer(res['sections']['not_found'] % section_name)
    return

  topics = section.get_topics()
  if not topics:
    await message.answer(res['topics']['no_any'] % section_name)
    return

  topics_list = "\n".join(topics)
  text = res['topics']['_prev'] % section_name
  text += f':\n{topics_list}'

  await message.answer(text)