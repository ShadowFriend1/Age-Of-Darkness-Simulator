# TODO: finish squad
import numpy as np


class squad:
    def __init__(self, units, coherency=2):
        self.units = units
        self.coherency = coherency

    def get_units(self):
        return self.units

    def join_squad(self, character):
        self.units.append(character)

    def leave_squad(self, character):
        self.units.remove(character)
        return squad(character)

    def check_coherency(self):
        for n in self.units:
            for m in self.units:
                if np.linalg.norm(n.get_position() - m.get_position()) > self.coherency and n is not m:
                    return False
            else:
                return True
