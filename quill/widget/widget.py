#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from tkinter import Text

class Widget(object):
    def __init__(self, text_widget: Text):
        self.text_widget = text_widget

        self._insert_widget()

    def _insert_widget(self):
        pass

