### Turtle racing ###

from random import randint
from turtle import Screen, Turtle


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color:"
).lower()
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

turtles = []

for i in range(7):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=(-150 + i * 50))
    turtles.append(t)

if bet:
    is_race_on = True

while is_race_on:
    for c in turtles:
        c.forward(randint(0, 10))
        if c.xcor() >= 200:
            win_color = c.color()[1].lower()
            is_race_on = False
if win_color == bet:
    print(f"You won. The {win_color} turtle was the winner.")
else:
    print(f"You lost. The {win_color} turtle was the winner.")

screen.exitonclick()
