import logging

from aiogram import types

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
