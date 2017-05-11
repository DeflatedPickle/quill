#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

__title__ = "Merchant"
__author__ = "DeflatedPickle"
__version__ = "1.1.4"


class Merchant(object):
    """Creates a merchant."""
    # TODO: Finish this class
    def __init__(self, window, name: str, money: int, price_difference: int, inventory: list, description=""):
        self.window = window
        self.name = name
        self.money = money
        self.price_difference = price_difference
        self.inventory = inventory
        self.description = description

        self.merchant_inventory = []
        self.your_inventory = []

    def show_inventory(self, *args):
        self.window.enable()
        self.window.insert_new_line()
        self.window.insert_new_line()

        self.merchant_inventory.clear()
        self.window.insert_text("-----Merchant-----", True)
        self.window.insert_text("Money: {}".format(self.money), True)
        self.window.insert_text("Inventory:", True)
        for item in self.inventory:
            self.window.insert_item(self.inventory[self.inventory.index(item)])
            trigger = self.window.insert_trigger(" Buy", True, command=lambda *args: self.buy_item(item))
            self.merchant_inventory.append(trigger)

        self.window.insert_text("-----Player-----", True)
        self.your_inventory.clear()
        self.window.insert_text("Money: {}".format(self.window.player.money), True)
        self.window.insert_text("Inventory:", True)
        for item in self.window.player.inventory:
            self.window.insert_item(self.inventory[self.window.player.inventory.index(item)])
            trigger = self.window.insert_trigger(" Sell", True, command=lambda *args: self.sell_item(item))
            self.your_inventory.append(trigger)
        self.window.insert_text("-------------------", True)

        self.window.goto_end()
        self.window.disable()

    def sell_item(self, item, *args):
        """Sell an item to the merchant."""
        self.window.player.inventory.remove(item)
        self.window.player.money += item.value
        self.inventory.append(item)
        self.money -= item.value

        self.window.enable()
        self.window.insert_new_line()

        self.window.insert_text("Thank you for the ")
        self.window.insert_item(item)
        self.window.insert_text(". I'm sure it will be of great use to me.")

        self.window.goto_end()
        self.window.disable()

        for item in self.merchant_inventory:
            self.window.toggle_trigger(item)

        for item in self.your_inventory:
            self.window.toggle_trigger(item)

        self.show_inventory()

    def buy_item(self, item, *args):
        """Buy an item from the merchant."""
        self.window.player.inventory.append(item)
        self.window.player.money -= item.value
        self.inventory.remove(item)
        self.money += item.value

        self.window.enable()
        self.window.insert_new_line()

        self.window.insert_text("Here you go. Enjoy the ")
        self.window.insert_item(item)
        self.window.insert_text(".")

        self.window.goto_end()
        self.window.disable()

        for item in self.merchant_inventory:
            self.window.toggle_trigger(item)

        for item in self.your_inventory:
            self.window.toggle_trigger(item)

        self.show_inventory()

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
