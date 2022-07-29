### Quiz Game ###

from res017.data import question_data
from res017.question_model import Question
from res017.quiz_brain import QuizBrain

question_bank = [
    Question(question["text"], question["answer"]) for question in question_data
]

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")
