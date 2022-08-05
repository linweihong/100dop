import datetime as dt

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

test_output = "./src/res039/test_data.json"

# Flight deal finder

# This file will need to use the DataManager,FlightSearch, FlightData,
#  NotificationManager classes to achieve the program requirements.

fs = FlightSearch(10)
codes = fs.fetch_codes()

fd = FlightData()
fd.set_fly_date((dt.datetime.today() + dt.timedelta(days=1)).strftime("%d/%m/%Y"))
fd.set_return_date((dt.datetime.today() + dt.timedelta(days=365)).strftime("%d/%m/%Y"))


price_list = list()
for location in codes:
    fd.set_destination(location["code"])
    print(f"Checking {location['code']} ...")
    flight = fd.get_cheapest_flight()
    location["price"] = flight["price"]
    if flight["flight_date"]:
        location["flight date"] = dt.datetime.fromisoformat(
            flight["flight_date"][:-1]
        ).strftime("%d/%m/%Y %H:%M")
    else:
        location["flight date"] = "N/A"
    if flight["return_date"]:
        location["return date"] = dt.datetime.fromisoformat(
            flight["return_date"][:-1]
        ).strftime("%d/%m/%Y %H:%M")
    else:
        location["return date"] = "N/A"
    location["link"] = flight["link"]
    price_list.append(location)

nm = NotificationManager()
dm = DataManager()
existing_data = dm.retrieve()["prices"]
for location in price_list:
    payload = {
        "city": location["city"],
        "iataCode": location["code"],
        "lowestPrice": location["price"],
        "flightDate": location["flight date"],
        "returnDate": location["return date"],
    }
    for row in existing_data:
        if location["city"] == row["city"]:
            if row["lowestPrice"] and row["lowestPrice"] > location["price"]:
                dm.edit(payload, row["id"])
                msg = (
                    f"Only S${location['price']} to fly from Singapore-SIN ",
                    f"to {location['city']}-{location['code']}, from "
                    f"{location['flight date'][:10]} to "
                    f"{location['return date'][:10]}.",
                )
                nm.send_message(msg)
            break
    else:
        dm.post(payload)
