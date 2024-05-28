import logging as log

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, Message, LinkPreviewOptions
from aiogram.fsm.context import FSMContext

from models.section import Section
from models.topic import Topic
from models.test_task import TestTask

import views.telegram.test_session
import views.telegram.common

from controllers.telegram.sections.states import FSMSection
from .callbacks import TestSessionCallbacks, AnswerCallbackFactory
from .states import FSMTestSession, TestSessionData

# DEFECT: code duplicate in other scripts
from config import config

res = config.resources
router = Router()

# ---------------------------------------------

@router.callback_query(F.data == TestSessionCallbacks.start, StateFilter(FSMSection.selected))
async def handle_start_test_session_callback(callback: CallbackQuery, state: FSMContext):
  data = await state.get_data()
  section: Section = data.get('section')
  session_data: TestSessionData = TestSessionData()
  await state.update_data({'session_data': session_data})

  text, keyboard = views.telegram.test_session.get_body_session(section, session_data)

  await callback.message.edit_text(text, reply_markup=keyboard)
  await state.set_state(FSMTestSession.session)


@router.callback_query(AnswerCallbackFactory.filter(), StateFilter(FSMTestSession.session))
async def handle_answer_test_session_callback(callback: CallbackQuery, callback_data: AnswerCallbackFactory, state: FSMContext):
  data = await state.get_data()
  section: Section = data.get('section')
  session_data: TestSessionData = data.get('session_data')

  answer_indx = int(callback_data.val)
  topic: Topic = section.topics[session_data.topic_indx]
  test: TestTask = topic.tests[session_data.test_indx]

  if (answer_indx == test.correct_answer_index):
    session_data.count_correct()
    await state.update_data({'session_data': session_data})

  text, keyboard = views.telegram.test_session.get_body_session_result(section, session_data, answer_indx)

  await callback.message.edit_text(text, reply_markup=keyboard, link_preview_options=LinkPreviewOptions(is_disabled=True))
  await state.set_state(FSMTestSession.result)


@router.callback_query(F.data == TestSessionCallbacks.next, StateFilter(FSMTestSession.result))
async def handle_next_test_callback(callback: CallbackQuery, state: FSMContext):
  data = await state.get_data()
  section: Section = data.get('section')
  session_data: TestSessionData = data.get('session_data')

  topic: Topic = section.topics[session_data.topic_indx]
  session_data.update_as_next(topic.get_tests_quantity())

  if (session_data.topic_indx >= len(section.topics)):
    # state.set_state(FSMTestSession.end)
    await handle_end_test_session_callback(callback, state)
    return

  await state.update_data({'session_data': session_data})

  text, keyboard = views.telegram.test_session.get_body_session(section, session_data)

  await callback.message.edit_text(text, reply_markup=keyboard)
  await state.set_state(FSMTestSession.session)


async def process_start_interact(message: Message):
  text, keyboard = views.telegram.common.get_body_start_interact()
  await message.answer(text, reply_markup=keyboard)


@router.callback_query(F.data == TestSessionCallbacks.stop)
async def handle_end_test_session_callback(callback: CallbackQuery, state: FSMContext):
  await state.clear()
  await process_start_interact(callback.message)
  await callback.answer()
