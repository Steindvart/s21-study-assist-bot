from aiogram import Dispatcher
from aiogram.filters import Command

import commands as cmd


def register_commands(dp: Dispatcher) -> None:
  # TODO - composite filters in one line
  dp.message.register(cmd.start, Command(commands=['start']))
  dp.message.register(cmd.about, Command(commands=['about']))
  dp.message.register(cmd.list_sections, Command(commands=['sections']))


# def register_processors(dp: Dispatcher) -> None:
#   dp.message.register(cmd.proc_message, StateFilter(BotStatesGroup.message))
#   dp.message.register(cmd.proc_reсipient, StateFilter(BotStatesGroup.recipient))
