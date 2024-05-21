import logging as log
from environs import Env

env = Env()
env.read_env()

# #NOTE - configure immediately after import is IMPORTANT!
log.basicConfig(filename='app.log',
                level=log._nameToLevel[env('LOG_LEVEL')],
                format='[{asctime}] {levelname:8} {filename}: {lineno} - {name} - {message}',
                style='{'
)

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot import bot
from controllers.telegram import register_commands


# Main
if __name__ == '__main__':
  storage: MemoryStorage = MemoryStorage()
  dp: Dispatcher = Dispatcher(storage=storage)

  # bot_config.initialize_sections(content_dir)
  register_commands(dp)
  # config.register_processors(dp)

  dp.run_polling(bot)