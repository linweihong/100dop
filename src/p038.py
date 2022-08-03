# Workout tracking

import datetime as dt

import requests

from constants import NUTRITIONIX_APPID, NUTRITIONIX_TOKEN, SHEETY_TOKEN

ntx_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_get_endpoint = (
    "https://api.sheety.co/2f87d8e4e78bbb26d6fa6d49ba315e03/angela'sWorkouts/workouts"
)
sheety_post_endpoint = (
    "https://api.sheety.co/2f87d8e4e78bbb26d6fa6d49ba315e03/angela'sWorkouts/workouts"
)

ntx_headers = {
    "x-app-id": NUTRITIONIX_APPID,
    "x-app-key": NUTRITIONIX_TOKEN,
}

ntx_payload = {
    "query": "climbed 5 routes at 12pm and swam 3 km at 9pm",
    "gender": "male",
    "weight_kg": 71,
    "height_cm": 180,
    "age": 35,
}

sty_headers = {"Authorization": "Bearer " + SHEETY_TOKEN}

r = requests.post(url=ntx_endpoint, headers=ntx_headers, json=ntx_payload)
exercises = r.json()["exercises"]

for exercise in exercises:
    sty_payload = {
        "workout": {
            "date": dt.date.today().strftime("%d-%m-%Y"),
            "time": dt.datetime.now().strftime("%H:%M"),
            "exercise": exercise["name"].capitalize(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    p = requests.post(
        url=sheety_post_endpoint,
        headers=sty_headers,
        json=sty_payload,
    )
