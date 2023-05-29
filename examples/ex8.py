import datetime
from dataclasses import dataclass

import dacite

DATA = {
    "origin": "ATL",
    "destination": "LAX",
    "departure": "2023-12-24T12:00:00",
    "currency": "USD",
    "price": 100.00,
}


@dataclass
class Flight:
    origin: str
    destination: str
    departure: datetime.datetime
    currency: str
    price: float


flight = dacite.from_dict(
    data_class=Flight,
    data=DATA,
    config=dacite.Config(
        type_hooks={datetime.datetime: datetime.datetime.fromisoformat}
    ),
)

print(flight)
