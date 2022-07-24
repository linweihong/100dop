### Hirst Painting ###

from turtle import Screen, Turtle
import colorgram
import random

t = Turtle()
screen = Screen()

# Draw a square
# for _ in range(4):
#     t.forward(100)
#     t.rt(90)

# Draw a dashed line
# for _ in range(50):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()

# Drawing different shapes
# screen.colormode(255)
# for i in range(3, 11):
#     t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     for _ in range(i):
#         t.forward(100)
#         t.rt(360 / i)

# Random walk
# screen.colormode(255)
# headings = [0, 90, 180, 270]
# t.pensize(15)
# t.speed(0)
# for _ in range(200):
#     t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     t.seth(random.choice(headings))
#     t.forward(30)

# Draw a spirograph
# screen.colormode(255)
# t.speed(0)
# circles = 50
# for i in range(circles):
#     t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     t.circle(100)
#     t.left(360 / circles)

colors = [
    (c.rgb.r, c.rgb.g, c.rgb.b)
    for c in colorgram.extract(".\\src\\res018\\image.jpg", 10)
]
screen.colormode(255)
t.speed(0)
t.pensize(20)
t.penup()
canvas = 20
spacing = 50
t.seth(180)
t.forward((canvas * spacing) / 2)
t.left(90)
t.forward((canvas * spacing) / 2)
t.seth(0)
for _ in range(canvas):
    for _ in range(canvas):
        t.dot(20, random.choice(colors))
        t.forward(spacing)
    t.left(180)
    t.forward(spacing * canvas)
    t.right(90)
    t.forward(spacing)
    t.right(90)


screen.exitonclick()
