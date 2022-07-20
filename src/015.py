### Coffee machine ###

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


def report(d):
    print(f"Water: {d['water']}ml")
    print(f"Milk: {d['milk']}ml")
    print(f"Coffee: {d['coffee']}g")
    print(f"Money: ${d['money']/100:.2f}")


def check(d, o):
    for k in o["ingredients"]:
        if o["ingredients"][k] > d[k]:
            print(f"Sorry, there is not enough {k}.")
            return False
    return True


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        break
    elif choice == "report":
        report(resources)
    else:
        order = MENU[choice]
        if check(resources, order):
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            cash = quarters * 25 + dimes * 10 + nickles * 5 + pennies
            if cash < order["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                for k in order["ingredients"]:
                    resources[k] -= order["ingredients"][k]
                resources["money"] += order["cost"]
                refund = cash - order["cost"]
                print(f"Here is ${refund/100:.2f} in change.")
                print(f"Here is your {choice} ☕. Enjoy!")
