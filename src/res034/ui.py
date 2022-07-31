import tkinter as tk

from quiz_brain import QuizBrain

IMG_TRUE_FILE = "./src/res034/images/true.png"
IMG_FALSE_FILE = "./src/res034/images/false.png"
THEME_COLOR = "#375362"
FONT = "Helvetica LT Std"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.root = tk.Tk()
        self.root.title("Quizzler")
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = tk.Label(
            text=f"Score: {self.quiz.score}",
            font=(FONT, 16),
            fg="white",
            bg=THEME_COLOR,
        )
        self.score_text.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            font=(FONT, 20, "italic"),
        )
        self.canvas.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=50,
        )
        self.get_next_question()

        self.img_true = tk.PhotoImage(file=IMG_TRUE_FILE)
        self.button_true = tk.Button(
            image=self.img_true,
            highlightthickness=0,
            command=lambda: self.check_answer("true"),
        )
        self.button_true.grid(row=2, column=0)

        self.img_false = tk.PhotoImage(file=IMG_FALSE_FILE)
        self.button_false = tk.Button(
            image=self.img_false,
            highlightthickness=0,
            command=lambda: self.check_answer("false"),
        )
        self.button_false.grid(row=2, column=1)

        self.root.mainloop()

    def check_answer(self, answer):
        "Checks the user's answer based on user input."
        self.give_feedback(self.quiz.check_answer(answer))
        self.score_text.config(text=f"Score: {self.quiz.score}")

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz."
            )
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.get_next_question)
