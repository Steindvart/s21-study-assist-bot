from aiogram import Dispatcher, types
from aiogram.filters import Command

import logging as log
import utils

# DEFECT: code duplicate in other scripts
from config import config, main_keyboard

res = config.resources

# ---------------------------------------------

def register_common_commnads(dp: Dispatcher) -> None:
  dp.message.register(start, Command(commands=['start']))
  dp.message.register(help, Command(commands=['help']))


async def start(message: types.Message) -> None:
  log.info(utils.get_log_str('start', message.from_user))

  text = res['hello'] + '\n\n' + '\n'.join(res['main_commands'].values())
  await message.answer(text, reply_markup=main_keyboard)


async def help(message: types.Message) -> None:
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
