### US States Game ###


import pandas as pd
import turtle

IMAGE = "./src/res025/blank_states_img.gif"
CSV = "./src/res025/50_states.csv"
CSV_OUT = "./src/res025/states_to_learn.csv"
FONT = ("Arial", 8, "normal")

# def get_mouse_click_coor(x, y):
#     print(x, y)


class Labeller(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()

    def label(self, state):
        x, y = (
            int(df[df.state == state].x),
            int(df[df.state == state].y),
        )
        self.goto(x, y)
        self.write(state, align="center", font=FONT)


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
screen.setup(width=725, height=491)

turtle.shape(IMAGE)
labeller = Labeller()

# turtle.onscreenclick(get_mouse_click_coor)

df = pd.read_csv(CSV)

guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput("Guess the State", "What's another state's name?")
    if not answer:
        pass
    elif answer.lower() == "exit":
        break
    else:
        for row in df["state"]:
            if answer.title() == row:
                if row not in guessed_states:
                    guessed_states.append(row)
                    # implement Turtle
                    labeller.label(row)

print(f"You guessed {len(guessed_states)} out of 50 states.")

# states_to_learn.csv

missed_states = [row for row in df.state if row not in guessed_states]
pd.DataFrame(missed_states).to_csv(CSV_OUT)
