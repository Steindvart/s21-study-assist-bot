from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from controllers.telegram.test_session.callbacks import TestSessionCallbacks, AnswerCallbackFactory
from controllers.telegram.test_session.states import TestSessionData

from models.section import Section
from models.topic import Topic
from models.test_task import TestTask

from config import config
res = config.resources

# ---------------------------------------------

def get_test_answers_str(test: TestTask, mark_right=False) -> str:
  answers_str = "\n".join(
    [f"{'✅' if mark_right and idx == test.correct_answer_index else '🔻' if mark_right else ''} {idx + 1}. {ans}"
      for idx, ans in enumerate(test.answers)]
  )
  return answers_str


def get_session_keyboard(task: TestTask, with_answers=True, with_actions=False, is_end=False) -> InlineKeyboardMarkup:
  answers_btns: list[InlineKeyboardButton] = []
  if (with_answers):
    for i in range(len(task.answers)):
      answers_btns.append(InlineKeyboardButton(text=str(i + 1), callback_data=AnswerCallbackFactory(val=str(i)).pack()))

  action_btns: list[InlineKeyboardButton] = []
  if (with_actions):
    action_btns.append(InlineKeyboardButton(text=res['testing']['stop'], callback_data=TestSessionCallbacks.end))
    if (not is_end):
      action_btns.append( InlineKeyboardButton(text=res['testing']['next'], callback_data=TestSessionCallbacks.next))

  keyboard = InlineKeyboardBuilder([answers_btns, action_btns])

  return keyboard.as_markup()


def get_body_session(section: Section, session_data: TestSessionData) -> (str, InlineKeyboardMarkup):
  topic: Topic = section.topics[session_data.topic_indx]
  test: TestTask = topic.tests[session_data.test_indx]

  test_text = (f"*{test.question}*\n\n"
               f"{get_test_answers_str(test)}")

  text = (f'{res['testing']['test_counter'] % (session_data.test_counter, section.get_tests_quantity())}\n'
          f'{res['topics']['topic']}: {topic.name}\n\n'
          f'{test_text}')

  keyboard = get_session_keyboard(test)

  return (text, keyboard)


def get_body_session_result(section: Section, session_data: TestSessionData, answer_indx: int) -> (str, InlineKeyboardMarkup):
  topic: Topic = section.topics[session_data.topic_indx]
  test: TestTask = topic.tests[session_data.test_indx]

  result_text = f'🟢 {res['testing']['right']}' if (answer_indx == test.correct_answer_index) else f'🔴 {res['testing']['wrong']}'
  explanation_text = (f"`----------------------------------`\n\n"
                      f"{test.explanation}")

  test_text = (f"*{test.question}*\n\n"
              f"{get_test_answers_str(test, True)}\n\n"
              f"{explanation_text if test.explanation else ''}")

  text = (f'{res['testing']['test_counter'] % (session_data.test_counter, session_data.test_total)}\n'
          f'{res['topics']['topic']}: {topic.name}\n\n'
          f'{res['testing']['your_answ']}: {answer_indx+1}. *{result_text}*!\n\n'
          f'{test_text}')

  keyboard = get_session_keyboard(test, False, True, session_data.is_end())

  return (text, keyboard)


def get_new_session_keyboard() -> InlineKeyboardMarkup:
  keyboard = InlineKeyboardBuilder([
    [InlineKeyboardButton(text=res['testing']['new'], callback_data=TestSessionCallbacks.new)]
  ])

  return keyboard.as_markup()


def get_body_session_end(section: Section, session_data: TestSessionData) -> (str, InlineKeyboardMarkup):
  if session_data.test_total == 0:
    percentage = 0
  else:
    percentage = (session_data.correct_answers / session_data.test_total) * 100

  if percentage <= 40:
    emoji = "🔴"
  elif 41 <= percentage <= 70:
    emoji = "🟡"
  else:
    emoji = "🟢"

  text = (f'✨ *{res['testing']['result']}*\n\n'
          f'📂 {res['sections']['section']}: *{section.name}*\n'
          f'📝 {res['testing']['test_counter_result'] % (session_data.test_counter, session_data.test_total)}\n\n'
          f'{res['testing']['correct_answ']}: *{session_data.correct_answers}*\n'
          f'{res["testing"]["successfully"]}: {emoji} *{percentage:.2f}%*')

  keyboard = get_new_session_keyboard()

  return (text, keyboard)
