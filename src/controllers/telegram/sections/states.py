from aiogram.fsm.state import State, StatesGroup

# ---------------------------------------------

class FSMSection(StatesGroup):
  sections_list = State()
  section_selected = State()
  section_testing = State()
  testing_result = State()


class FSMTestSession(StatesGroup):
  test = State()
  result = State()
  end = State()


# #TODO: use for improve data exchange in handlers
class FSMTestSessionData():
  topic_indx: int = 0
  test_indx: int = 0
  test_total: int = 0