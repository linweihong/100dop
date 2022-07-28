### NATO alphabet ###

import pandas as pd

df = pd.read_csv("./src/res026/nato_phonetic_alphabet.csv")

d = {row.letter: row.code for (index, row) in df.iterrows()}

while True:
    username = input("What is your name? ")
    try:
        print([d[c.upper()] for c in username])
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        break
