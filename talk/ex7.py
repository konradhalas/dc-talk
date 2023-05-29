import dacite

from talk.ex6 import FlightSearchResults, RESPONSE_DATA

result = dacite.from_dict(data_class=FlightSearchResults, data=RESPONSE_DATA)

print(result)
