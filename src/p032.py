# Automated birthday wisher #

import datetime as dt
import pandas as pd
import random
import smtplib
import ssl

ctx = ssl.create_default_context()

CSV_FILE = "./src/res032/birthdays.csv"
TEMPLATES_FOLDER = "./src/res032/letter_templates/"
TEMPLATES = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
quote_file = "./src/res032/quotes.txt"
password = "..."  # removed
sender = "..."  # removed
# message = """Subject:Hello

# Hello from Python.
# """


def ordinals(n):
    if n > 3 and n < 21:
        return str(n) + "th"
    elif str(n)[-1] == "1":
        return str(n) + "st"
    elif str(n)[-1] == "2":
        return str(n) + "nd"
    elif str(n)[-1] == "3":
        return str(n) + "rd"
    else:
        return str(n) + "th"


def send_email(receiver, message):
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)


# with open(quote_file) as f:
#     quotes = [line.strip() for line in f.readlines()]

# if dt.datetime.now().weekday() == 0:
#     message = f"""Subject:Motivational Mondays

#     {random.choice(quotes)}"""
#     send_email(message)

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# Done

# 2. Check if today matches a birthday in the birthdays.csv

# NOTE: Possibly more efficient to check current date against df instead of iterating
# over df

df = pd.read_csv(CSV_FILE)
now = dt.datetime.now()

for (index, row) in df.iterrows():
    if row.month == now.month and row.day == now.day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the
        # [NAME] with the person's actual name from birthdays.csv
        with open("".join([TEMPLATES_FOLDER, random.choice(TEMPLATES)])) as f:
            message = [line.replace("[NAME]", row["name"]) for line in f.readlines()]
        message = (
            f"Subject:Happy {ordinals(now.year - row.year)} birthday {row['name']}!\n\n"
            + "".join(message)
        )
        # 4. Send the letter generated in step 3 to that person's email address.
        send_email(row.email, message)
