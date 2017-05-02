__title__ = "Item"
__author__ = "DeflatedPickle"
__version__ = "1.0.0"


class Item(object):
    """Creates an item."""
    def __init__(self, window, name: str, info: dict, description="", value=0, rarity="Common"):
        self.window = window
        self.name = name
        self.description = description
        self.value = value
        self.info = info
        self.rarity = rarity

        for key in self.info:
            # print(key)
            if key in self.window.valid_item_arguments:
                for sub_key in self.info[key]:
                    # print(sub_key, ":", self.info[key][sub_key])
                    if sub_key in self.window.valid_item_arguments[key]:
                        if sub_key == "info":
                            if self.info[key][sub_key] in self.window.valid_item_infos[key]:
                                pass
                            else:
                                print("{} is not a valid item info.".format(self.info[key][sub_key]))
                    else:
                        print("{} is not a valid item argument.".format(sub_key))
            else:
                print("{} is not a valid item info.".format(key))

        if self.rarity in self.window.valid_item_rarities:
            pass
        else:
            print("{} is not a valid item rarity.".format(self.rarity))

    def show_stats(self, *args):
        self.window.enable()
        self.window.insert_new_line()
        self.window.insert_new_line()

        self.window.text.insert("end", "Name: {}\nInfo: {}\nRarity: {}\n".format(self.name, self.info, self.rarity),
                                "Quote")

        self.window.goto_end()
        self.window.disable()
