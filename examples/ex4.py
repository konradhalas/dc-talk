from dataclasses import dataclass


@dataclass
class Currency:
    code: str

    def __post_init__(self):
        if len(self.code) != 3:
            raise ValueError("Currency code must be 3 characters long")


print(Currency("USD"))
