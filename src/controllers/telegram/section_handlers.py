import logging as log

from aiogram import Router, types
from aiogram.filters import Command

# DEFECT: code duplicate in other scripts
from config import config

res = config.resources
sections = config.sections
router = Router()

# ---------------------------------------------


@router.message(Command(commands=['sections']))
async def process_list_sections_command(message: types.Message) -> None:
  log.info(sections)
  if not sections:
    await message.answer(f"{res['sections']['no_any']}.")
    return

  sections_list = "\n".join(sections.keys())
  text = (f"{res['sections']['available']}:\n"
          f'{sections_list}')

  await message.answer(text)


@router.message(Command(commands=['topics']))
async def process_list_topics_command(message: types.Message):
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