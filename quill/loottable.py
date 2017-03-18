import random

__title__ = "LootTable"
__author__ = "DeflatedPickle"
__version__ = "1.0.0"


class LootTable(object):
    """Creates a loot table."""
    def __init__(self, window, name: str, items: list):
        self.window = window
        self.name = name
        self.items = items

    def pick_item(self):
        """Picks a random item from the table."""
        return self.items[random.randint(0, len(self.window.player.inventory)) - 1]

    def open(self, *args):
        """Opens the container and gives the player an item inside."""
        self.window.player.give(self.pick_item())

    def get_items(self, *args):
        """Returns all items in the chest."""
        return self.items

    def get_items_names(self, *args):
        """Returns all names of the items in the chest."""
        list_ = []
        for i in self.items:
            list_.append(i.name)
        return list_
