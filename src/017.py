### Quiz Game ###

from res017.data import question_data
from res017.question_model import Question

question_bank = [
    Question(question["text"], question["answer"]) for question in question_data
]

print(question_bank)