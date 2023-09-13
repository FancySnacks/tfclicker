from dataclasses import dataclass, field


@dataclass
class Item:
    """Represents a single currency item (scrap, rec, ref or a key)"""
    name: str
    amount: float
    gain_rate: float
    gain_amount: float

    def increment(self):
        self.amount += self.gain_amount

    def __repr__(self) -> str:
        return f"{int(self.amount)}x {self.name}"
