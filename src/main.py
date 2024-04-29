import logging

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot import bot
import config


# Configure logging
logging.basicConfig(filename='data/app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s - %(message)s')


# Main
if __name__ == '__main__':
  storage: MemoryStorage = MemoryStorage()
  dp: Dispatcher = Dispatcher(storage=storage)

  # Commands
  # TODO - move it to separate block
  config.register_commands(dp)
  # config.register_processors(dp)

  dp.run_polling(bot)