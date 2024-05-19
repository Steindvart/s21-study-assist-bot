from dataclasses import dataclass
from typing import List

import logging
import os

@dataclass
class Section:
  name: str
  path: str

  def __repr__(self) -> str:
    return self.name

def get_sections(directory="../content") -> List[Section]:
  sections = []
  try:
    for entry in os.listdir(directory):
      entry_path = os.path.join(directory, entry)
      if os.path.isdir(entry_path):
        sections.append(Section(entry, entry_path))
  except Exception as e:
    logging.error(f"Error accessing directory {directory}: {e}")

  return sections
