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

# 3 - frozen
# print({filters})

# 4 - replace
# print(replace(filters, origin="JFK"))

# 5 - asdict
# print(asdict(filters))
