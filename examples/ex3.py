import datetime
from dataclasses import dataclass


@dataclass
class FlightsAPIFilters:
    origin: str
    destination: str
    departure_date: datetime.date
    currency: str | None


filters = FlightsAPIFilters(
    origin="ATL",
    destination="LAX",
    currency="USD",
    departure_date=datetime.date(2023, 12, 24),
)

# 1 - __repr__
print(filters)

# 2 - IDE
# print(filters.origin)

# 3 - default value
# print(filters.carriers)

# 4 - frozen
# filters.origin = "JFK"
# print({filters})

# 5 - replace
# print(replace(filters, origin="JFK"))

# 6 - asdict
# print(asdict(filters))

# 7 - custom method
# def display_format(self) -> str:
#     return f"{self.origin}->{self.destination} ({self.departure_date.isoformat()})"
# print(filters.display_format())

# 8 - IDE/mypy

# FlightsAPIFilters(
#     origin=123,
#     destination="LAX",
#     currency="USD",
#     departure_date=datetime.date(2023, 12, 24),
# )
