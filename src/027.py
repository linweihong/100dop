### Mile to kilometers converter ###

import tkinter as tk

FONT = ("Fira Code", 14)


def button_click():
    output_label["text"] = int(user_input.get()) * 1.609


# Window
window = tk.Tk()
window.title("Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
user_input = tk.Entry(width=10)
user_input.focus()
user_input.grid(row=0, column=1)

# Labels
lb1 = tk.Label(text="miles", justify="left", font=FONT)
lb1.grid(row=0, column=2)

lb2 = tk.Label(text="is equal to", justify="right", font=FONT)
lb2.grid(row=1, column=0)

lb3 = tk.Label(text="km", justify="left", font=FONT)
lb3.grid(row=1, column=2)

output_label = tk.Label(text="", font=FONT)
output_label.config(padx=20, pady=20)
output_label.grid(row=1, column=1)

# Button
button = tk.Button(text="calculate", font=FONT, command=button_click)
button.grid(row=2, column=1)

# Mainloop
window.mainloop()
