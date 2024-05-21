from aiogram import Bot

from environs import Env

# ---------------------------------------------

env = Env()
env.read_env()

bot: Bot = Bot(env("BOT_TOKEN"), parse_mode="Markdown")
