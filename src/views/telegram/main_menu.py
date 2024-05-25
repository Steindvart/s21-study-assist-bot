from aiogram import Bot
from aiogram.types import BotCommand

from config import config

res = config.resources

# ---------------------------------------------


async def set_main_menu(bot: Bot):
  main_menu_commands = [
    BotCommand(
      command=command,
      description=description
    ) for command, description in res['main_commands'].items() if command != '_prev'
  ]

  await bot.set_my_commands(main_menu_commands)