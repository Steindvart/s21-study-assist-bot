from aiogram.fsm.state import State, StatesGroup

# ---------------------------------------------


class FSMSection(StatesGroup):
  section_selected = State()
  section_testing = State()