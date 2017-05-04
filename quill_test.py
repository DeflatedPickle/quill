import quill
from quill.merchant import Merchant
from quill.quest import Quest
import tkinter as tk


class Game(quill.Window):
    def startup(self):
        self.sword_broken = quill.Item(self, "Broken Sword", {"weapon": {"type": "sword", "damage": 5}},
                                       rarity="Common")
        self.sword_of_doom = quill.Item(self, "Sword of Doom", {"weapon": {"type": "sword", "damage": 150}},
                                        rarity="Legendary")
        self.potion_small_health = quill.Item(self, "Small Potion of Health",
                                              {"potion": {"type": "health", "amount": 15}}, rarity="Common")
        self.potion_medium_health = quill.Item(self, "Medium Potion of Health",
                                               {"potion": {"type": "health", "amount": 30}}, rarity="Uncommon")
        self.potion_large_health = quill.Item(self, "Large Potion of Health",
                                              {"potion": {"type": "health", "amount": 50}}, rarity="Rare")

        self.loot_small_chest = quill.LootTable(self, "Small Chest", [self.sword_broken,
                                                                      self.potion_small_health,
                                                                      self.potion_medium_health,
                                                                      self.potion_large_health])

        self.merchant_frank_lyatut = Merchant(self, name="Frank Lyatut", price_difference=0,
                                              inventory=[self.potion_small_health,
                                                         self.potion_medium_health], money=100)

        self.simple_quest = Quest(self, "Simple Quest", [self.sword_of_doom], "Do something.",
                                  "You were told to do something.")

        self.variable_state = tk.IntVar()
        self.variable_maximized = tk.BooleanVar()

        self.menu()

    def menu(self, *args):
        self.enable()
        self.clear()

        self.insert_text("Maze Game", tag="Heading-4")
        self.insert_new_line()

        self.insert_command("> Start\n", command=self.start)
        self.insert_command("> Options\n", command=self.options)
        self.insert_command("> Exit\n", command=self.exit)

        self.goto_end()
        self.disable()

    def start(self, *args):
        self.enable()
        self.clear()

        self.insert_text("Chapter 1", tag="Heading-4")
        self.insert_text("- Awaken", tag="Heading-5")
        self.insert_new_line()

        self.insert_text("You wake up, surrounded by ")
        self.insert_trigger("stone walls", command=self.stone_walls)
        self.insert_text(".")

        self.goto_end()
        self.disable()

    def options(self, *args):
        self.enable()
        self.clear()

        self.insert_text("Options", tag="Heading-3")
        self.insert_new_line()
        self.insert_new_line()

        self.insert_text("Window Options", tag="Heading-4")
        self.insert_new_line()
        self.insert_radiobutton(self.variable_state, 0, "Normal", command=self.check_state)
        self.insert_new_line()
        self.insert_radiobutton(self.variable_state, 1, "Full Screen", command=self.check_state)
        self.insert_new_line()
        self.insert_radiobutton(self.variable_state, 2, "Border-less", command=self.check_state)
        self.insert_new_line()
        self.insert_checkbutton(self.variable_maximized, "Maximized", command=self.check_maximized)
        self.insert_new_line()
        self.insert_new_line()

        self.insert_new_line()
        self.insert_command("< Back", command=self.menu)

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

        self.insert_text("You search the walls. Upon inspection, you notice that the walls are ")
        self.insert_extending_text("...", extend="dirty")
        self.insert_text(". You brush a bit of dirt off and find a bit of wall weak enough to ")
        self.insert_trigger("break through", command=self.break_through)

        self.goto_end()
        self.disable()

    def break_through(self, *args):
        self.enable()
        self.insert_new_line()
        self.insert_new_line()

        self.insert_text("You take a few steps back before ramming your shoulder into the wall. The wall "
                         "crumbles as you smash through. In front of you lies a ")
        self.insert_trigger("long path", command=self.long_path)
        self.insert_text(". You also notice a ")
        # self.insert_container("end", self.loot_small_chest, self.small_chest)
        self.insert_container(self.loot_small_chest, command=self.open_small_chest)
        self.insert_text(" tucked away in the corner of the room.")

        self.disable_extend("Extend-dirty-normal")
        self.goto_end()
        self.disable()

    def long_path(self, *args):
        self.enable()
        self.insert_new_line()
        self.insert_new_line()

        if self.check_container("Container-SmallChest"):
            self.insert_text("You ignore the chest and make your way down the path. ")
        else:
            self.insert_text("You take whatever was in the chest and make your way down the path. ")
        self.insert_text("You stroll down the long path till you come to a split in the path. To the right of "
                         "you, there's a ")
        self.insert_trigger("foggy path", command=self.foggy_path)
        self.insert_text(" and in front of you, the ")
        self.insert_trigger("path continues", command=self.path_continues)
        self.insert_text(".")

        self.lock_container("Container-SmallChest")
        self.goto_end()
        self.disable()

    def open_small_chest(self, *args):
        self.enable()
        self.insert_new_line()
        self.insert_new_line()

        item = self.loot_small_chest.open()
        self.insert_text("You found a ")
        self.insert_item(item)
        self.insert_text(".")

        self.goto_end()
        self.disable()

    def foggy_path(self, *args):
        self.enable()
        self.insert_new_line()
        self.insert_new_line()

        self.insert_text("You turn to the right and head down the foggy path. ")
        self.insert_trigger("Keep Going", command=self.keep_going)
        self.insert_text(".")

        self.toggle_trigger("Trigger-pathcontinues")
        self.goto_end()
        self.disable()

    def keep_going(self, *args):
        self.enable()
        self.insert_new_line()
        self.insert_new_line()

        self.insert_text("You keep walking down the path. As you walk, you start to see a shadow. You hear a "
                         "faint voice and keep walking towards the figure. You see the figure in plain sight, "
                         "and it turns out to be a merchant, sitting down. They introduce themselves, they're "
                         "called ")
        self.insert_merchant(self.merchant_frank_lyatut)
        self.insert_text(".")

        self.goto_end()
        self.disable()

    def path_continues(self, *args):
        self.enable()
        self.insert_new_line()
        self.insert_new_line()

        self.insert_text("You continue to walk forwards and finally exit the fog. You look around. You are in ")
        self.insert_extending_text("...", extend="a large gray cube")
        self.insert_text(". Below you notice a ")
        self.insert_extending_text("look down", extend="note")
        self.insert_text(".")

        self.toggle_trigger("Trigger-foggypath")
        self.goto_end()
        self.disable()


def main():
    app = Game(title="Maze Game")
    app.mainloop()


if __name__ == "__main__":
    main()
