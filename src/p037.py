# Habit tracker #

from datetime import date

import requests

from constants import PIXELA_TOKEN

PXLA_USERS_EP = "https://pixe.la/v1/users"
PXLA_GRAPH_EP = PXLA_USERS_EP + "/weihong/graphs"
PXLA_CG_EP = PXLA_GRAPH_EP + "/codinggraph"
USERNAME = "irxs"

q = input("How many hours did you code today? ")

headers = {"X-USER-TOKEN": PIXELA_TOKEN}

payload = {
    "date": date.today().strftime("%Y%m%d"),
    "quantity": q,
}

# r = requests.post(PXLA_USERS_EP, json=payload)
# r = requests.post(PXLA_GRAPH_EP, json=payload, headers=headers)
r = requests.post(PXLA_CG_EP, json=payload, headers=headers)
