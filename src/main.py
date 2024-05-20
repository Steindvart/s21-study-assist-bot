import logging as log

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot import bot
from controllers.telegram import register_commands


# Configure logging
log.basicConfig(filename='data/app.log', level=log.INFO,
                    format='%(asctime)s %(levelname)s %(name)s - %(message)s')


# Main
if __name__ == '__main__':
  storage: MemoryStorage = MemoryStorage()
  dp: Dispatcher = Dispatcher(storage=storage)


  # bot_config.initialize_sections(content_dir)
  register_commands(dp)
  # config.register_processors(dp)

  dp.run_polling(bot)