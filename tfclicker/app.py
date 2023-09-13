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
        """Start game loop"""
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
