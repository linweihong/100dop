### Password manager ###


import tkinter as tk
import random

from string import ascii_letters, digits, punctuation
from tkinter import messagebox

FONT = ("Fira Code", 10, "normal")


# ---------------------------- PASSWORD GENERATOR --------------------- #


def generate_password():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for _ in range(nr_letters):
        password_list.append(random.choice(ascii_letters))

    for _ in range(nr_symbols):
        password_list.append(random.choice(punctuation))

    for _ in range(nr_numbers):
        password_list.append(random.choice(digits))

    random.shuffle(password_list)

    password = "".join(password_list)

    # Copy password to clipboard
    root.clipboard_clear()
    root.clipboard_append(password)

    # Insert password into app
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD -------------------------- #


def save_password():
    data = [website_entry.get(), email_entry.get(), password_entry.get()]
    if "" in set(data) or len(data) < 3:
        messagebox.showerror(
            title="Oops", message="Please make sure you have not left any fields empty."
        )
    else:
        message = (
            f"These are the details entered:\nEmail: {data[1]}\n"
            f"Password: {data[2]}\nSave these details?"
        )
        if messagebox.askokcancel(title=data[0], message=message):
            with open("./src/res029/data.txt", "a") as f:
                f.write(" | ".join(data))
                f.write("\n")
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

root = tk.Tk()
root.title("Password Manager")
root.config(padx=40, pady=40)

# Canvas
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo = tk.PhotoImage(file="./src/res029/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:", font=FONT).grid(row=1, column=0)

email_label = tk.Label(text="Email/Username:", font=FONT).grid(row=2, column=0)

password_label = tk.Label(text="Password:", font=FONT).grid(
    row=3, column=0, sticky="EW"
)


# Entries
website_entry = tk.Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = tk.Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(tk.END, "test@email.com")

password_entry = tk.Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_button = tk.Button(
    text="Generate password", font=FONT, command=generate_password
)
generate_button.grid(row=3, column=2, sticky="E")

add_button = tk.Button(text="Add", font=FONT, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


# Main loop
root.mainloop()
