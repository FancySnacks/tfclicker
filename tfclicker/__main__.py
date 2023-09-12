"""Entry script"""

import time

from dataclasses import dataclass, field
from multiprocessing import Process
from typing import Sequence


@dataclass
class Item:
    name: str
    amount: float
    gain_rate: float
    gain_amount: float

    def increment(self):
        self.amount += self.gain_amount


class Overlord:
    def __init__(self):
        self.weapons = Item("weapons", 0, 1.0, 1.0)
        self.scrap = Item("scrap", 0, 0.0, 0.0)
        self.reclaimed = Item("reclaimed", 0, 0.0, 0.0)
        self.refined = Item("refined", 0, 0.0, 0.0)
        self.keys = Item("keys", 0, 0.0, 0.0)

    def begin(self):
        p = Process(target=self.increment_score)
        p.start()

    def increment_score(self):
        while True:
            self.weapons.increment()
            print(f"Weapons: {self.weapons.amount}")
            time.sleep(self.weapons.gain_rate)


def main(argv: Sequence[str] | None = None):
    app = Overlord()
    app.begin()


if __name__ == '__main__':
    main()
