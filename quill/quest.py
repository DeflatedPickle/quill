__title__ = "Quest"
__author__ = "DeflatedPickle"
__version__ = "1.1.0"


class Quest(object):
    """Creates an quest."""
    def __init__(self, name: str, reward: str, goal: str, description=""):
        self.name = name
        self.reward = reward
        self.goal = goal
        self.description = description

    def complete(self, *args):
        """Complete the Quest."""
        pass

    def fail(self, *args):
        """Fail a Quest."""
        pass

    def hand_in(self, *args):
        """Hand in a Quest."""
        pass
