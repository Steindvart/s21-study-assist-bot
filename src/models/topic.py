import logging as log

from utils import get_only_filename
from .test_task import TestTask

# ---------------------------------------------

class Topic:
  name: str
  path: str
  section_name: str
  tests: list[TestTask]


  def __init__(self, section_name: str, path: str):
    self.path = path
    self.name = get_only_filename(path)
    self.section_name = section_name
    self.tests = self._init_tests()
    log.debug(self.tests[0])


  def _init_tests(self) -> list[str]:
    try:
      with open(self.path, 'r', encoding='utf-8') as file:
        content = file.read()
        parts = content.split('---')
        return [TestTask(part.strip()) for part in parts if part.strip()]
    except FileNotFoundError:
      raise Exception(f"File not found: {self.path}")
    except Exception as e:
      raise Exception(f"Error reading file {self.path}: {e}")
