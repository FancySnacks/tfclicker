import time

from multiprocessing import Process

from item import Item


class Overlord:
    """Represents a game session"""
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
            print(self.weapons)
            time.sleep(self.weapons.gain_rate)