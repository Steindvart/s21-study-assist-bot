import logging as log
from aiogram import Dispatcher

from .common_commands import register_common_commnads
from .section_commands import register_section_commnads


def register_commands(dp: Dispatcher) -> None:
  log.info('COMMNDS')
  register_common_commnads(dp)
  register_section_commnads(dp)
