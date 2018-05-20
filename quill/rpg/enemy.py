#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

__title__ = "Enemy"
__author__ = "DeflatedPickle"
__version__ = "1.0.0"


class Enemy(object):
    """Creates an enemy."""
    # TODO: Finish this class
    def __init__(self, name: str, damage: int, health: int, total_health: int):
        self.name = name
        self.damage = damage
        self.health = health
        self.total_health = total_health
