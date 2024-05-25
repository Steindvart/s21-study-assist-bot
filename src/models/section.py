from dataclasses import dataclass
from typing import List

import logging as log
import os

from .topic import Topic

# ---------------------------------------------

class Section:
  name: str
  path: str
  topics: list[Topic]

  def __init__(self, name: str, path: str):
    self.name = name
    self.path = os.path.normpath(path)
    self.topics = self._init_topics()


  def _init_topics(self) -> list[Topic]:
    topics = []
    try:
      for entry in os.listdir(self.path):
        if entry.endswith('.md'):
          topics.append(Topic(self.name, os.path.join(self.path, entry)))
    except Exception as e:
      log.error(f"Error accessing topics in section {self.name}: {e}")
    return topics


  def __repr__(self) -> str:
    return self.name


def get_sections(directory: str) -> List[Section]:
  sections = []
  try:
    for entry in os.listdir(directory):
      entry_path = os.path.join(directory, entry)
      if os.path.isdir(entry_path):
        sections.append(Section(entry, entry_path))
  except Exception as e:
    log.error(f"Error accessing directory {directory}: {e}")

  return sections
