import quill
import tkinter as tk


class Game(quill.Window):
    def startup(self):
        self.sword_broken = quill.Item(self, "Broken Sword", {"weapon": {"type": "sword", "damage": 5}},
                                           rarity="Common")
        self.sword_of_doom = quill.Item(self, "Sword of Doom", {"weapon": {"type": "sword", "damage": 150}},
                                            rarity="Legendary")
        self.potion_small_health = quill.Item(self, "Small Potion of Health", {"potion": {"type": "health", "amount": 15}}, rarity="Common")
        self.potion_medium_health = quill.Item(self, "Medium Potion of Health", {"potion": {"type": "health", "amount": 30}}, rarity="Uncommon")
        self.potion_large_health = quill.Item(self, "Large Potion of Health", {"potion": {"type": "health", "amount": 50}}, rarity="Rare")

        self.loot_small_chest = quill.LootTable(self, "Small Chest", [self.sword_broken, self.potion_small_health, self.potion_medium_health, self.potion_large_health])

        self.variable_state = tk.IntVar()
        self.variable_maximized = tk.BooleanVar()

        self.menu()

    def menu(self, *args):
        self.enable()
        self.clear()

        self.insert_text("end", "Maze Game", tag="Heading-4")
        self.insert_new_line()

        self.insert_command("end", "> Start\n", command=self.start)
        self.insert_command("end", "> Options\n", command=self.options)
        self.insert_command("end", "> Exit\n", command=self.exit)

        self.goto_end()
        self.disable()

    def start(self, *args):
        self.enable()
        self.clear()

        self.insert_text("end", "Chapter 1", tag="Heading-4")
        self.insert_text("end", "- Awaken", tag="Heading-5")
        self.insert_new_line()

        self.insert_text("end", "You wake up, surrounded by ")
        self.insert_trigger("end", "stone walls", self.stone_walls)
        self.insert_text("end", ".")

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
        self.insert_radiobutton("end", self.variable_state, 0, "Normal", command=self.check_state)
        self.insert_new_line()
        self.insert_radiobutton("end", self.variable_state, 1, "Full Screen", command=self.check_state)
        self.insert_new_line()
        self.insert_radiobutton("end", self.variable_state, 2, "Border-less", command=self.check_state)
        self.insert_new_line()
        self.insert_checkbutton("end", self.variable_maximized, "Maximized", command=self.check_maximized)
        self.insert_new_line()
        self.insert_new_line()

        self.insert_new_line()
        self.insert_command("end", "< Back", self.menu)

        self.goto_end()
        self.disable()

    def check_state(self, *args):
        if self.variable_state.get() == 0:
            self.add_borders()
            self.unfullscreen()

        elif self.variable_state.get() == 1:
            self.add_borders()
            self.fullscreen()

        elif self.variable_state.get() == 2:
            self.unfullscreen()
            self.remove_borders()

    def check_maximized(self, *args):
        if self.variable_maximized.get():
            self.normal()
        else:
            self.maximise()

    def stone_walls(self, *args):
        self.enable()
        self.insert_new_line()
        self.insert_new_line()

        self.insert_text("end", "You search the walls. Upon inspection, you notice that the walls are ")
        self.insert_extending_text("end", "...", "dirty")
        self.insert_text("end", ". You brush a bit of dirt off and find a bit of wall weak enough to ")
        self.insert_trigger("end", "break through", self.break_through)

        self.goto_end()
        self.disable()

    def break_through(self, *args):
        self.enable()
        self.insert_new_line()
        self.insert_new_line()

        self.insert_text("end", "You take a few steps back before ramming your shoulder into the wall. The wall crumbles as you smash through. In front of you lies a ")
        self.insert_trigger("end", "long path", self.long_path)
        self.insert_text("end", ". You also notice a ")
        self.insert_container("end", self.loot_small_chest, self.small_chest)
        self.insert_text("end", " tucked away in the corner of the room.")

        self.disable_extend("Extend-dirty-normal")
        self.goto_end()
        self.disable()

    def long_path(self, *args):
        self.enable()
        self.insert_new_line()
        self.insert_new_line()

        if self.check_container("Container-SmallChest"):
            self.insert_text("end", "You ignore the chest and make your way down the path. ")
        else:
            self.insert_text("end", "You take whatever was in the chest and make your way down the path. ")
        self.insert_text("end", "You stroll down the long path till you come to a split in the path. To the right of you, there's a ")
        self.insert_trigger("end", "foggy path", self.foggy_path)
        self.insert_text("end", " and in front of you, the ")
        self.insert_trigger("end", "path continues", self.path_continues)
        self.insert_text("end", ".")

        self.lock_container("Container-SmallChest")
        self.goto_end()
        self.disable()

    def small_chest(self, *args):
        self.enable()
        self.insert_new_line()
        self.insert_new_line()

        self.insert_text("end", "You walk towards the chest and open it. Inside of the chest was a ")
        self.insert_item("end", self.sword_broken)
        self.insert_text("end", ".")

        self.goto_end()
        self.disable()

    def foggy_path(self, *args):
        self.enable()
        self.insert_new_line()
        self.insert_new_line()

        self.insert_text("end", "You turn to the right and head down the foggy path.")

        self.toggle_trigger("Trigger-pathcontinues")
        self.goto_end()
        self.disable()

    def path_continues(self, *args):
        self.enable()
        self.insert_new_line()
        self.insert_new_line()

        self.insert_text("end", "You continue to walk forwards and finally exit the fog.")

        self.toggle_trigger("Trigger-foggypath")
        self.goto_end()
        self.disable()


def main():
    app = Game(title="Maze Game")
    app.mainloop()

if __name__ == "__main__":
    main()
