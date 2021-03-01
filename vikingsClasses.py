
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health  = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, the_damage):
        self.health = {"the_damage"} - {"health"}
        

# Viking


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
