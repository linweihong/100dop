from turtle import Turtle

FONT = ("Consolas", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.goto(0, 270)
        self.color("white")
        self.refresh_score()

    def refresh_score(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
