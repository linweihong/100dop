### Pomodoro app ###

import time
import tkinter as tk

from math import floor

# ---------------------------- CONSTANTS ------------------------------ #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "IBM Plex Mono"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.2
MARK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ---------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    title_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------ #


def start_timer():
    global reps
    reps += 1
    if reps > 8:  # Stop program
        pass
    elif reps == 8:  # Long break
        title_label.config(text="Break", fg=RED)
        countdown(int(LONG_BREAK_MIN * 60))
    elif reps % 2:  # Work
        title_label.config(text="Work", fg=GREEN)
        countdown(int(WORK_MIN * 60))
    else:  # Short break
        title_label.config(text="Break", fg=PINK)
        countdown(int(SHORT_BREAK_MIN * 60))


# ---------------------------- COUNTDOWN MECHANISM -------------------- #


def countdown(count):
    global timer
    minutes = floor(count / 60)
    seconds = count % 60
    count_str = f"{minutes:02}:{seconds:02}"
    canvas.itemconfig(timer_text, text=count_str)
    if count >= 0:
        timer = window.after(1000, countdown, int(count) - 1)
    else:
        start_timer()
        global reps
        check_label.config(text=MARK * (reps // 2))


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="./src/res028/tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=1)

start_button = tk.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_label = tk.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16))
check_label.grid(row=3, column=1)

window.mainloop()
