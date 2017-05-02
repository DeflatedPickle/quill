__title__ = "Merchant"
__author__ = "DeflatedPickle"
__version__ = "1.1.1"


class Merchant(object):
    """Creates an Merchant."""
    def __init__(self, window, name: str, money: int, difference: int, inventory: list, description=""):
        self.window = window
        self.name = name
        self.money = money
        self.difference = difference
        self.inventory = inventory
        self.description = description

    def show_inventory(self, *args):
        self.window.enable()
        self.window.insert_new_line()
        self.window.insert_new_line()

        self.window.text.insert("end", "Inventory:\n", "Quote")
        for item in self.inventory:
            self.window.insert_item("end", self.inventory[self.inventory.index(item)])
            self.window.insert_command("end", " Buy", command=self.buy_item)
            self.window.insert_command("end", " Sell", command=self.sell_item)
            self.window.text.insert("end", "\n", "Quote")

        self.window.goto_end()
        self.window.disable()

    def sell_item(self, item, *args):
        """Sell an Item to the Merchant."""
        self.window.player.inventory.remove(item)
        self.window.player.money += item.value
        self.inventory.append(item)
        self.money -= item.value

    def buy_item(self, item, *args):
        """Buy an Item from the Merchant."""
        self.window.player.inventory.append(item)
        self.window.player.money -= item.value
        self.inventory.remove(item)
        self.money += item.value

    def give(self, item):
        """Gives the Merchant an item."""
        self.inventory.append(item)

    def remove(self, item):
        """Remove an item from the Merchant."""
        self.inventory.remove(item)

    def pay(self, how_much: int):
        """Give money to the Merchant."""
        self.money += how_much

    def receive(self, how_much: int):
        """Take money from the Merchant."""
        self.money -= how_much
