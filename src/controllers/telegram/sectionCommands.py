import logging as log

from aiogram import Dispatcher, types
from aiogram.filters import Command

# DEFECT: code duplicate in other scripts
from bot import bot_config

res = bot_config.resources
sections = bot_config.sections


def register_section_commnads(dp: Dispatcher) -> None:
  dp.message.register(list_sections, Command(commands=['sections']))
  dp.message.register(list_topics, Command(commands=['topics']))


async def list_sections(message: types.Message) -> None:
  log.info(sections)
  if not sections:
    await message.answer(f"{res['sections']['no_any']}.")
    return

  sections_list = "\n".join(sections.keys())
  text = (f"{res['sections']['available']}:\n"
          f'{sections_list}')

  await message.answer(text)


async def list_topics(message: types.Message):
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