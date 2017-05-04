#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import random

__title__ = "LootTable"
__author__ = "DeflatedPickle"
__version__ = "1.0.1"


class LootTable(object):
    """Creates a loot table."""
    def __init__(self, window, name: str, items: list):
        self.window = window
        self.name = name
        self.items = items

    def pick_item(self):
        """Picks a random item from the table."""
        return self.items[random.randint(0, len(self.items)) - 1]

    def open(self, *args):
        """Opens the container and gives the player an item inside."""
        item = self.pick_item()
        self.window.player.give(item)
        return item

    def get_items(self, *args):
        """Returns all items in the chest."""
        return self.items

    def get_items_names(self, *args):
        """Returns all names of the items in the chest."""
        list_ = []
        for i in self.items:
            list_.append(i.name)
        return list_
