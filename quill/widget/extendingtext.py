#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from tkinter import Text

import quill

from quill.widget import Widget

class ExtendingText(Widget):
    def __init__(self, window: quill.Window, text_widget: Text, text: str="", fill_line: bool=False, index: int or str="end", command=None):
        self.window = window
        self.text_widget = text_widget
        self.text = text
        self.fill_line = fill_line
        self.index = index
        self.command = command

        tag = "Extend-{}-{}:{}".format(re.sub("[^0-9a-zA-Z]+", "", extend), "normal", self.window.id_current_extend)
        tag2 = "Extend-{}-{}:{}".format(re.sub("[^0-9a-zA-Z]+", "", extend), "extend", self.window.id_current_extend)

    def _insert_widget(self):
        self.text.tag_configure(tag, foreground=self.colour_extend_on, elide=False)
        self.text.tag_configure(tag2, foreground=self.colour_extend_off, elide=True)
        self.text.insert(index, what + "\n" if fill_line else what, tag)
        self.text.insert(index, extend + "\n" if fill_line else extend, tag2)

        self.unbind_tag(tag, release=True, both=True)

        self.text.tag_bind(tag, "<ButtonRelease-1>", command, "+")
        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_extend(tag, tag2), "+")

        self.bind_cursor(tag)
        self.bind_background(tag)

        self.id_current_extend += 1

