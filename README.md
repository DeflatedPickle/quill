# quill
A Python library used to create text-based games with TkInter.

[![PyPI](https://img.shields.io/pypi/pyversions/quill.svg)](https://pypi.python.org/pypi/quill)
[![PyPI](https://img.shields.io/pypi/v/quill.svg)](https://pypi.python.org/pypi/quill)

[![PyPI](https://img.shields.io/pypi/dd/quill.svg)](https://pypi.python.org/pypi/quill)
[![PyPI](https://img.shields.io/pypi/dw/quill.svg)](https://pypi.python.org/pypi/quill)
[![PyPI](https://img.shields.io/pypi/dm/quill.svg)](https://pypi.python.org/pypi/quill)

## Getting Started

### Installing The Library

First off, you will need to have Python 3 installed and have Python in your system PATH. Then, you will need to open your systems' command prompt and type: `pip install quill`, this will install this library to your system.

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


class Game(quill.Window):
    def startup(self):
        pass
```

### Creating A Room

`quill` treats functions as rooms, and they should be used as so. We'll first need to make a function.

```python
import quill


class Game(quill.Window):
    def startup(self):
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

LootTables are used to store mass amounts of items, a LootTable is then assigned to a container. When the container is opened, a random item can be picked from the LootTable and added to the players' inventory. They can be created with the `quill.LootTable` class.

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
- `insert_text(index, what)` inserts a string of text.
- `insert_extending_text(index, what, extend, command)` inserts a string of text which changes into a different string once the player clicks on it.
- `insert_command(index, what, command)` inserts a command which can be pressed to run a function.
- `insert_checkbutton(index, variable, what, command)` inserts a checkbutton which can be pressed to change its' state.
- `insert_radiobutton(index, variable, value, what, command)` inserts a radiobutton which can be pressed to change the value of a variable.
- `insert_trigger(index, what, command)` inserts a trigger which can be used run a command once.
- `insert_container(index, loot_table, command)` inserts a container which can be opened to give the player an item.
- `insert_item(index, item)` inserts an item which can be pressed to show its' stats.
- `insert_merchant(index, merchant)` inserts a merchant who can be pressed to show their inventory.

* `insert_newline()` inserts a new line.
* `insert_space()` inserts a space.
* `insert_tab()` inserts a tab.

**Tag Functions**
- `tag_get_all()` returns all current tags of the `tk.Text` widget.
- `tag_get_all_type()` returns all current tags of the `tk.Text` that follow a certain type.

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

        self.insert_text("end", "Game", "Heading-3")
        self.insert_new_line()
        self.insert_new_line()

        self.insert_command("end", "> Start", self.start)
        self.insert_new_line()
        self.insert_command("end", "> Exit", self.exit)
        self.insert_new_line()

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
import tkinter as tk


class Game(quill.Window):
    def startup(self):
        self.variable_full_screen = tk.BooleanVar()
        self.variable_menu = tk.BooleanVar()
        self.variable_difficulty = tk.IntVar()
        self.menu()

    def menu(self, *args):
        self.enable()
        self.clear()

        self.insert_text("end", "Game", "Heading-3")
        self.insert_new_line()
        self.insert_new_line()

        self.insert_command("end", "> Start", self.start)
        self.insert_new_line()
        self.insert_command("end", "> Options", self.options)
        self.insert_new_line()
        self.insert_command("end", "> Exit", self.exit)
        self.insert_new_line()

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

        self.insert_text("end", "Options", "Heading-3")
        self.insert_new_line()
        self.insert_new_line()

        self.insert_text("end", "Window Options", "Heading-4")
        self.insert_new_line()
        self.insert_checkbutton("end", self.variable_full_screen, "Full Screen")
        self.insert_new_line()
        self.insert_checkbutton("end", self.variable_menu, "Show Menu")
        self.insert_new_line()
        self.insert_new_line()

        self.insert_text("end", "Difficulty", "Heading-4")
        self.insert_new_line()
        self.insert_radiobutton("end", self.variable_difficulty, 0, "Very Easy")
        self.insert_new_line()
        self.insert_radiobutton("end", self.variable_difficulty, 1, "Easy")
        self.insert_new_line()
        self.insert_radiobutton("end", self.variable_difficulty, 2, "Medium")
        self.insert_new_line()
        self.insert_radiobutton("end", self.variable_difficulty, 3, "Hard")
        self.insert_new_line()
        self.insert_radiobutton("end", self.variable_difficulty, 4, "Are You Insane?")
        self.insert_new_line()

        self.insert_new_line()
        self.insert_command("end", "< Back", self.menu)

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
