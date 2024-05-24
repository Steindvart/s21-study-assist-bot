from config import config
import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import controllers.telegram as ct
from views.telegram import main_menu

# ---------------------------------------------

async def main() -> None:
  storage: MemoryStorage = MemoryStorage()
  dp: Dispatcher = Dispatcher(storage=storage)
  bot: Bot = Bot(config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))

  dp.include_router(ct.common_handlers.router)
  dp.include_router(ct.sections.handlers.router)
  dp.include_router(ct.other_handlers.router)

  # bot_config.initialize_sections(content_dir)

  await main_menu.set_main_menu(bot)

  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)


asyncio.run(main())