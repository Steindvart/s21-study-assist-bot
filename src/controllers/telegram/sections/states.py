from aiogram.fsm.state import State, StatesGroup

# ---------------------------------------------

class FSMSection(StatesGroup):
  sections_list = State()
  section_selected = State()
  section_testing = State()