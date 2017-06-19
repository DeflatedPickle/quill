import quill
import tkinter as tk

game = quill.Window()


def startup():
    game.sword_broken = quill.Item(game, "Broken Sword", {"weapon": {"type": "sword", "damage": 5}}, rarity="Common")
    game.potion_health_small = quill.Item(game, "Small Potion of Health", {"potion": {"type": "health", "amount": 15}},
                                          value=15, rarity="Common")

    game.loot_small_chest = quill.LootTable(game, "Small Chest", [game.sword_broken, game.potion_health_small])

    game.variable_state = tk.IntVar()
    game.variable_maximized = tk.BooleanVar()

    menu()


def menu(*args):
    game.enable()
    game.clear()

    game.insert_text("Maze Game", True, tag="Heading-4")

    game.insert_command("> Start", command=start)
    game.insert_command("> Options", command=options)
    game.insert_command("> Exit", command=game.exit)

    game.goto_end()
    game.disable()


def start(*args):
    game.enable()
    game.clear()

    game.insert_text("Chapter 1", tag="Heading-4")
    game.insert_text("- Awaken", tag="Heading-5")
    game.insert_new_line()

    game.insert_text("You wake up, surrounded by ")
    game.insert_trigger("stone walls", command=None)
    game.insert_text(".")

    game.goto_end()
    game.disable()


def options(*args):
    game.enable()
    game.clear()

    game.insert_text("Options", tag="Heading-3")
    game.insert_new_line()
    game.insert_new_line()

    game.insert_text("Window Options", tag="Heading-4")
    game.insert_new_line()
    game.insert_radiobutton("Normal", game.variable_state, 0, command=check_state)
    game.insert_radiobutton("Full Screen", game.variable_state, 1, command=check_state)
    game.insert_radiobutton("Border-less", game.variable_state, 2, command=check_state)
    game.insert_checkbutton("Maximized", game.variable_maximized, command=check_maximized)
    game.insert_new_line()

    game.insert_new_line()
    game.insert_command("< Back", command=menu)

    game.goto_end()
    game.disable()


def check_state(*args):
    if game.variable_state.get() == 0:
        game.add_borders()
        game.unfullscreen()

    elif game.variable_state.get() == 1:
        game.add_borders()
        game.fullscreen()

    elif game.variable_state.get() == 2:
        game.unfullscreen()
        game.remove_borders()


def check_maximized(*args):
    if game.variable_maximized.get():
        game.normal()
    else:
        game.maximise()


def main():
    startup()
    game.mainloop()


if __name__ == "__main__":
    main()
