import numpy as np


class unit:
    def __init__(self, stats, wargear, rules, unit_types, height, base_size=None, position=None, footprint=None):
        if position is None:
            position = [0, 0, 0]
        self.stats = stats
        self.wargear = wargear
        self.rules = rules
        self.unit_types = unit_types
        self.height = height
        self.base_size = base_size
        self.position = np.array(position)
        self.footprint = footprint

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
