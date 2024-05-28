from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext

import logging as log
import utils
import views.telegram.common

from .test_session.callbacks import TestSessionCallbacks
from .test_session.states import FSMTestSession

# DEFECT: code duplicate in other scripts
from config import config

res = config.resources
router = Router()

# ---------------------------------------------

async def process_start(message: Message):
  text = views.telegram.common.get_text_start_message()
  await message.answer(text)


async def process_start_interact(message: Message):
  text, keyboard = views.telegram.common.get_body_start_interact()
  await message.answer(text, reply_markup=keyboard)


@router.message(CommandStart())
async def handle_start_command(message: Message) -> None:
  log.info(utils.get_log_str('start', message.from_user))

  await process_start(message)
  await process_start_interact(message)


@router.message(Command(commands='new'))
async def handle_new_command(message: Message, state: FSMContext) -> None:
  log.info(utils.get_log_str('new', message.from_user))

  await state.clear()
  await process_start_interact(message)


@router.callback_query(F.data == TestSessionCallbacks.new, StateFilter(FSMTestSession.end))
async def handle_new_callback(callback: CallbackQuery, state: FSMContext):
  await callback.answer()
  await handle_new_command(callback.message, state)


@router.message(Command(commands='help'))
async def process_help_command(message: Message) -> None:
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
