### Secret auction program ###

import os

bids = dict()

print("Welcome to the secret auction program.")
bidding = True
while bidding:
    os.system("CLS")
    print(f"Current bids: {len(bids)}")
    bidder_name = input("What is your name? ")
    bids[int(input("What is your bid? "))] = bidder_name
    if input("Are there any other bids? (yes / no) ") == "no":
        bidding = False

os.system("CLS")
print(f"The winner is {bids[max(bids)]} with a bid of ${max(bids)}.")
