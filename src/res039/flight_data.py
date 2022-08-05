import requests

from constants import endpoint
from constants import flightsearch_key as f_apikey


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(
        self,
        nights_in_dst_from=7,
        nights_in_dest_to=28,
        max_stopovers=1,
        adults=2,
    ):
        self.search_endpoint = endpoint + "v2/search"
        self.headers = {"apikey": f_apikey}
        self.payload = {
            "fly_from": "SIN",
            "flight_type": "round",
            "nights_in_dst_from": nights_in_dst_from,
            "nights_in_dst_to": nights_in_dest_to,
            "max_stopovers": max_stopovers,
            "adults": adults,
            "curr": "SGD",
            "locale": "en",
        }

    def set_destination(self, des):
        self.payload["fly_to"] = des

    def set_fly_date(self, date):
        self.payload["date_from"] = date

    def set_return_date(self, date):
        self.payload["date_to"] = date

    def search_flights(self):
        r = requests.get(
            url=self.search_endpoint, headers=self.headers, params=self.payload
        )
        r.raise_for_status()
        return r.json()["data"]

    def get_cheapest_flight(self):
        try:
            d = self.search_flights()[0]
        except IndexError:
            return {
                "nights_in_dest": 0,
                "price": 0,
                "airlines": "N/A",
                "link": None,
                "flight_date": None,
                "return_date": None,
            }
        return {
            "nights_in_dest": d["nightsInDest"],
            "price": d["price"],
            "airlines": d["airlines"],
            "link": d["deep_link"],
            "flight_date": d["route"][0]["local_departure"],
            "return_date": d["route"][-1]["local_arrival"],
        }
