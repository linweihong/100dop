### Pong ###

from turtle import Screen, Turtle
from time import sleep

# Own classes : Scoreboard, paddle, ball
# Controlling paddle
# Ball behaviour
# Wall collision
# Paddle collision
# Scoring

FONT = ("Consolas", 40, "normal")


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def move_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)


class Ball(Turtle):
    def __init__(self, position):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self):
        self.x_move = -self.x_move
        self.speedup()

    def bounce_y(self):
        self.y_move = -self.y_move

    def reset_position(self):
        self.home()
        self.bounce_x()

    def speedup(self):
        self.x_move *= 1.1
        self.y_move *= 1.1

    def reset_speed(self):
        self.x_move = 10
        self.y_move = 10


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 540)
        self.paddle_0_score = 0
        self.paddle_1_score = 0
        self.update_scoreboard()

    def l_scored(self):
        self.paddle_0_score += 1
        self.update_scoreboard()

    def r_scored(self):
        self.paddle_1_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"{self.paddle_0_score} : {self.paddle_1_score}", align="center", font=FONT
        )


paddle_0 = Paddle(position=(-700, 0))
paddle_1 = Paddle(position=(700, 0))
ball = Ball(position=(0, 0))
scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1600, height=1200)
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(paddle_0.move_up, "q")
screen.onkey(paddle_0.move_down, "a")
screen.onkey(paddle_1.move_up, "y")
screen.onkey(paddle_1.move_down, "i")

game = True

while game:
    sleep(0.1)
    ball.move()
    if ball.ycor() > 580 or ball.ycor() < -580:
        ball.bounce_y()
        ball.speedup()
    if any([ball.distance(paddle_0) < 50, ball.distance(paddle_1) < 50]) and any(
        [ball.xcor() > 670, ball.xcor() < -670]
    ):
        ball.bounce_x()
    if ball.xcor() > 770:
        scoreboard.l_scored()
        ball.reset_speed()
        ball.reset_position()
    if ball.xcor() < -770:
        scoreboard.r_scored()
        ball.reset_speed()
        ball.reset_position()

    screen.update()


screen.exitonclick()
