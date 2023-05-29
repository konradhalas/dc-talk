import requests


def get_flights(filters):
    response = requests.get("https://api.airline.com/flights", params=filters)
    return response.json()
