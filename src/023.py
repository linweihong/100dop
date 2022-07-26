### Turtle crossing ###

from time import sleep
from turtle import Screen, Turtle
import random

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
MOVE_INCREMENT = 10
FINISH_LINE_Y = 280
FONT = ("Consolas", 24, "normal")
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.seth(90)
        self.penup()
        self.speed(0)
        self.reset_position()

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 10) < 3:
            new_car = Car()
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


class Car(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.speed(0)
        self.car_speed = 10
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.reset_position()

    def reset_position(self):
        self.goto(340, random.choice(range(-250, 260, 20)))


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.goto(-280, 260)
        self.level = 1
        self.color("black")
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.home()
        self.write("Game over", align="center", font=FONT)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")

game = True

while game:
    sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            scoreboard.game_over()
            game = False
    if player.ycor() > FINISH_LINE_Y:
        car_manager.level_up()
        scoreboard.level_up()
        player.reset_position()
    screen.update()

screen.exitonclick()
