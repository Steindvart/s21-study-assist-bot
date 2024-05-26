import logging as log

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

import views.telegram.sections

from .callbacks import SectionsCallbackFactory, SectonCallbacks
from .states import FSMSection

# DEFECT: code duplicate in other scripts
from config import config

res = config.resources
sections = config.sections
router = Router()

# ---------------------------------------------

@router.callback_query(F.data == SectonCallbacks.list_sections, StateFilter(default_state))
async def handle_list_sections_callback(callback: CallbackQuery, state: FSMContext) -> None:
  if not sections:
    await callback.message.answer(f"{res['sections']['no_any']}.")
    return

  text, keyboard = views.telegram.sections.get_body_list_sections(sections)

  await callback.message.edit_text(text, reply_markup=keyboard)
  await state.set_state(FSMSection.sections_list)


@router.callback_query(SectionsCallbackFactory.filter(), StateFilter(FSMSection.sections_list))
async def handle_select_section_callback(callback: CallbackQuery, callback_data: SectionsCallbackFactory, state: FSMContext):
  section_name = callback_data.section_name
  section = sections.get(section_name)
  if not section:
    await callback.message.answer(res['sections']['not_found'] % section_name)
    return

  text, keyboard = views.telegram.sections.get_body_select_section(section)

  await callback.message.edit_text(text, reply_markup=keyboard)
  await state.set_state(FSMSection.section_selected)


@router.callback_query(F.data == SectonCallbacks.back_to_select, StateFilter(FSMSection.section_selected))
async def handle_back_section_callback(callback: CallbackQuery, state: FSMContext):
  await handle_list_sections_callback(callback, state)