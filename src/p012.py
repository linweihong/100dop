### Number Guessing Game ###

import random
import sys


answer = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
    attempts = 10
else:
    attempts = 5

guess = None
while guess != answer and attempts > 0:
    if attempts > 1:
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        print(f"You have {attempts} attempt remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == answer:
        print("You got it!")
        sys.exit()
    elif guess > answer:
        print("Too high.")
        attempts -= 1
    elif guess < answer:
        print("Too low.")
        attempts -= 1
if not attempts:
    print(f"Out of attempts. You've failed. The answer was {answer}.")
