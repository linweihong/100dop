### Rock, paper, scissors ###

import random

choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
moves = {0: "rock", 1: "paper", 2: "scissors"}
print(f"You chose {moves[choice]}.")
com_choice = random.randint(0, 2)
print(f"Computer chose {moves[com_choice]}.")
if choice == com_choice:
    print("It's a draw.")
elif choice == 0:
    if com_choice == 1:
        print("You lose.")
    else:
        print("You win.")
elif choice == 1:
    if com_choice == 0:
        print("You win.")
    else:
        print("You lose.")
elif choice == 2:
    if com_choice == 0:
        print("You lose.")
    else:
        print("You win.")
