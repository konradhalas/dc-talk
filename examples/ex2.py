import requests


def get_flights(filters):
    if filters["currency"] not in ["USD", "PLN"]:
        raise ValueError("Currency not supported")
    response = requests.get("https://api.airline.com/flights", params=filters)
    return response.json()
