from aiogram.filters.callback_data import CallbackData

# ---------------------------------------------

class TestSessionCallbacks():
  start = 'session:start'
  stop = 'session:stop'
  next = 'session:next'


class AnswerCallbackFactory(CallbackData, prefix='answer'):
  val: str
