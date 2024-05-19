import logging

from aiogram import types

from section import get_sections

# DEFECT - using global objects, not good
from bot import bot, bot_config, main_keyboard
import utils

# Alliaces
res = bot_config.resources

sections = {}

def initialize_sections():
  global sections
  sections = {section.name: section for section in get_sections()}

async def start(message: types.Message) -> None:
  logging.info(utils.get_log_str('start', message.from_user))

  text = res['hello'] + '\n\n' + '\n'.join(res['main_commands'].values())
  await message.answer(text, reply_markup=main_keyboard)


async def about(message: types.Message) -> None:
  logging.info(utils.get_log_str('about', message.from_user))

  desc = res['description']
  features = '\n'.join(res['features'].values())

  contribute = (f'{res['contribute']['_prev']}\n'
                f'{res['contribute']['desc']}\n\n'
                f'{res['contribute']['repo']}')

  text = (f'{desc}\n\n'
          f'{features}\n\n'
          f'{contribute}')

  await message.answer(text)

async def list_sections(message: types.Message) -> None:
  if not sections:
    await message.answer(f"{res['sections']['no_any']}.")

  sections_list = "\n".join(sections.keys())
  text = (f"{res['sections']['available']}:\n"
          f'{sections_list}')

  await message.answer(text)

async def list_topics(message: types.Message):
  command_parts = message.text.split()
  if len(command_parts) < 2:
    await message.answer(f"'{res['topics']['specify']}' '{res['topics']['format']}'")
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
