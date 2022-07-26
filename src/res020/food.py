from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(
            random.choice(range(-260, 280, 20)), random.choice(range(-260, 280, 20))
        )
