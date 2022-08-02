class wargear:
    def __init__(self, name, desc, type_gear):
        self.name = name
        self.desc = desc
        self.type_gear = type_gear

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.desc

    def get_type_gear(self):
        return self.type_gear

class weapon(wargear):
    def __init__(self, name, desc, type_gear, strength, ap, range_inches, type_weapon, shots, rules):
        super().__init__(name, desc, type_gear)
        self.strength = strength
        self.ap = ap
        self.range_inches = range_inches
        self.type_weapon = type_weapon
        self.shots = shots
        self.rules = rules

    def get_strength(self):
        return self.strength

    def get_ap(self):
        return self.ap

    def get_range_inches(self):
        return self.range_inches

    def get_type_weapon(self):
        return self.type_weapon

    def get_shots(self):
        return self.shots

    def get_rules(self):
        return self.rules
