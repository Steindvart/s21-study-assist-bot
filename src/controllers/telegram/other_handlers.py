from aiogram import Router
from aiogram.types import Message

# DEFECT: code duplicate in other scripts
from config import config

res = config.resources
sections = config.sections
router = Router()

# ---------------------------------------------


@router.message()
async def process_unknown_message(message: Message):
  text = (f'{res['unknown']}\n\n'
          f'{'\n'.join(res['main_commands'].values())}')
  await message.answer(text)