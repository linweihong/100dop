import json

import requests

from constants import endpoint
from constants import flightsearch_key as f_apikey


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, limit=200):
        self.dump_endpoint = endpoint + "locations/dump"
        self.headers = {"apikey": f_apikey}
        self.dump_payload = {
            "locale": "en-US",
            "location_types": "city",
            "limit": limit,
            "sort": "rank",
        }

    def get_dump(self):
        r = requests.get(
            url=self.dump_endpoint, headers=self.headers, params=self.dump_payload
        )
        r.raise_for_status()
        return r.json()["locations"]

    def fetch_codes(self):
        d = self.get_dump()
        codes = []
        for location in d:
            codes.append({"city": location["name"], "code": location["code"]})
        # with open("./src/res039/test_data.json", "w") as f:
        #     json.dump(codes, f, indent=2)
        return codes
