# ISS Overhead Notifier #

import datetime as dt
import requests
import smtplib, ssl

from pprint import pprint

# from tkinter import *


# def get_quote():
#     response = requests.get("https://api.kanye.rest/")
#     canvas.itemconfig(quote_text, text=response.json()["quote"])


# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="./src/res033/background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(
#     150,
#     207,
#     text="",
#     width=250,
#     font=("Helvetica LT Std", 20, "bold"),
#     fill="white",
# )
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="./src/res033/kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)

# window.mainloop()

MY_LAT = 1.352083
MY_LONG = 103.819839
CAFILE = "./src/res033/certs.pem"

sender = "..."
password = "..."
receiver = "..."
message = """Subject:ISS overhead

Look up! The ISS is above you in the sky.
"""


def send_email():
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)


params = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=params, verify=False
)

sunrise, sunset = (
    int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0]),
    int(response.json()["results"]["sunset"].split("T")[1].split(":")[0]),
)

response = requests.get("http://api.open-notify.org/iss-now.json")
lat, long = float(response.json()["iss_position"]["latitude"]), float(
    response.json()["iss_position"]["longitude"]
)

now = dt.datetime.now()

print("Testing:", lat, long, now.hour, sunset, sunrise)

if (
    lat >= MY_LAT - 5
    and lat <= MY_LAT + 5
    and long > MY_LONG - 5
    and long < MY_LONG + 5
):
    if now.hour >= sunset or now.hour < sunrise:
        send_email()
