from dataclasses import dataclass, field


class UpgradeMaster:
    def __init__(self):
        self.upgrades: list[Purchasable] = []


@dataclass
class Tier:
    name: str
    number: int


@dataclass
class Purchasable:
    name: str
    price_in_weapons: float
    price_multiplier: float
    current_tier: Tier
    tiers: list[Tier] = field(default_factory=list)
