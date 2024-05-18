import logging

from aiogram import types

from section import get_sections

# DEFECT - using global objects, not good
from bot import bot, bot_config, main_keyboard
import utils

# Alliaces
res = bot_config.resources


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
  sections = get_sections()

  if not sections:
    await message.answer(f"{res['sections']['not_found']}.")

  sections_list = "\n".join([section.name for section in sections])
  text = (f"{res['sections']['available']}:\n"
          f'{sections_list}')

  await message.answer(text)