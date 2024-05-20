from dataclasses import dataclass
from typing import List

import logging as log
import os


@dataclass
class Section:
  name: str
  path: str

  def __repr__(self) -> str:
    return self.name

  def get_topics(self) -> List[str]:
    topics = []
    try:
      for entry in os.listdir(self.path):
        if entry.endswith('.md'):
          topics.append(entry)
    except Exception as e:
      log.error(f"Error accessing topics in section {self.name}: {e}")
    return topics


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
