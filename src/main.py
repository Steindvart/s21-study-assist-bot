import config
import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot import bot
import controllers.telegram
import views.telegram

# ---------------------------------------------

async def main() -> None:
  storage: MemoryStorage = MemoryStorage()
  dp: Dispatcher = Dispatcher(storage=storage)

  dp.include_router(controllers.telegram.common_handlers.router)
  dp.include_router(controllers.telegram.section_handlers.router)
  dp.include_router(controllers.telegram.other_handlers.router)

  # bot_config.initialize_sections(content_dir)

  await views.telegram.main_menu.set_main_menu(bot)

  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)


asyncio.run(main())