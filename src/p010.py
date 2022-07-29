### Calculator ###

import os


def n_add(a, b):
    return a + b


def n_subtract(a, b):
    return a - b


def n_multiply(a, b):
    return a * b


def n_divide(a, b):
    return a / b


operators = {"+": n_add, "-": n_subtract, "*": n_multiply, "/": n_divide}
mem = None

while True:
    os.system("CLS")
    if mem == None:
        mem = float(input("What's the first number? "))
    for op in operators:
        print(op)
    operator = input("Pick an operation: ")
    n2 = float(input("What's the next number? "))
    ans = operators[operator](mem, n2)
    print(f"{mem} {operator} {n2} = {ans}")
    if (
        input(
            f"Type 'y' to continue calculating with {ans},"
            "or type 'n' to start a new calculation: "
        )
        == "n"
    ):
        mem = None
    else:
        mem = ans
