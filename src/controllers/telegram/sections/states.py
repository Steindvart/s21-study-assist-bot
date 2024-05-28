from aiogram.fsm.state import State, StatesGroup

# ---------------------------------------------

class FSMSection(StatesGroup):
  list = State()
  selected = State()
