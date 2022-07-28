### NATO alphabet ###

import pandas as pd

df = pd.read_csv("./src/res026/nato_phonetic_alphabet.csv")

d = {row.letter: row.code for (index, row) in df.iterrows()}

username = input("What is your name? ")
print([d[c.upper()] for c in username if c.isalpha()])
