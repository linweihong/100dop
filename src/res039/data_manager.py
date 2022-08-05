import requests

from constants import SHEETY_TOKEN


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
        self.endpoint = (
            "https://api.sheety.co/2f87d8e4e78bbb26d6fa6d49ba315e03/flights/prices"
        )

    def retrieve(self):
        r = requests.get(url=self.endpoint, headers=self.headers)
        r.raise_for_status()
        return r.json()

    def post(self, d):
        r = requests.post(url=self.endpoint, headers=self.headers, json={"price": d})
        r.raise_for_status()

    def edit(self, d, row):
        r = requests.put(
            url=self.endpoint + "/" + str(row), headers=self.headers, json=d
        )
        r.raise_for_status()
