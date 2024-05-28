from aiogram.filters.callback_data import CallbackData

# ---------------------------------------------

class SectonCallbacks():
  list = 'section:list_sections'
  back_to_select = 'section:back_to_select'


class SectionsCallbackFactory(CallbackData, prefix='section'):
  section_name: str
