__title__ = "Merchant"
__author__ = "DeflatedPickle"
__version__ = "1.0.0"


class Merchant(object):
    """Creates an merchant."""
    def __init__(self, name: str, money: int, inventory: list, description=""):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.description = description

    def get_inventory(self, *args):
        pass

    def sell_item(self, item, *args):
        pass

    def buy_item(self, item, *args):
        pass
