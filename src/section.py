import logging
import os

class Section:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

def get_sections(directory="../content"):
  sections = []
  try:
    for entry in os.listdir(directory):
      entry_path = os.path.join(directory, entry)
      if os.path.isdir(entry_path):
        sections.append(Section(entry))
  except Exception as e:
    logging.error(f"Error accessing directory {directory}: {e}")

  return sections
