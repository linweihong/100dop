# Open Weather API

import asyncio
import os

import requests
import telegram

T_TOKEN = os.environ.get("T_TOKEN")
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
OW_API_KEY = os.environ.get("OW_API_KEY")
SG_LON = "103.819839"
SG_LAT = "1.352083"

CHATID = os.environ.get("CHATID")

CODES = {
    "2": "storm",
    "3": "drizzle",
    "5": "rain",
}

params = {
    "lat": SG_LAT,
    "lon": SG_LON,
    "exclude": "",
    "appid": OW_API_KEY,
}


async def tbot(msg):
    bot = telegram.Bot(T_TOKEN)
    async with bot:
        await bot.send_message(
            text=msg,
            chat_id=CHATID,
        )


def check_weather():
    "Check Open Weather for the weather forecast in the next 24 hours."
    response = requests.get(ENDPOINT, params=params)
    d = response.json()["list"]
    for forecast in d[0:9]:
        if str(forecast["weather"][0]["id"])[0] in ["2", "3", "5"]:
            return (
                "Bring an umbrella. ☔ "
                f"It will {CODES[str(forecast['weather'][0]['id'])[0]]} today."
            )
    return None


r = check_weather()
if r:
    asyncio.run(tbot(r))
