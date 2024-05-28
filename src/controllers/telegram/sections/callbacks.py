from enum import Enum

from aiogram.filters.callback_data import CallbackData

# ---------------------------------------------

#IMPROVE: separate callback by type
class SectonCallbacks():
  list_sections = 'call:list_sections'
  back_to_select = 'call:back_to_select'
  start_testing = 'call:start_testing'
  stop_testing = 'call:stop_testing'
  next_testing = 'call:next_testing'


class SectionsCallbackFactory(CallbackData, prefix='section'):
  section_name: str


class AnswerCallbackFactory(CallbackData, prefix='answer'):
  val: str
