### Password manager ###


import json
import tkinter as tk
import random

from string import ascii_letters, digits, punctuation
from tkinter import messagebox

FONT = ("Fira Code", 10, "normal")
LOGO_FILE = "./src/res030/logo.png"
OUTPUT_FILE = "./src/res030/data.json"


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
    website, email, password = (
        website_entry.get(),
        email_entry.get(),
        password_entry.get(),
    )
    if "" in (website, email, password) or None in (website, email, password):
        messagebox.showerror(
            title="Oops", message="Please make sure you have not left any fields empty."
        )
    else:
        p_dict = {
            website: {
                "email": email,
                "password": password,
            }
        }
        message = (
            f"These are the details entered:\nEmail: {email}\n"
            f"Password: {password}\nSave these details?"
        )
        if messagebox.askokcancel(title=website, message=message):
            passwords.update(p_dict)
            with open(OUTPUT_FILE, "w") as f:
                json.dump(passwords, f, sort_keys=True, indent=4)
            password_entry.delete(0, tk.END)
            website_entry.delete(0, tk.END)
            website_entry.focus()


# ---------------------------- FETCH PASSWORDS ------------------------ #

try:
    with open(OUTPUT_FILE) as f:
        passwords = json.load(f)
except FileNotFoundError:
    passwords = dict()


# ---------------------------- SEARCH --------------------------------- #


def search():
    query = website_entry.get()
    try:
        passwords[query]
    except KeyError:
        message = f"You have not saved any credentials for {query}."
    else:
        message = (
            f"Email: {passwords[query]['email']}\n"
            f"Password: {passwords[query]['password']}"
        )
        root.clipboard_clear()
        root.clipboard_append(passwords[query]["password"])
    messagebox.showinfo(title=query, message=message)


# ---------------------------- UI SETUP ------------------------------- #

root = tk.Tk()
root.title("Password Manager")
root.config(padx=40, pady=40)

# Canvas
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo = tk.PhotoImage(file=LOGO_FILE)
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
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

email_entry = tk.Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(tk.END, "test@email.com")

password_entry = tk.Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
search_button = tk.Button(text="Search", font=FONT, command=search)
search_button.grid(row=1, column=2, sticky="EW")

generate_button = tk.Button(
    text="Generate password", font=FONT, command=generate_password
)
generate_button.grid(row=3, column=2, sticky="E")

add_button = tk.Button(text="Add", font=FONT, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


# Main loop
root.mainloop()
