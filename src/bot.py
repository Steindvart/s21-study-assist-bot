from aiogram import Bot

from config import config

# ---------------------------------------------

bot: Bot = Bot(config.bot_token, parse_mode="Markdown")
