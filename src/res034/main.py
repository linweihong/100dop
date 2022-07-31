import requests

from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

params = {"amount": "10", "type": "boolean"}
response = requests.get("https://opentdb.com/api.php", params=params)
question_data = response.json()["results"]

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

quiz_ui = QuizInterface(quiz)
