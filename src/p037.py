# Habit tracker #

import datetime as dt

import requests

from constants import PIXELA_TOKEN

PXLA_USERS_EP = "https://pixe.la/v1/users"
PXLA_GRAPH_EP = PXLA_USERS_EP + "/irxs/graphs"
PXLA_CG_EP = PXLA_GRAPH_EP + "/coding"
USERNAME = "irxs"

q = input("How many hours did you code today? ")
t = input("Are you logging this after midnight? [y/n] ")
if t.lower() == "y":
    i = 1
else:
    i = 0

headers = {"X-USER-TOKEN": PIXELA_TOKEN}

payload = {
    "date": (dt.date.today() - dt.timedelta(days=i)).strftime("%Y%m%d"),
    "quantity": q,
}

# r = requests.post(PXLA_USERS_EP, json=payload)
# r = requests.post(PXLA_GRAPH_EP, json=payload, headers=headers)
r = requests.post(PXLA_CG_EP, json=payload, headers=headers)
print(r.text)
