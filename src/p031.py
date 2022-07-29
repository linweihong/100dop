### Flash Card Program ###

import json
import pandas as pd
import random
import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
IMG_FLASHCARD_FRONT = "./src/res031/card_front.png"
IMG_FLASHCARD_BACK = "./src/res031/card_back.png"
IMG_RIGHT = "./src/res031/right.png"
IMG_WRONG = "./src/res031/wrong.png"
CSV_DATA = "./src/res031/french_words.csv"
SAVE_FILE = "./src/res031/data.json"

card_timer = None
card = None
# ---------- DICTIONARY DATA

try:
    with open(SAVE_FILE) as f:
        d = json.load(f)
except FileNotFoundError:
    d = pd.read_csv(CSV_DATA).to_dict(orient="records")
if len(d) == 0:
    d = pd.read_csv(CSV_DATA).to_dict(orient="records")

# ---------- FLASHCARD LOGIC


def choose_card():
    try:
        return random.choice(d)
    except IndexError:
        root.destroy()
        raise FileNotFoundError("No more words.")


def display_card():
    global card
    card = choose_card()
    canvas.itemconfig(card_bg, image=img_flashcard_front)
    canvas.itemconfig(label_lang, text="French", fill="black")
    canvas.itemconfig(label_card, text=card["French"], fill="black")
    global card_timer
    card_timer = root.after(3000, flip_card, card["English"])


def check_pressed():
    global d
    global card
    d.remove(card)
    save_progress()
    global card_timer
    root.after_cancel(card_timer)
    display_card()


def cross_pressed():
    global card_timer
    root.after_cancel(card_timer)
    display_card()


# ---------- FLIP CARD


def flip_card(en):
    canvas.itemconfig(card_bg, image=img_flashcard_back)
    canvas.itemconfig(label_lang, text="English", fill="white")
    canvas.itemconfig(label_card, text=en, fill="white")


# ---------- SAVE PROGRESS


def save_progress():
    global d
    with open(SAVE_FILE, "w") as f:
        json.dump(d, f, sort_keys=True, indent=4)


# ---------- USER INTERFACE

root = tk.Tk()
root.title("Flashcards")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas

img_flashcard_front = tk.PhotoImage(file=IMG_FLASHCARD_FRONT)
img_flashcard_back = tk.PhotoImage(file=IMG_FLASHCARD_BACK)

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_bg = canvas.create_image(400, 263, image=img_flashcard_front)
canvas.grid(row=0, column=0, columnspan=2)

label_lang = canvas.create_text(
    400, 150, text="", font=("Helvetica LT Std", 40, "italic")
)
label_card = canvas.create_text(
    400, 263, text="", font=("Helvetica LT Std", 60, "bold")
)

# Buttons

img_wrong = tk.PhotoImage(file=IMG_WRONG)
button_cross = tk.Button(
    image=img_wrong, highlightthickness=0, command=cross_pressed, borderwidth=0
)
button_cross.grid(row=1, column=0)

img_right = tk.PhotoImage(file=IMG_RIGHT)
button_check = tk.Button(
    image=img_right, highlightthickness=0, command=check_pressed, borderwidth=0
)
button_check.grid(row=1, column=1)

display_card()

root.mainloop()
