from dataclasses import dataclass

from aiogram.fsm.state import State, StatesGroup

# ---------------------------------------------

class FSMTestSession(StatesGroup):
  session = State()
  result = State()
  end = State()


@dataclass
class TestSessionData():
  topic_indx: int = 0
  test_indx: int = 0
  test_counter: int = 1
  test_total: int = 0
  correct_answers = 0

  def update_as_next(self, tests_quantity: int):
    self.test_indx = self.test_indx + 1
    self.test_counter = self.test_counter + 1

    if (self.test_indx >= tests_quantity):
      self.topic_indx = self.topic_indx + 1
      self.test_indx = 0

  def count_correct(self):
    self.correct_answers = self.correct_answers + 1

  def is_end(self) -> bool:
    if self.test_counter >= self.test_total: return True
    else: return False