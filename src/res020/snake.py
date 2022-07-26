### Snake class ###

from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((i * -20, 0))

    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):
            self.segments[s].goto(
                self.segments[s - 1].xcor(), self.segments[s - 1].ycor()
            )
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        "Adds a new segment to the snake."
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
