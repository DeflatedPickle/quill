#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk
from tkinter import font
import re

from .player import Player
from .loottable import LootTable
from .item import Item
from .merchant import Merchant
from .quest import Quest

__title__ = "Window"
__author__ = "DeflatedPickle"
__version__ = "1.41.2"


class Window(tk.Tk):
    """Creates the Window used for the game."""
    def __init__(self, title="Quill", icon=None, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(title)
        if icon is not None:
            self.iconphoto(self._w, icon)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.player = Player(100, 100)

        self.valid_item_types = {"weapon": ["sword", "axe", "bow"],
                                 "potion": ["health"],
                                 "key": ["door", "chest"]}

        self.valid_item_arguments = {"weapon": {"type": "", "damage": 0},
                                     "potion": {"type": "", "amount": 0},
                                     "key": {"type": ""}}

        self.valid_item_rarities = {"Uncommon": "white",
                                    "Common": "green",
                                    "Rare": "blue",
                                    "Epic": "purple",
                                    "Legendary": "orange"}

        self.text = tk.Text(self, wrap="word", state="disabled")
        self.text.grid(row=0, column=0, sticky="nesw")
        self.text.focus()

        self.scrollbar_horizontal = ttk.Scrollbar(self, orient="horizontal", command=self.text.xview)
        # self.scrollbar_horizontal.grid(row=1, column=0, sticky="we")

        self.scrollbar_vertical = ttk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.scrollbar_vertical.grid(row=0, column=1, sticky="ns")

        self.text.configure(xscrollcommand=self.scrollbar_horizontal.set, yscrollcommand=self.scrollbar_vertical.set)

        self.colour_text = "black"
        self.colour_text_background = "white"
        self.colour_text_background_active = "light grey"

        self.colour_command = "blue"
        self.id_current_command = 0

        self.colour_extend_on = "turquoise"
        self.colour_extend_off = "slate blue"
        self.id_current_extend = 0

        self.colour_check_on = "green"
        self.colour_check_off = "red"
        self.id_current_check = 0

        self.colour_radio_on = "green"
        self.colour_radio_off = "red"
        self.id_current_radio = 0

        self.colour_trigger_on = "green"
        self.colour_trigger_off = "red"
        self.id_current_trigger = 0

        self.colour_container_on = "orange"
        self.colour_container_off = "cyan"
        self.id_current_container = 0

        self.colour_item_on = "gold"
        self.colour_item_off = "purple"
        self.id_current_item = 0

        self.colour_merchant_on = "gold"
        self.colour_merchant_off = "purple"
        self.id_current_merchant = 0

        self.colour_quest_on = "gold"
        self.colour_quest_off = "purple"
        self.id_current_quest = 0

        value = 30
        for i in range(5):
            self.font = font.Font(family="TkTextFont", size=value)
            self.text.tag_configure("Heading-{}".format(i+1), font=self.font)
            value -= 5

        self.text.tag_configure("Quote", background="light grey")
        self.text.tag_configure("Paragraph", foreground=self.colour_text)

        self.startup()

    def startup(self):
        """This function runs on startup."""
        pass

    # Modifier Functions

    def enable(self, *args):
        """Must be used before inserting anything."""
        self.text.configure(state="normal")

    def disable(self, *args):
        """Used to disable the text."""
        self.text.configure(state="disable")

    def clear(self, *args):
        """Clears all text from the game."""
        self.text.delete(1.0, "end")

    def goto_end(self, *args):
        """Scrolls the text widget to the bottom."""
        self.text.see("end")

    # Insert Methods

    def insert_text(self, what: str="", fill_line: bool=False, index: int or str="end", tag: str="Paragraph", *args):
        """Inserts a string of text into the game."""
        self.text.insert(index, what + "\n" if fill_line else what, tag)

    def insert_extending_text(self, what: str="", extend: str="", fill_line: bool=False, index: int or str="end", command=None, *args):
        """Inserts a string of text that can be extended."""
        tag = "Extend-{}-{}:{}".format(re.sub("[^0-9a-zA-Z]+", "", extend), "normal", self.id_current_extend)
        tag2 = "Extend-{}-{}:{}".format(re.sub("[^0-9a-zA-Z]+", "", extend), "extend", self.id_current_extend)
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

    def toggle_extend(self, tag: str, tag2: str, *args):
        """Toggles an extending text off."""
        self.text.tag_configure(tag, elide=True)
        self.text.tag_configure(tag2, elide=False)

    def disable_extend(self, tag: str, *args):
        """Disables an extending text."""
        self.text.tag_configure(tag, foreground=self.colour_extend_off)
        self.text.tag_unbind(tag, "<ButtonRelease-1>")
        self.text.tag_unbind(tag, "<Button-1>")

    def insert_command(self, what: str="", fill_line: bool=True, index: int or str="end", command=None, *args):
        """Inserts a click-able command into the game."""
        tag = "Command-{}:{}".format(re.sub("[^0-9a-zA-Z]+", "", what), self.id_current_command)
        self.text.tag_configure(tag, foreground=self.colour_command)
        self.text.insert(index, what + "\n" if fill_line else what, tag)

        self.unbind_tag(tag, release=True)

        self.text.tag_bind(tag, "<ButtonRelease-1>", command, "+")

        self.bind_cursor(tag)
        self.bind_background(tag)

        self.id_current_command += 1

    def insert_checkbutton(self, what: str="", variable: tk.BooleanVar=None, fill_line: bool=True, index: int or str="end", command=None, *args):
        """Insert a checkbutton into the game."""
        tag = "Check-{}:{}".format(re.sub("[^0-9a-zA-Z]+", "", what), self.id_current_check)
        if variable.get():
            self.text.tag_configure(tag, foreground=self.colour_check_on)
        elif not variable.get():
            self.text.tag_configure(tag, foreground=self.colour_check_off)
        self.text.insert(index, what + "\n" if fill_line else what, tag)

        self.unbind_tag(tag)

        self.text.tag_bind(tag, "<Button-1>", command, "+")
        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_check(variable, tag), "+")

        self.bind_cursor(tag)
        self.bind_background(tag)

        self.id_current_check += 1

    def toggle_check(self, variable: tk.BooleanVar, tag: str, *args):
        """Toggles a checkbutton."""
        variable.set(not variable.get())
        if variable.get():
            self.text.tag_configure(tag, foreground=self.colour_check_on)
        elif not variable.get():
            self.text.tag_configure(tag, foreground=self.colour_check_off)

    def insert_radiobutton(self, what: str="", variable: tk.IntVar=None, value: int=0, fill_line: bool=True, index: int or str="end", command=None, *args):
        """Inserts a radiobutton into the game."""
        tag = "Radio-{}-{}:{}".format(re.sub("[^0-9a-zA-Z]+", "", str(variable)), str(value), self.id_current_radio)
        if variable.get() == value:
            self.text.tag_configure(tag, foreground=self.colour_radio_on)
        elif variable.get() != value:
            self.text.tag_configure(tag, foreground=self.colour_radio_off)
        self.text.insert(index, what + "\n" if fill_line else what, tag)

        self.unbind_tag(tag, release=True, both=True)

        self.text.tag_bind(tag, "<ButtonRelease-1>", command, "+")
        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_radio(variable, value, tag), "+")

        self.bind_cursor(tag)
        self.bind_background(tag)

        self.id_current_radio += 1

    def toggle_radio(self, variable: tk.IntVar, value: int, tag: str, *args):
        """Toggles a radiobutton."""
        variable.set(value)
        for name in self.text.tag_names():
            name_cut = "{}_{}".format(name.split(":")[0][:8], name.split(":")[0][8:]).split("-")
            try:
                name_cut = name_cut[0] + "-" + name_cut[1]
            except IndexError:
                pass
            if name_cut == "Radio-{}".format(str(variable)):
                self.text.tag_configure(name, foreground=self.colour_radio_off)

        if variable.get() == value:
            self.text.tag_configure(tag, foreground=self.colour_radio_on)
        elif variable.get() != value:
            self.text.tag_configure(tag, foreground=self.colour_radio_off)

    def insert_trigger(self, what: str="", fill_line: bool=False, index: int or str="end", command=None, *args):
        """Inserts a trigger into the game."""
        tag = "Trigger-{}:{}".format(re.sub("[^0-9a-zA-Z]+", "", what), self.id_current_trigger)
        self.text.tag_configure(tag, foreground=self.colour_trigger_on)
        self.text.insert(index, what + "\n" if fill_line else what, tag)

        self.unbind_tag(tag)

        self.text.tag_bind(tag, "<Button-1>", command, "+")
        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_trigger(tag), "+")

        self.bind_cursor(tag)
        self.bind_background(tag)

        self.id_current_trigger += 1

        return tag

    def toggle_trigger(self, tag: str, *args):
        """Toggles a trigger off."""
        self.text.tag_configure(tag, foreground=self.colour_trigger_off)
        self.text.tag_unbind(tag, "<Button-1>")

    def check_trigger(self, tag: str, *args):
        """Checks the value of a trigger."""
        if self.text.tag_cget(tag, "foreground") == self.colour_trigger_on:
            return True
        elif self.text.tag_cget(tag, "foreground") == self.colour_trigger_off:
            return False

    # Insert Classes

    def insert_container(self, loot_table: LootTable, fill_line: bool=False, index: int or str="end", command=None, *args):
        """Insert a checkbutton into the game."""
        tag = "Container-{}:{}".format(re.sub("[^0-9a-zA-Z]+", "", loot_table.name), self.id_current_container)
        self.text.tag_configure(tag, foreground=self.colour_container_on)
        self.text.insert(index, loot_table.name + "\n" if fill_line else loot_table.name, tag)

        self.unbind_tag(tag)

        self.text.tag_bind(tag, "<Button-1>", command, "+")
        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.open_container(loot_table, tag), "+")

        self.bind_cursor(tag)
        self.bind_background(tag)

        self.id_current_container += 1

    def open_container(self, loot_table: LootTable, tag: str, *args):
        """Opens a container."""
        loot_table.open()
        self.text.tag_configure(tag, foreground=self.colour_container_off)
        self.text.tag_unbind(tag, "<Button-1>")

    def lock_container(self, tag: str, *args):
        """Locks a container."""
        self.text.tag_configure(tag, foreground=self.colour_container_off)
        self.text.tag_unbind(tag, "<Button-1>")

    def check_container(self, tag: str, *args):
        """Checks the value of a container."""
        if self.text.tag_cget(tag, "foreground") == self.colour_container_on:
            return True
        elif self.text.tag_cget(tag, "foreground") == self.colour_container_off:
            return False

    def insert_item(self, item: Item, fill_line: bool=False, index: int or str="end", *args):
        """Inserts an item into the game."""
        tag = "Item-{}:{}".format(re.sub("[^0-9a-zA-Z]+", "", item.name), self.id_current_item)
        self.text.tag_configure(tag, foreground=self.colour_item_on)
        self.text.insert(index, item.name + "\n" if fill_line else item.name, tag)

        self.unbind_tag(tag)

        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_item(item, tag), "+")

        self.bind_cursor(tag)
        self.bind_background(tag)

        self.id_current_item += 1

    def toggle_item(self, item: Item, tag: str, *args):
        """Toggles an item."""
        item.show_stats()
        self.text.tag_configure(tag, foreground=self.colour_item_off)

    def insert_merchant(self, merchant: Merchant, fill_line: bool=False, index: int or str="end", *args):
        """Inserts an merchant into the game."""
        tag = "Merchant-{}:{}".format(re.sub("[^0-9a-zA-Z]+", "", merchant.name), self.id_current_merchant)
        self.text.tag_configure(tag, foreground=self.colour_merchant_on)
        self.text.insert(index, merchant.name + "\n" if fill_line else merchant.name, tag)

        self.unbind_tag(tag)

        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_merchant(merchant, tag), "+")

        self.bind_cursor(tag)
        self.bind_background(tag)

        self.id_current_merchant += 1

    def toggle_merchant(self, merchant: Merchant, tag: str, *args):
        """Toggles a merchant."""
        merchant.show_inventory()
        self.text.tag_configure(tag, foreground=self.colour_merchant_off)

    def insert_quest(self, quest: Quest, fill_line: bool=False, index: int or str="end", *args):
        """Inserts a quest into the game."""
        tag = "Quest-{}:{}".format(re.sub("[^0-9a-zA-Z]+", "", quest.name), self.id_current_quest)
        self.text.tag_configure(tag, foreground=self.colour_merchant_on)
        self.text.insert(index, quest.name + "\n" if fill_line else quest.name, tag)

        self.unbind_tag(tag)

        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_quest(quest, tag), "+")

        self.bind_cursor(tag)
        self.bind_background(tag)

        self.id_current_quest += 1

    def toggle_quest(self, quest: Quest, tag: str, *args):
        """Toggles a quest."""
        quest.show()
        self.text.tag_configure(tag, foreground=self.colour_quest_off)

    # Insert Widgets

        # TK Versions

    def insert_tk_button(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Button into the game."""
        widget = tk.Button(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_checkbutton(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Checkbutton into the game."""
        widget = tk.Checkbutton(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_entry(self, index: int or str="end", *args, **kwargs):
        """Insert an tk.Entry into the game."""
        widget = tk.Entry(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_frame(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Frame into the game."""
        widget = tk.Frame(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_label(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Label into the game."""
        widget = tk.Label(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_labelframe(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.LabelFrame into the game."""
        widget = tk.LabelFrame(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_menubutton(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Menubutton into the game."""
        widget = tk.Menubutton(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_panedwindow(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.PanedWindow into the game."""
        widget = tk.PanedWindow(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_radiobutton(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Radiobutton into the game."""
        widget = tk.Radiobutton(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_scale(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Scale into the game."""
        widget = tk.Scale(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_scrollbar(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Scrollbar into the game."""
        widget = tk.Scrollbar(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

        # TK Only

    def insert_tk_canvas(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Canvas into the game."""
        widget = tk.Canvas(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_listbox(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Listbox into the game."""
        widget = tk.Listbox(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_message(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Listbox into the game."""
        widget = tk.Message(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_text(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Listbox into the game."""
        widget = tk.Text(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_tk_spinbox(self, index: int or str="end", *args, **kwargs):
        """Insert a tk.Spinbox into the game."""
        widget = tk.Spinbox(self.text, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

        # TTK Versions

    def insert_ttk_button(self, command=None, width: int=None, index: int or str="end", *args, **kwargs):
        """Insert a ttk.Button into the game."""
        widget = ttk.Button(self.text, command=command, width=width, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_checkbutton(self, command=None, offvalue: int=0, onvalue: int=1, variable: tk.BooleanVar=None, index: int or str="end", *args, **kwargs):
        """Insert a ttk.Checkbutton into the game."""
        widget = ttk.Checkbutton(self.text, command=command, offvalue=offvalue, onvalue=onvalue, variable=variable, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_entry(self, exportselection: int=0, invalidcommand=None, justify: tk.LEFT or tk.CENTER or tk.RIGHT or str=None, show: str=None, state: str="normal", textvariable: tk.Variable=None, validate=None, validatecommand=None, width: int=None, index: int or str="end", *args, **kwargs):
        """Insert a ttk.Entry into the game."""
        widget = ttk.Entry(self.text, exportselection=exportselection, invalidcommand=invalidcommand, justify=justify, show=show, state=state, textvariable=textvariable, validate=validate, validatecommand=validatecommand, width=width, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_frame(self, borderwidth: int=0, relief: tk.FLAT or tk.RAISED or tk.SUNKEN or tk.GROOVE or tk.RIDGE or str="flat", padding: list=[], width: int=None, height: int=None, index: int or str="end", *args, **kwargs):
        """Insert a ttk.Frame into the game."""
        widget = ttk.Frame(self.text, borderwidth=borderwidth, relief=relief, padding=padding, width=width, height=height, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_label(self, anchor: tk.W or tk.CENTER or tk.E or str=None, background: str="", font: font.Font=None, foreground: str="", justify: tk.LEFT or tk.CENTER or tk.RIGHT or str=None, padding: list=[], relief: tk.FLAT or tk.RAISED or tk.SUNKEN or tk.GROOVE or tk.RIDGE or str="flat", text: str="", wraplength: int=0, index: int or str="end", *args, **kwargs):
        """Insert a ttk.Label into the game."""
        widget = ttk.Label(self.text, anchor=anchor, background=background, font=font, foreground=foreground, justify=justify, padding=padding, relief=relief, text=text, wraplength=wraplength, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_labelframe(self, labelanchor: str="nw", text: str="", underline: int=None, padding: list=[], labelwidget: tk.Widget=None, width: int=None, height: int=None, index: int or str="end", *args, **kwargs):
        """Insert a ttk.LabelFrame into the game."""
        widget = ttk.LabelFrame(self.text, labelanchor=labelanchor, text=text, underline=underline, padding=padding, labelwidget=labelwidget, width=width, height=height, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_menubutton(self, direction: str="below", menu: tk.Menu=None, index: int or str="end", *args, **kwargs):
        """Insert a ttk.Menubutton into the game."""
        widget = ttk.Menubutton(self.text, direction=direction, menu=menu, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_panedwindow(self, orient: tk.HORIZONTAL or tk.VERTICAL or str=None, width: int=None, height: int=None, index: int or str="end", *args, **kwargs):
        """Insert a ttk.PanedWindow into the game."""
        widget = ttk.PanedWindow(self.text, orient=orient, width=width, height=height, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_radiobutton(self, command=None, value: int=None, variable: tk.IntVar=None, index: int or str="end", *args, **kwargs):
        """Insert a ttk.Radiobutton into the game."""
        widget = ttk.Radiobutton(self.text, command=command, value=value, variable=variable, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_scale(self, command=None, from_: int=0, length: int=100, to: int=100, value: float=0.0, variable: tk.IntVar=None, index: int or str="end", *args, **kwargs):
        """Insert a ttk.Scale into the game."""
        widget = ttk.Scale(self.text, command=command, from_=from_, length=length, to=to, value=value, variable=variable, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_scrollbar(self, command=None, orient: tk.HORIZONTAL or tk.VERTICAL or str=None, index: int or str="end", *args, **kwargs):
        """Insert a ttk.Scrollbar into the game."""
        widget = ttk.Scrollbar(self.text, command=command, orient=orient, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

        # TTK Only

    def insert_ttk_combobox(self, exportselection: bool=False, justify: str="left", height: int=None, postcommand=None, state: str="normal", textvariable: tk.Variable=None, values: list=[], width: int=10, index: int or str="end", *args, **kwargs):
        """Insert a ttk.Combobox into the game."""
        widget = ttk.Combobox(self.text, exportselection=exportselection, justify=justify, height=height, postcommand=postcommand, state=state, textvariable=textvariable, values=values, width=width, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_notebook(self, height: int=None, padding: list=[], width: int=None, index: int or str="end", **kwargs):
        """Insert a ttk.Notebook into the game."""
        widget = ttk.Notebook(self.text, height=height, padding=padding, width=width, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_progressbar(self, orient: str="horizontal", length: int=None, mode: str="determinate", maximum: int=100, value: int=0, variable: tk.IntVar=None, phase: int=0, index: int or str="end", **kwargs):
        """Insert a ttk.Progressbar into the game."""
        widget = ttk.Progressbar(self.text, orient=orient, length=length, mode=mode, maximum=maximum, value=value, variable=variable, phase=phase, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_separator(self, orient: str="horizontal", index: int or str="end", **kwargs):
        """Insert a ttk.Separator into the game."""
        widget = ttk.Separator(self.text, orient=orient, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    def insert_ttk_treeview(self, columns: list=[], displaycolumns: list or str="#all", height: int=None, padding: list=[], selectmode: str="extended", show: str="tree headings", index: int or str="end", **kwargs):
        """Insert a ttk.Separator into the game."""
        widget = ttk.Treeview(self.text, columns=columns, displaycolumns=displaycolumns, height=height, padding=padding, selectmode=selectmode, show=show, **kwargs)
        self.text.window_create(index, window=widget)

        return widget

    # Bind Functions

    def unbind_tag(self, tag, release=False, both=False):
        """Unbinds a tag."""
        self.text.tag_unbind(tag, "<Button-1>" if not release else "<ButtonRelease-1>")
        if both:
            self.text.tag_unbind(tag, "<Button-1>")
        self.text.tag_unbind(tag, "<Enter>")
        self.text.tag_unbind(tag, "<Leave>")

    def bind_cursor(self, tag):
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.configure(cursor="hand2"), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.configure(cursor="arrow"), "+")

    def bind_background(self, tag):
        self.text.tag_bind(tag, "<Enter>",
                           lambda *args: self.text.tag_configure(tag,
                                                                 background=self.colour_text_background_active), "+")
        self.text.tag_bind(tag, "<Leave>",
                           lambda *args: self.text.tag_configure(tag, background=self.colour_text_background), "+")

    # Insert Spaces

    def insert_new_line(self, *args):
        """Adds a new line to the game."""
        self.text.insert("end", "\n")

    def insert_space(self, *args):
        """Adds a space to the game."""
        self.text.insert("end", " ")

    def insert_tab(self, *args):
        """Adds a tab to the game."""
        self.text.insert("end", "\t")

    # Tag Functions

    def new_tag(self, tag: str, **options):
        """Creates a new tag."""
        self.text.tag_configure(tag, options)

    def tag_configure(self, tag: str, **options):
        """Configures an existing tag."""
        self.text.tag_configure(tag, options)

    def tag_delete(self, tag: str):
        """Deletes a tag."""
        self.text.tag_delete(tag)

    def tag_get_all(self, *args):
        """Returns all tags."""
        list_ = []
        for i in self.text.tag_names():
            list_.append(i)
        return list_

    def tag_get_all_type(self, type, *args):
        """Returns all tags starting with a given prefix."""
        list_ = []
        for i in self.text.tag_names():
            if i.split("-")[0] == type:
                list_.append(i)
        return list_

    # Window Functions

    def normal(self, *args):
        """Un-maximizes the window."""
        self.state("normal")

    def maximise(self, *args):
        """Maximizes the window."""
        self.state("zoomed")

    def unfullscreen(self, *args):
        """Un-full-screens the window."""
        self.attributes("-fullscreen", False)

    def fullscreen(self, *args):
        """Makes the window full-screen."""
        self.attributes("-fullscreen", True)

    def add_borders(self, *args):
        """Adds the borders and title bar back to the window."""
        self.overrideredirect(False)

    def remove_borders(self, *args):
        """Removes the borders and title bar from the window."""
        self.overrideredirect(True)

    # Other Functions

    def exit(self, *args):
        """Exits the game."""
        raise SystemExit
