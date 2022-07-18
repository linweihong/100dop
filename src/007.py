### Hangman ###

import os
import random

stages = [
    """+---+
|   |
|
|
|
|
======""",
    """+---+
|   |
|   0
|
|
|
======""",
    """+---+
|   |
|   0
|   |
|
|
======""",
    """+---+
|   |
|   0
|  /|
|
|
======""",
    """+---+
|   |
|   0
|  /|\\
|
|
======""",
    """+---+
|   |
|   0
|  /|\\
|  /
|
======""",
    """+---+
|   |
|   0
|  /|\\
|  / \\
|
======""",
]

word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)

guesses = []
guessed = False
life = 0
while not guessed and life != 6:
    if guesses:
        guesses.sort()
        print("Guesses: " + " ".join(c.upper() for c in guesses))
    guess = input("Guess a letter: ").lower()
    os.system("CLS")
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid guess.")
    elif guess in guesses:
        print("You've already guessed that letter.")
    else:
        guesses.append(guess)
        if guess in set(word):
            pass
        else:
            life += 1
    print(stages[life])
    print(" ".join(c.upper() if c in guesses else "_" for c in word))
    if all(c in guesses for c in set(word)):
        guessed = True

if guessed:
    print("You win.")
if life == 6:
    print(f"You lose. The answer was {word.upper()}.")
