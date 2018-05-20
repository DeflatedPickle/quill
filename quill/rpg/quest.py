#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

__title__ = "Quest"
__author__ = "DeflatedPickle"
__version__ = "1.1.0"


class Quest(object):
    """Creates an quest."""
    # TODO: Finish this class
    def __init__(self, window, name: str, reward: list, goal: str, description=""):
        self.window = window
        self.name = name
        self.reward = reward
        self.goal = goal
        self.description = description

    def show(self, *args):
        """Shows the quest."""
        # TODO: Finish this function
        pass

    def complete(self, *args):
        """Complete the quest."""
        # TODO: Finish this function
        pass

    def fail(self, *args):
        """Fail a quest."""
        # TODO: Finish this function
        pass

    def hand_in(self, *args):
        """Hand in a quest."""
        # TODO: Finish this function
        pass
