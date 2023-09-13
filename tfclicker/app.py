"""Manager class that puts it all together"""

from item import ItemMaster


class Overlord:
    """Represents a game session"""
    def __init__(self):
        self.ItemMaster = ItemMaster()

    def begin(self):
        """Start game loop"""
        pass
