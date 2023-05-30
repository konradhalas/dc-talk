from dataclasses import asdict

import dacite
import requests

from examples.ex3 import FlightsAPIFilters
from examples.ex6 import FlightSearchResults


def get_flights(filters: FlightsAPIFilters) -> FlightSearchResults:
    if filters.currency and filters.currency not in ["USD", "PLN"]:
        raise ValueError("Currency not supported")
    response = requests.get("https://api.airline.com/flights", params=asdict(filters))
    return dacite.from_dict(data_class=FlightSearchResults, data=response.json())
