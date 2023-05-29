import requests

from examples.ex3 import FlightsAPIFilters


def get_flights(filters: FlightsAPIFilters) -> dict:
    if filters.currency and filters.currency not in ["USD", "PLN"]:
        raise ValueError("Currency not supported")
    response = requests.get("https://api.airline.com/flights", params=filters)
    return response.json()
