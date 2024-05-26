from enum import Enum

from aiogram.filters.callback_data import CallbackData

class SectionsCallbackFactory(CallbackData, prefix='section'):
  section_name: str


class SectonCallbacks():
  list_sections = 'call:list_sections'
  start_testing = 'call:start_testing'
  back_to_select = 'call:back_to_select'
