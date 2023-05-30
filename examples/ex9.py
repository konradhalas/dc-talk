from dataclasses import dataclass
from typing import Literal

import dacite

DATA = {
    # origin, destination, departure...
    "ancillaries": [
        {
            "type": "INTERNET",
            "network_speed": "512KB",
        },
        {
            "type": "INSURANCE",
            "amount": 1000,
        },
    ]
}


@dataclass
class InternetAncillary:
    type: Literal["INTERNET"]
    network_speed: str


@dataclass
class InsuranceAncillary:
    type: Literal["INSURANCE"]
    amount: int


@dataclass
class Flight:
    ancillaries: list[InternetAncillary | InsuranceAncillary]


result = dacite.from_dict(data_class=Flight, data=DATA)

print(result)
