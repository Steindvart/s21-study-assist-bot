import config
import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot import bot
from controllers.telegram import register_commands

# ---------------------------------------------

async def main() -> None:
  storage: MemoryStorage = MemoryStorage()
  dp: Dispatcher = Dispatcher(storage=storage)

  # bot_config.initialize_sections(content_dir)
  register_commands(dp)
  # config.register_processors(dp)

  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)

asyncio.run(main())