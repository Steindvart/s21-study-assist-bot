from aiogram.filters.callback_data import CallbackData

# ---------------------------------------------

class TestSessionCallbacks():
  start = 'session:start'
  end = 'session:stop'
  next = 'session:next'
  new = 'session:new'


class AnswerCallbackFactory(CallbackData, prefix='answer'):
  val: str
