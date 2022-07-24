class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        user_answer = input(
            f"Q.{self.question_number+1}:"
            f" {self.question_list[self.question_number].text}"
            " (True/False)? "
        )
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def still_has_questions(self):
        try:
            self.question_list[self.question_number]
        except IndexError:
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Current score: {self.score}/{self.question_number+1}")
