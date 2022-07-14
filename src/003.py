### Treasure Island ###

import sys

art = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
'''


def prompt(*args):
    text_prompt = str(args[0]).capitalize()
    for option in args[1:-1]:
        text_prompt += f", {option.lower()}"
    text_prompt += f" or {str(args[-1])}? "
    input_check = False
    while not input_check:
        user_input = input(text_prompt)
        for option in args:
            if user_input.lower() in {option.lower(), option[0].lower()}:
                input_check = True
    return user_input[0].lower()


print(art)
print("Welcome to Treasure Island. Your mission is to find the treasure.")

m = prompt("Left", "right")
if m == "r":
    print("You fall into a hole. Game over.")
    sys.exit()

m = prompt("Swim", "wait")
if m == "s":
    print("You have been attacked by trout. Game over.")
    sys.exit()

m = prompt("Blue", "yellow", "red")
if m == "b":
    print("You have been eaten by beasts. Game over.")
    sys.exit()
elif m == "r":
    print("You have died in a fire. Game over.")
    sys.exit()
elif m == "y":
    print("You win!")
