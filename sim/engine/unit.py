import numpy as np


class unit:
    def __init__(self, stats, wargear, rules, position=None):
        if position is None:
            position = [0, 0, 0]
        self.stats = stats
        self.wargear = wargear
        self.rules = rules
        self.position = np.array(position)

    def move(self, move):
        self.position += move

    def get_position(self):
        return self.position

    def get_stat(self, stat):
        return self.stats[stat]

    def get_rules(self):
        return self.rules

    def get_wargear(self):
        return self.wargear
