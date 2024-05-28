from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from controllers.telegram.sections.callbacks import SectionsCallbackFactory, SectonCallbacks, AnswerCallbackFactory

from models.section import Section
from models.topic import Topic
from models.test_task import TestTask

from config import config
res = config.resources

# ---------------------------------------------

def select_section_keyboard(sections: list[str]) -> InlineKeyboardMarkup:
  keyboard = InlineKeyboardBuilder()
  for section_name in sections:
    keyboard.button(text=section_name, callback_data=SectionsCallbackFactory(section_name=section_name))

  return keyboard.as_markup()


def get_interactive_section_keyboard() -> InlineKeyboardMarkup:
  keyboard = InlineKeyboardBuilder([
    [InlineKeyboardButton(text=res['testing']['start'], callback_data=SectonCallbacks.start_testing)],
    [InlineKeyboardButton(text=res['sections']['back_to_select'], callback_data=SectonCallbacks.back_to_select)]
  ])

  return keyboard.as_markup()


def get_body_list_sections(sections: dict) -> (str, InlineKeyboardMarkup):
  sections_list: str = "\n- ".join(sections.keys())
  text = (f"{res['sections']['available']}:\n"
          f'- {sections_list}')

  keyboard = select_section_keyboard(sections.keys())

  return (text, keyboard)


def get_body_select_section(section: Section) -> (str, InlineKeyboardMarkup):
  text = (f'📂 {res['sections']['section']}: *{section.name}*\n'
          f'📝 {res['sections']['tests_quantity']}: {section.get_tests_quantity()}\n\n'
          f'📚 {res['sections']['topics']}:\n- {"\n- ".join([str(topic) for topic in section.topics])}')

  keyboard = get_interactive_section_keyboard()

  return (text, keyboard)

def get_testing_session_keyboard(task: TestTask, with_action=False) -> InlineKeyboardMarkup:
  answers_btns: list[InlineKeyboardButton] = []
  for i in range(len(task.answers)):
    answers_btns.append(InlineKeyboardButton(text=str(i + 1), callback_data=AnswerCallbackFactory(val=str(i)).pack()))

  action_btns: list[InlineKeyboardButton] = []
  if (with_action):
    action_btns = [
      InlineKeyboardButton(text=res['testing']['stop'], callback_data=SectonCallbacks.stop_testing),
      InlineKeyboardButton(text=res['testing']['next'], callback_data=SectonCallbacks.next_testing)
    ]

  keyboard = InlineKeyboardBuilder([answers_btns, action_btns])

  return keyboard.as_markup()


def get_body_testing_session(section: Section, current_test_total: int, current_test: int, current_topic: int) -> (str, InlineKeyboardMarkup):
  topic: Topic = section.topics[current_topic]
  test: TestTask = topic.tests[current_test]

  text = (f'{res['testing']['question_counter'] % (current_test_total, section.get_tests_quantity())}\n'
          f'{res['topics']['topic']}: {topic.name}\n\n'
          f'{test.get_str_for_message()}')

  keyboard = get_testing_session_keyboard(section.topics[current_topic].tests[current_test])

  return (text, keyboard)


#IMPROVE: better args for func
def get_body_testing_session_result(section: Section, answer_indx: int,
                                    current_test_total: int, current_test: int, current_topic: int) -> (str, InlineKeyboardMarkup):
  topic: Topic = section.topics[current_topic]
  test: TestTask = topic.tests[current_test]

  result = f'🟢 {res['testing']['right']}' if (answer_indx == test.correct_answer_index) else f'🔴 {res['testing']['wrong']}'

  text = (f'{res['testing']['question_counter'] % (current_test_total, section.get_tests_quantity())}\n'
          f'{res['topics']['topic']}: {topic.name}\n\n'
          f'{res['testing']['your_answ']}: {answer_indx+1}. *{result}*!\n\n'
          f'{test.get_str_for_message(True, True)}')

  keyboard = get_testing_session_keyboard(section.topics[current_topic].tests[current_test], True)

  return (text, keyboard)