import config

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot import bot
from controllers.telegram import register_commands

# ---------------------------------------------

# Main
if __name__ == '__main__':
  storage: MemoryStorage = MemoryStorage()
  dp: Dispatcher = Dispatcher(storage=storage)

  # bot_config.initialize_sections(content_dir)
  register_commands(dp)
  # config.register_processors(dp)

  dp.run_polling(bot)