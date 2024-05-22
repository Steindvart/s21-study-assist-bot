from aiogram import Router, types
from aiogram.filters import Command, CommandStart

import logging as log
import utils

# DEFECT: code duplicate in other scripts
from config import config, main_keyboard

res = config.resources
router = Router()

# ---------------------------------------------


@router.message(CommandStart())
async def process_start_command(message: types.Message) -> None:
  log.info(utils.get_log_str('start', message.from_user))

  text = res['hello'] + '\n\n' + '\n'.join(res['main_commands'].values())
  await message.answer(text, reply_markup=main_keyboard)


@router.message(Command(commands='help'))
async def process_help_command(message: types.Message) -> None:
  log.info(utils.get_log_str('help', message.from_user))

  desc = res['description']
  features = '\n'.join(res['features'].values())

  contribute = (f'{res['contribute']['_prev']}\n'
                f'{res['contribute']['desc']}\n\n'
                f'{res['contribute']['repo']}')

  text = (f'{desc}\n\n'
          f'{features}\n\n'
          f'{contribute}')

  await message.answer(text)
