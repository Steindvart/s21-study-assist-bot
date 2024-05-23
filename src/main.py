from config import config
import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import controllers.telegram
import views.telegram

# ---------------------------------------------

async def main() -> None:
  storage: MemoryStorage = MemoryStorage()
  dp: Dispatcher = Dispatcher(storage=storage)
  bot: Bot = Bot(config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))

  dp.include_router(controllers.telegram.common_handlers.router)
  dp.include_router(controllers.telegram.section_handlers.router)
  dp.include_router(controllers.telegram.other_handlers.router)

  # bot_config.initialize_sections(content_dir)

  await views.telegram.main_menu.set_main_menu(bot)

  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)


asyncio.run(main())