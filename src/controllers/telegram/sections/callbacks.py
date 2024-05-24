from aiogram.filters.callback_data import CallbackData

class SectionsCallbackFactory(CallbackData, prefix='section'):
  section_name: str