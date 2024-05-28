import logging as log

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from models.section import Section
from models.topic import Topic

import views.telegram.sections
import views.telegram.common

from .callbacks import SectionsCallbackFactory, AnswerCallbackFactory, SectonCallbacks
from .states import FSMSection, FSMTestSession

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

  await state.update_data(section=section)
  await state.set_state(FSMSection.section_selected)


@router.callback_query(F.data == SectonCallbacks.start_testing, StateFilter(FSMSection.section_selected))
async def handle_start_testing_callback(callback: CallbackQuery, state: FSMContext):
  data = await state.get_data()
  section: Section = data.get('section')
  #IMPROVE: find better way for many args
  current_topic_indx = 0
  current_test_indx = 0
  current_test_total = 1
  await state.update_data({'current_topic_indx': current_topic_indx,
                           'current_test_indx': current_test_indx, 'current_test_total': current_test_total})

  text, keyboard = views.telegram.sections.get_body_testing_session(section, current_test_total,
                                                                    current_test_indx, current_topic_indx)

  await callback.message.edit_text(text, reply_markup=keyboard)
  await state.set_state(FSMSection.section_testing)


@router.callback_query(AnswerCallbackFactory.filter(), StateFilter(FSMSection.section_testing))
async def handle_answer_result_callback(callback: CallbackQuery, callback_data: AnswerCallbackFactory, state: FSMContext):
  data = await state.get_data()
  section: Section = data.get('section')
  current_topic_indx = data.get('current_topic_indx')
  current_test_indx = data.get('current_test_indx')
  current_test_total = data.get('current_test_total')
  answer_indx = int(callback_data.val)

  text, keyboard = views.telegram.sections.get_body_testing_session_result(section, answer_indx,
                                                                          current_test_total, current_test_indx,
                                                                          current_topic_indx)

  await callback.message.edit_text(text, reply_markup=keyboard)
  await state.set_state(FSMSection.testing_result)


@router.callback_query(F.data == SectonCallbacks.next_testing, StateFilter(FSMSection.testing_result))
async def handle_next_testing_callback(callback: CallbackQuery, state: FSMContext):
  data = await state.get_data()
  section: Section = data.get('section')

  current_topic_indx = data.get('current_topic_indx')
  topic: Topic = section.topics[current_topic_indx]

  current_test_indx = data.get('current_test_indx') + 1
  current_test_total = data.get('current_test_total') + 1

  if (current_test_indx >= topic.get_tests_quantity()):
    current_topic_indx = current_topic_indx + 1
    current_test_indx = 0

  if (current_topic_indx >= len(section.topics)):
    # state.set_state(FSMTestSession.end)
    await handle_end_testing_callback(callback, state)
    return

  await state.update_data({'current_topic_indx': current_topic_indx ,
                           'current_test_indx': current_test_indx, 'current_test_total': current_test_total})

  text, keyboard = views.telegram.sections.get_body_testing_session(section, current_test_total,
                                                                    current_test_indx, current_topic_indx)

  await callback.message.edit_text(text, reply_markup=keyboard)
  await state.set_state(FSMSection.section_testing)


async def process_start_interact(message: Message):
  text, keyboard = views.telegram.common.get_body_start_interact()
  await message.answer(text, reply_markup=keyboard)


@router.callback_query(F.data == SectonCallbacks.stop_testing)
async def handle_end_testing_callback(callback: CallbackQuery, state: FSMContext):
  await state.clear()
  await process_start_interact(callback.message)
  await callback.answer()


@router.callback_query(F.data == SectonCallbacks.back_to_select, StateFilter(FSMSection.section_selected))
async def handle_back_section_callback(callback: CallbackQuery, state: FSMContext):
  await handle_list_sections_callback(callback, state)