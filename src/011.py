### Blackjack capstone project ###

import os
import random
import sys

deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 4


def bust(t):
    min_score = 0
    for card in t:
        if card == "J" or card == "Q" or card == "K":
            min_score += 10
        elif card == "A":
            min_score += 1
        else:
            min_score += card
    if min_score > 21:
        return True
    return False


def score(t):
    points = 0
    aces = 0
    for card in t:
        if card == "J" or card == "Q" or card == "K":
            points += 10
        elif type(card) == int:
            points += card
        else:
            aces += 1
            points += 1
    if aces:
        if points < 12:
            points += 10
    return points


game = True
while game:
    os.system("CLS")
    cards = deck.copy()
    p_hand = []
    c_hand = []
    for _ in range(2):
        p_hand.append(cards.pop(cards.index(random.choice(cards))))
    for _ in range(2):
        c_hand.append(cards.pop(cards.index(random.choice(cards))))
    print(f"Your cards: {p_hand}")
    print(f"Computer's first card: {c_hand[0]}")
    drawing = True
    while drawing and not bust(p_hand):
        if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            p_hand.append(cards.pop(cards.index(random.choice(cards))))
            print(f"Your cards: {p_hand}")
        else:
            drawing = False
    if bust(p_hand):
        print("You're bust. You lose.")
    else:
        while score(c_hand) < 17:
            c_hand.append(cards.pop(cards.index(random.choice(cards))))
        if bust(c_hand):
            print(f"The computer's cards: {c_hand}")
            print("Computer is bust. You win!")
        elif score(p_hand) > score(c_hand):
            print(f"The computer's cards: {c_hand}")
            if score(p_hand) == 21:
                print("Blackjack!")
            print("You win!")
        elif score(p_hand) == score(c_hand):
            print(f"The computer's cards: {c_hand}")
            if score(p_hand) == 21:
                print("Blackjack! But...")
            print("It's a draw.")
        else:
            print(f"The computer's cards: {c_hand}")
            print("You lose.")
    if input("Do you want to play another game of Blackjack? Type 'y' or 'n': ") == "n":
        game = False
