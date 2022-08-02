class wargear:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class weapon(wargear):
    def __init__(self, name, desc, strength, ap, range_inches, type_weapon, shots, rules):
        super().__init__(name, desc)
        self.strength = strength
        self.ap = ap
        self.range_inches = range_inches
        self.type_weapon = type_weapon
        self.shots = shots
        self.rules = rules

