from dataclasses import dataclass

# result of response.json()
RESPONSE_DATA = {
    "point_of_sale": "US",
    "flights": [
        {
            "origin": "ATL",
            "destination": "LAX",
            "departure": "2023-12-24T12:00:00",
            "currency": "USD",
            "price": 100.00,
        },
        {
            "origin": "ATL",
            "destination": "LAX",
            "departure": "2023-12-24T14:00:00",
            "currency": "USD",
            "price": 200.00,
        },
    ]
}


@dataclass
class Flight:
    origin: str
    destination: str
    departure: str
    currency: str
    price: float


@dataclass
class FlightSearchResults:
    point_of_sale: str
    flights: list[Flight]


result = FlightSearchResults(
    point_of_sale=RESPONSE_DATA["point_of_sale"],
    flights=[
        Flight(
            origin=flight["origin"],
            destination=flight["destination"],
            departure=flight["departure"],
            currency=flight["currency"],
            price=flight["price"],
        )
        for flight in RESPONSE_DATA["flights"]
    ],
)


