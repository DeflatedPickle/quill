__title__ = "Merchant"
__author__ = "DeflatedPickle"
__version__ = "1.1.1"


class Merchant(object):
    """Creates an merchant."""
    # TODO: Finish this class
    def __init__(self, window, name: str, money: int, price_difference: int, inventory: list, description=""):
        self.window = window
        self.name = name
        self.money = money
        self.price_difference = price_difference
        self.inventory = inventory
        self.description = description

    def show_inventory(self, *args):
        self.window.enable()
        self.window.insert_new_line()
        self.window.insert_new_line()

        self.window.insert_text("Inventory:\n", tag="Quote")
        for item in self.inventory:
            self.window.insert_item(self.inventory[self.inventory.index(item)])
            self.window.insert_command(" Buy", command=self.buy_item)
            self.window.insert_command(" Sell", command=self.sell_item)
            self.window.insert_text("\n", tag="Quote")

        self.window.goto_end()
        self.window.disable()

    def sell_item(self, item, *args):
        """Sell an Item to the merchant."""
        self.window.player.inventory.remove(item)
        self.window.player.money += item.value
        self.inventory.append(item)
        self.money -= item.value

    def buy_item(self, item, *args):
        """Buy an Item from the merchant."""
        self.window.player.inventory.append(item)
        self.window.player.money -= item.value
        self.inventory.remove(item)
        self.money += item.value

    def give(self, item):
        """Gives the merchant an item."""
        self.inventory.append(item)

    def remove(self, item):
        """Remove an item from the merchant."""
        self.inventory.remove(item)

    def pay(self, how_much: int):
        """Give money to the merchant."""
        self.money += how_much

    def receive(self, how_much: int):
        """Take money from the merchant."""
        self.money -= how_much
