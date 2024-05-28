from dataclasses import dataclass

from aiogram.fsm.state import State, StatesGroup

# ---------------------------------------------

class FSMTestSession(StatesGroup):
  session = State()
  result = State()
  end = State()


# #TODO: use for improve data exchange in handlers
@dataclass
class TestSessionData():
  topic_indx: int = 0
  test_indx: int = 0
  test_total: int = 1

  def update_as_next(self, tests_quantity: int):
    self.test_indx = self.test_indx + 1
    self.test_total = self.test_total + 1

    if (self.test_indx >= tests_quantity):
      self.topic_indx = self.topic_indx + 1
      self.test_indx = 0
