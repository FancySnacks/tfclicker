"""Currencies"""

import time

from multiprocessing import Process
from dataclasses import dataclass


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


weapons = Item("weapons", 0, 1.0, 1.0)
scrap = Item("scrap", 0, 0.0, 0.0)
reclaimed = Item("reclaimed", 0, 0.0, 0.0)
refined = Item("refined", 0, 0.0, 0.0)
keys = Item("keys", 0, 0.0, 0.0)


class ItemMaster:
    """Manages all currencies"""
    def __init__(self):
        self.weapons = weapons
        self.scrap = scrap
        self.reclaimed = reclaimed
        self.refined = refined
        self.keys = keys

        p = Process(target=self.start_increment_score_loop, args=[self.weapons])
        p.start()

    def start_increment_score_loop(self, target: Item):
        """
        An asynchronous while loop that increases count of target item based on its gain_rate and gain_amount
        properties
        """
        while True:
            target.increment()
            print(target)
            time.sleep(target.gain_rate)
