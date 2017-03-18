__title__ = "Player"
__author__ = "DeflatedPickle"
__version__ = "1.0.0"


class Player(object):
    """Creates the player."""
    def __init__(self, health: int, total_health: int, money=0):
        self.health = health
        self.total_health = total_health
        self.money = money
        self.inventory = []

    def heal(self, amount: int):
        """Heals the player by a given amount."""
        for i in range(amount):
            if self.health <= self.total_health:
                self.health += 1

    def get_inventory(self):
        """Returns all items in the players inventory."""
        return self.inventory

    def get_inventory_names(self):
        """Returns all names of the items in the players inventory."""
        list_ = []
        for i in self.inventory:
            list_.append(i.name)
        return list_

    def give(self, item):
        """Gives the player an item."""
        self.inventory.append(item)

    def pay(self, how_much: int):
        self.money += how_much

    def receive(self, how_much: int):
        self.money -= how_much