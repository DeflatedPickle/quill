#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from tkinter import Text

from quill.widget import Widget

class Text(Widget):
    def __init__(self, text_widget: Text, text: str="", fill_line: bool=False, index: int or str="end", tag: str="Paragraph"):
        self.text_widget = text_widget
        self.text = text
        self.fill_line = fill_line
        self.index = index
        self.tag = tag

    def _insert_widget(self):
        self.text_widget.insert(index, text + "\n" if fill_line else text, tag)

