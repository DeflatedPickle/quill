# quill
A Python library used to create text-based games with TkInter.

[![PyPI](https://img.shields.io/pypi/pyversions/quill.svg)](https://pypi.python.org/pypi/quill)
[![PyPI](https://img.shields.io/pypi/v/quill.svg)](https://pypi.python.org/pypi/quill)

[![PyPI](https://img.shields.io/pypi/dd/quill.svg)](https://pypi.python.org/pypi/quill)
[![PyPI](https://img.shields.io/pypi/dw/quill.svg)](https://pypi.python.org/pypi/quill)
[![PyPI](https://img.shields.io/pypi/dm/quill.svg)](https://pypi.python.org/pypi/quill)

## Quill Examples

Incase you would like to read some examples of `quill` in action, feel free to read through the included examples;
- `quill_game.py`, a simple game made with `quill`.
- `quill_widgets.py`, a showcase of widgets available.
- `quill_calculator.py`, a simple calculator made with `quill`.

## Getting Started

### Installing The Library

First off, you will need to have Python 3 installed and have Python in your system PATH. Then, you will need to open your system's terminal and type: `pip install quill`, this will install this library to your system.

### Updating The Library

Being in development, this library will occasionally be updated. Since updates are not automatic, when you would like to update the library to get new features, you will need to open your system's terminal and type: `pip install quill --upgrade`, this will then update the library to the latest version.

## Using The Library

To use the library in your code, simply import like so: `import quill`.

### Creating The Window

To create the window, you'll want to subclass `quill.Window`.

```python
import quill


class Game(quill.Window):
    pass
```

After subclassing the `Window` class, you should make use of the classes `startup` function and use it to define your variables.

```python
import quill
from tkinter import IntVar


class Game(quill.Window):
    def startup(self):
        self.variable = IntVar()
```

### Creating A Room

`quill` treats functions as rooms, and they should be used as so. We'll first need to make a function.

```python
import quill
from tkinter import IntVar


class Game(quill.Window):
    def startup(self):
        self.variable = IntVar()

        self.start()
        
    def start(self):
        pass
```

### Creating An Item

With `quill`, you can create items for your player to find throughout the game. They can be created by using the `quill.Item` class.

```python
self.sword_broken = quill.Item(self, "Broken Sword", {"weapon": {"type": "sword", "damage": 5}}, rarity="Common")
```

### Creating A LootTable

LootTables are used to store mass amounts of items, a LootTable is then assigned to a container. When the container is opened, a random item can be picked from the LootTable and added to the player's inventory. They can be created with the `quill.LootTable` class.

```python
self.loot_small_chest = quill.LootTable(self, "Small Chest", [self.sword_broken])
```

### Window Commands

The `Window` class comes with a lot of built-in commands to use, a few of these are needed with every function. You can find a few helpful ones below:

**Modifier Functions**
- `enable()` allows for text to be entered into the `tk.Text` widget.
- `clear()` clears all text from the `tk.Text` widget.
- `disable()` removes the ability for text to be entered into the `tk.Text` widget, without this at the end of the function, the player could enter in whatever text they wanted.
- `goto_end()` scrolls the `tk.Text` widget to the bottom.

**Insert Functions**
- `insert_text(what, fill_line, index, tag)` inserts a string of text.
- `insert_extending_text(what, extend, fill_line, index, command)` inserts a string of text which changes into a different string once the player clicks on it.
- `insert_command(what, fill_line, index, command)` inserts a command which can be pressed to run a function.
- `insert_checkbutton(what, variable, fill_line, index, command)` inserts a checkbutton which can be pressed to change it's state.
- `insert_radiobutton(what, variable, value, fill_line, index, command)` inserts a radiobutton which can be pressed to change the value of a variable.
- `insert_trigger(what, index, command)` inserts a trigger which can be used run a command once.


- `insert_container(loot_table, fill_line, index, command)` inserts a container which can be clicked to give the player an item.
- `insert_item(item, fill_line, index)` inserts an item which can be clicked to show it's stats.
- `insert_merchant(merchant, fill_line, index)` inserts a merchant which can be clicked to show it's inventory.
- `insert_quest(quest, fill_line, index)` inserts a quest which can be clicked to show it's inventory.

**Insert Spaces**

- `insert_newline()` inserts a new line.
- `insert_space()` inserts a space.
- `insert_tab()` inserts a tab.

**Insert Widgets**

- `insert_tk_button()` inserts a `tk.Button`.
- `insert_tk_checkbutton()` inserts a `tk.Checkbutton`.
- `insert_tk_entry()` inserts a `tk.Entry`.
- `insert_tk_frame()` inserts a `tk.Frame`.
- `insert_tk_label()` inserts a `tk.Label`.
- `insert_tk_labelframe()` inserts a `tk.LabelFrame`.
- `insert_tk_menubutton()` inserts a `tk.Menubutton`.
- `insert_tk_panedwindow()` inserts a `tk.PanedWindow`.
- `insert_tk_radiobutton()` inserts a `tk.Radiobutton`.
- `insert_tk_scale()` inserts a `tk.Scale`.
- `insert_tk_scrollbar()` inserts a `tk.Scrollbar`.


- `insert_tk_canvas` inserts a `tk.Canvas`.
- `insert_tk_listbox` inserts a `tk.Listbox`.
- `insert_tk_message` inserts a `tk.Listbox`.
- `insert_tk_text` inserts a `tk.Text`.
- `insert_tk_spinbox` insert a `tk.Spinbox`.


- `insert_ttk_button()` insert a `ttk.Button`.
- `insert_ttk_checkbutton()` inserts a `ttk.Checkbutton`.
- `insert_ttk_entry()` inserts a `ttk.Entry`.
- `insert_ttk_frame()` inserts a `ttk.Frame`.
- `insert_ttk_label()` inserts a `ttk.Label`.
- `insert_ttk_labelframe()` inserts a `ttk.LabelFrame`.
- `insert_ttk_menubutton()` inserts a `ttk.Menubutton`.
- `insert_ttk_panedwindow()` inserts a `ttk.PanedWindow`.
- `insert_ttk_radiobutton()` inserts a `ttk.Radiobutton`.
- `insert_ttk_scale()` inserts a `ttk.Scale`.
- `insert_ttk_scrollbar()` inserts a `ttk.Scrollbar`.


- `insert_ttk_combobox()` inserts a `ttk.Combobox`.
- `insert_ttk_notebook()` inserts a `ttk.Notebook`.
- `insert_ttk_progressbar()` inserts a `ttk.Progressbar`.
- `insert_ttk_separator()` inserts a `ttk.Separator`.
- `insert_ttk_treeview()` inserts a `ttk.Treeview`.

**Tag Functions**
- `new_tag()` create a new tag.
- `tag_configure()` configure an existing tag.
- `tag_delete()` deletes an existing tag.
- `tag_get_all()` returns all current tags of the `tk.Text` widget.
- `tag_get_all_type()` returns all current tags of the `tk.Text` that follow a certain type.

**Window Functions**
- `normal()` un-maximizes the window
- `maximise()` maximizes the window
- `unfullscreen()` un-full-screens the window
- `fullscreen()` makes the window full-screen
- `add_borders()` adds the borders and title bar back to the window
- `remove_borders()` removes the borders and title bar from the window

**Other Functions**
- `exit()` exits the game.

### Creating A Menu

Most games these days have menus, and it'd be a good idea to have one. Thankfully, menus can easily be made with `quill`.

#### Creating The Start Menu

```python
import quill


class Game(quill.Window):
    def startup(self):
        self.menu()
        
    def menu(self, *args):
        self.enable()
        self.clear()

        self.insert_text("Maze Game", True, tag="Heading-4")

        self.insert_command("> Start", command=self.start)
        self.insert_command("> Exit", command=self.exit)

        self.goto_end()
        self.disable()

    def start(self, *args):
        self.enable()
        self.clear()

        self.goto_end()
        self.disable()
```

#### Creating The Option Menu

You might find that you want an option menu in your game. These can also be made easily.

```python
import quill
from tkinter import BooleanVar, IntVar


class Game(quill.Window):
    def startup(self):
        self.variable_full_screen = BooleanVar()
        self.variable_menu = BooleanVar()
        self.variable_difficulty = IntVar()
        self.menu()

    def menu(self, *args):
        self.enable()
        self.clear()

        self.insert_text("Maze Game", True, tag="Heading-3")

        self.insert_command("> Start", command=self.start)
        self.insert_command("> Options", command=self.options)
        self.insert_command("> Exit", command=self.exit)

        self.goto_end()
        self.disable()

    def start(self, *args):
        self.enable()
        self.clear()

        self.goto_end()
        self.disable()

    def options(self, *args):
        self.enable()
        self.clear()

        self.insert_text("Options", tag="Heading-3")
        self.insert_new_line()

        self.insert_text("Window Options", True, tag="Heading-4")
        self.insert_checkbutton("Full Screen", self.variable_full_screen)
        self.insert_checkbutton("Show Menu", self.variable_menu)
        self.insert_new_line()

        self.insert_text("Difficulty", tag="Heading-4")
        self.insert_radiobutton("Very Easy", self.variable_difficulty, 0)
        self.insert_radiobutton("Easy", self.variable_difficulty, 1)
        self.insert_radiobutton("Medium", self.variable_difficulty, 2)
        self.insert_radiobutton("Hard", self.variable_difficulty, 3)
        self.insert_radiobutton("Are You Insane?", self.variable_difficulty, 4)
        self.insert_new_line()

        self.insert_new_line()
        self.insert_command("< Back", command=self.menu)

        self.goto_end()
        self.disable()
```

### Running Your Game

At some point, you will find that you actually want to play your game. Put this at the bottom of your script to run it:

```python
def main():
    app = Game(title="Maze Game")
    app.mainloop()

if __name__ == "__main__":
    main()
```
