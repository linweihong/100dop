### Caesar Cipher ###

import string


def caesar(message, shift):
    out = ""
    for c in message:
        if not c.isalpha():
            out += c
        elif c.isupper():
            out += string.ascii_uppercase[
                (string.ascii_uppercase.index(c) + shift) % 26
            ]
        elif c.islower():
            out += string.ascii_lowercase[
                (string.ascii_lowercase.index(c) + shift) % 26
            ]
    return out


def cipher():
    mode = ""
    while mode != "encode" and mode != "decode":
        mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    out = ""
    if mode == "encode":
        out = caesar(message, shift)
        print(f"Here's the encoded result: {out}")
    elif mode == "decode":
        out = caesar(message, -shift)
        print(f"Here's the decoded result: {out}")


run = True
while run:
    cipher()
    check = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if check.lower() == "no":
        run = False
