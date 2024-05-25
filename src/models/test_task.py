from typing import List, Optional
import re

# ---------------------------------------------

class TestTask:
  question: str
  answers: List[str]
  correct_answer_index: int
  explanation: Optional[str]


  def __init__(self, text: str):
    lines = text.strip().split('\n')

    self.question = TestTask.extract_question(lines)
    self.answers, self.correct_answer_index = TestTask.extract_answers(lines)
    self.explanation = TestTask.extract_explanation(lines)


  @staticmethod
  def extract_question(lines: List[str]) -> str:
    return lines[0].strip('#').strip()


  @staticmethod
  def extract_answers(lines: List[str]) -> (List[str], int):
    answers = []
    correct_answer_index = -1

    answer_pattern = re.compile(r'- \[( |x)\] (.+)')
    for i, line in enumerate(lines[1:], start=1):
      match = answer_pattern.match(line)
      if match:
        is_correct, answer_text = match.groups()
        answers.append(answer_text.strip())
        if is_correct == 'x':
          correct_answer_index = i - 1

    return answers, correct_answer_index


  @staticmethod
  def extract_explanation(lines: List[str]) -> Optional[str]:
    if '## :desc' in lines:
      i = lines.index('## :desc')
      return '\n'.join(lines[i + 1:]).strip()

    return None


  def __str__(self) -> str:
    answers_str = "\n".join(
      [f"{idx + 1}. {ans}"
        for idx, ans in enumerate(self.answers)]
    )
    explanation_str = f"\nExplanation: {self.explanation}" if self.explanation else ""
    return (f"Question: {self.question}\n"
            f"Answers:\n{answers_str}\n"
            f"Correct Answer: {self.correct_answer_index + 1}\n"
            f"{explanation_str}")


  def __repr__(self) -> str:
    return (f"TestTask(question={self.question!r}, "
            f"answers={self.answers!r}, "
            f"correct_answer_index={self.correct_answer_index!r}, "
            f"explanation={self.explanation!r})")