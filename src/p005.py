### Password generator ###

import random
import string

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like? "))
numbers = int(input("How many numbers would you like? "))

password = []

for n in range(letters):
    password.append(random.choice(string.ascii_letters))
for n in range(symbols):
    password.append(random.choice(string.punctuation))
for n in range(numbers):
    password.append(str(random.randint(0, 9)))
random.shuffle(password)
print(f"Here is your password: {''.join(password)}")
