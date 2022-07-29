### Tip calculator ###

print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? "))
print(
    "Each person should pay: ${:.2f}".format(
        round((total * (1 + tip / 100)) / people, 2)
    )
)
