import tkinter as tk
from tkinter import ttk
from tkinter import font
import re

from .player import *

__title__ = "Window"
__author__ = "DeflatedPickle"
__version__ = "1.0.0"


class Window(tk.Tk):
    """Creates the window used for the game."""
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

        self.colour_extend_on = "turquoise"
        self.colour_extend_off = "slate blue"

        self.colour_check_on = "green"
        self.colour_check_off = "red"

        self.colour_radio_on = "green"
        self.colour_radio_off = "red"

        self.colour_trigger_on = "green"
        self.colour_trigger_off = "red"

        self.colour_container_on = "orange"
        self.colour_container_off = "cyan"

        self.colour_item_on = "gold"
        self.colour_item_off = "purple"

        self.colour_merchant_on = "gold"
        self.colour_merchant_off = "purple"

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

    def enable(self):
        """Must be used before inserting anything."""
        self.text.configure(state="normal")

    def disable(self):
        """Used to disable the text."""
        self.text.configure(state="disable")

    def insert_text(self, index: int or str, what: str, tag="Paragraph"):
        """Inserts a string of text into the game."""
        self.text.insert(index, what, tag)

    def insert_extending_text(self, index: int or str, what: str, extend: str, command=None):
        """Inserts a string of text that can be extended."""
        tag = "Extend-{}-{}".format(re.sub("[^0-9a-zA-Z]+", "", extend), "normal")
        tag2 = "Extend-{}-{}".format(re.sub("[^0-9a-zA-Z]+", "", extend), "extend")
        self.text.tag_configure(tag, foreground=self.colour_extend_on, elide=False)
        self.text.tag_configure(tag2, foreground=self.colour_extend_off, elide=True)
        self.text.insert(index, what, tag)
        self.text.insert(index, extend, tag2)

        self.text.tag_unbind(tag, "<Button-1>")
        self.text.tag_unbind(tag, "<Enter>")
        self.text.tag_unbind(tag, "<Leave>")

        self.text.tag_bind(tag, "<Button-1>", command, "+")
        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_extend(tag, tag2), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.configure(cursor="hand2"), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background_active), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.configure(cursor="arrow"), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background), "+")

    def toggle_extend(self, tag, tag2):
        """Toggles an extending text off."""
        self.text.tag_configure(tag, elide=True)
        self.text.tag_configure(tag2, elide=False)

    def disable_extend(self, tag):
        """Disables an extending text."""
        self.text.tag_configure(tag, foreground=self.colour_extend_off)
        self.text.tag_unbind(tag, "<Button-1>")

    def insert_command(self, index: int or str, what: str, command=None):
        """Inserts a click-able command into the game."""
        tag = "Command-{}".format(re.sub("[^0-9a-zA-Z]+", "", what))
        self.text.tag_configure(tag, foreground=self.colour_command)
        self.text.insert(index, what, tag)

        self.text.tag_unbind(tag, "<Button-1>")
        self.text.tag_unbind(tag, "<Enter>")
        self.text.tag_unbind(tag, "<Leave>")

        self.text.tag_bind(tag, "<Button-1>", command, "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.configure(cursor="hand2"), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background_active), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.configure(cursor="arrow"), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background), "+")

    def insert_checkbutton(self, index: int or str, variable, what: str, command=None):
        """Insert a checkbutton into the game."""
        tag = "Check-{}".format(re.sub("[^0-9a-zA-Z]+", "", what))
        if variable.get():
            self.text.tag_configure(tag, foreground=self.colour_check_on)
        elif not variable.get():
            self.text.tag_configure(tag, foreground=self.colour_check_off)
        self.text.insert(index, what, tag)

        self.text.tag_unbind(tag, "<Button-1>")
        self.text.tag_unbind(tag, "<Enter>")
        self.text.tag_unbind(tag, "<Leave>")

        self.text.tag_bind(tag, "<Button-1>", command, "+")
        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_check(variable, tag), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.configure(cursor="hand2"), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background_active), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.configure(cursor="arrow"), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background), "+")

    def toggle_check(self, variable, tag, *args):
        """Toggles a checkbutton."""
        variable.set(not variable.get())
        if variable.get():
            self.text.tag_configure(tag, foreground=self.colour_check_on)
        elif not variable.get():
            self.text.tag_configure(tag, foreground=self.colour_check_off)

    def insert_radiobutton(self, index: int or str, variable, value, what: str, command=None):
        """Inserts a radiobutton into the game."""
        tag = "Radio-{}-{}".format(re.sub("[^0-9a-zA-Z]+", "", str(variable)), str(value))
        if variable.get() == value:
            self.text.tag_configure(tag, foreground=self.colour_radio_on)
        elif variable.get() != value:
            self.text.tag_configure(tag, foreground=self.colour_radio_off)
        self.text.insert(index, what, tag)

        self.text.tag_unbind(tag, "<Button-1>")
        self.text.tag_unbind(tag, "<Enter>")
        self.text.tag_unbind(tag, "<Leave>")

        self.text.tag_bind(tag, "<Button-1>", command, "+")
        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_radio(variable, value, tag), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.configure(cursor="hand2"), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background_active), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.configure(cursor="arrow"), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background), "+")

    def toggle_radio(self, variable, value, tag):
        """Toggles a radiobutton."""
        variable.set(value)
        for i in self.text.tag_names():
            if "{}_{}".format(i[:8], i[8:])[:-2] == "Radio-{}".format(str(variable)):
                self.text.tag_configure(i, foreground=self.colour_radio_off)

        if variable.get() == value:
            self.text.tag_configure(tag, foreground=self.colour_radio_on)
        elif variable.get() != value:
            self.text.tag_configure(tag, foreground=self.colour_radio_off)

    def insert_trigger(self, index: int or str, what: str, command=None):
        """Inserts a trigger into the game."""
        tag = "Trigger-{}".format(re.sub("[^0-9a-zA-Z]+", "", what))
        self.text.tag_configure(tag, foreground=self.colour_trigger_on)
        self.text.insert(index, what, tag)

        self.text.tag_unbind(tag, "<Button-1>")
        self.text.tag_unbind(tag, "<Enter>")
        self.text.tag_unbind(tag, "<Leave>")

        self.text.tag_bind(tag, "<Button-1>", command, "+")
        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_trigger(tag), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.configure(cursor="hand2"), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background_active), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.configure(cursor="arrow"), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background), "+")

    def toggle_trigger(self, tag):
        """Toggles a trigger off."""
        self.text.tag_configure(tag, foreground=self.colour_trigger_off)
        self.text.tag_unbind(tag, "<Button-1>")

    def check_trigger(self, tag):
        """Checks the value of a trigger."""
        if self.text.tag_cget(tag, "foreground") == self.colour_trigger_on:
            return True
        elif self.text.tag_cget(tag, "foreground") == self.colour_trigger_off:
            return False

    def insert_container(self, index: int or str, loot_table, command=None):
        """Insert a checkbutton into the game."""
        tag = "Container-{}".format(re.sub("[^0-9a-zA-Z]+", "", loot_table.name))
        self.text.tag_configure(tag, foreground=self.colour_container_on)
        self.text.insert(index, loot_table.name, tag)

        self.text.tag_unbind(tag, "<Button-1>")
        self.text.tag_unbind(tag, "<Enter>")
        self.text.tag_unbind(tag, "<Leave>")

        self.text.tag_bind(tag, "<Button-1>", command, "+")
        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.open_container(loot_table, tag), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.configure(cursor="hand2"), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background_active), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.configure(cursor="arrow"), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background), "+")

    def open_container(self, loot_table, tag, *args):
        """Opens a container."""
        loot_table.open()
        self.text.tag_configure(tag, foreground=self.colour_container_off)
        self.text.tag_unbind(tag, "<Button-1>")

    def lock_container(self, tag):
        """Locks a container."""
        self.text.tag_configure(tag, foreground=self.colour_container_off)
        self.text.tag_unbind(tag, "<Button-1>")

    def check_container(self, tag):
        """Checks the value of a container."""
        if self.text.tag_cget(tag, "foreground") == self.colour_container_on:
            return True
        elif self.text.tag_cget(tag, "foreground") == self.colour_container_off:
            return False

    def insert_item(self, index: int or str, item):
        """Inserts an item into the game."""
        tag = "Item-{}".format(re.sub("[^0-9a-zA-Z]+", "", item.name))
        self.text.tag_configure(tag, foreground=self.colour_item_on)
        self.text.insert(index, item.name, tag)

        self.text.tag_unbind(tag, "<Button-1>")
        self.text.tag_unbind(tag, "<Enter>")
        self.text.tag_unbind(tag, "<Leave>")

        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_item(item, tag), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.configure(cursor="hand2"), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background_active), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.configure(cursor="arrow"), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background), "+")

    def toggle_item(self, item, tag, *args):
        """Toggles an item."""
        item.show_stats()
        self.text.tag_configure(tag, foreground=self.colour_item_off)

    def insert_merchant(self, index: int or str, merchant):
        """Inserts an merchant into the game."""
        tag = "Merchant-{}".format(re.sub("[^0-9a-zA-Z]+", "", merchant.name))
        self.text.tag_configure(tag, foreground=self.colour_merchant_on)
        self.text.insert(index, merchant.name, tag)

        self.text.tag_unbind(tag, "<Button-1>")
        self.text.tag_unbind(tag, "<Enter>")
        self.text.tag_unbind(tag, "<Leave>")

        self.text.tag_bind(tag, "<Button-1>", lambda *args: self.toggle_merchant(merchant, tag), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.configure(cursor="hand2"), "+")
        self.text.tag_bind(tag, "<Enter>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background_active), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.configure(cursor="arrow"), "+")
        self.text.tag_bind(tag, "<Leave>", lambda *args: self.text.tag_configure(tag, background=self.colour_text_background), "+")

    def toggle_merchant(self, merchant, tag, *args):
        """Toggles a merchant."""
        merchant.show_inventory()
        self.text.tag_configure(tag, foreground=self.colour_merchant_off)

    def insert_new_line(self):
        """Adds a new line to the game."""
        self.text.insert("end", "\n")

    def insert_space(self):
        """Adds a space to the game."""
        self.text.insert("end", " ")

    def insert_tab(self):
        """Adds a tab to the game."""
        self.text.insert("end", "\t")

    def new_tag(self, tag: str, **options):
        """Creates a new tag."""
        self.text.tag_configure(tag, options)

    def tag_configure(self, tag: str, **options):
        """Configures an existing tag."""
        self.text.tag_configure(tag, options)

    def tag_delete(self, tag: str):
        """Deletes a tag."""
        self.text.tag_delete(tag)

    def tag_get_all(self):
        """Returns all tags."""
        list_ = []
        for i in self.text.tag_names():
            list_.append(i)
        return list_

    def tag_get_all_type(self, type):
        """Returns all tags starting with a given prefix."""
        list_ = []
        for i in self.text.tag_names():
            if i.split("-")[0] == type:
                list_.append(i)
        return list_

    def clear(self):
        """Clears all text from the game."""
        self.text.delete(1.0, "end")

    def goto_end(self):
        """Scrolls the text widget to the bottom."""
        self.text.see("end")

    def exit(self, *args):
        """Exits the game."""
        raise SystemExit
