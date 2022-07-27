from pathlib import Path
from turtle import Turtle

FONT = ("Consolas", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.ht()
        self.goto(0, 270)
        self.color("white")
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} High score: {self.high_score}",
            align="center",
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.refresh_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

    def get_high_score(self):
        path = Path(__file__).parent / "data.txt"
        with path.open() as f:
            if s := f.read():
                return int(s)
            else:
                return 0

    def set_high_score(self):
        path = Path(__file__).parent / "data.txt"
        with path.open("w") as f:
            f.write(str(self.high_score))
