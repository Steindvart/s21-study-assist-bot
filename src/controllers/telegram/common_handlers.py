from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

import logging as log
import utils
import views.telegram.common

# DEFECT: code duplicate in other scripts
from config import config

res = config.resources
router = Router()

# ---------------------------------------------

async def process_start(message: types.Message):
  text = views.telegram.common.get_text_start_message()
  await message.answer(text)


async def process_start_interact(message: types.Message):
  text, keyboard = views.telegram.common.get_body_start_interact()
  await message.answer(text, reply_markup=keyboard)


@router.message(CommandStart())
async def handle_start_command(message: types.Message) -> None:
  log.info(utils.get_log_str('start', message.from_user))

  await process_start(message)
  await process_start_interact(message)


@router.message(Command(commands='cancel'))
async def handle_cancel_command(message: types.Message, state: FSMContext) -> None:
  log.info(utils.get_log_str('cancel', message.from_user))

  await state.clear()
  await process_start_interact(message)


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
