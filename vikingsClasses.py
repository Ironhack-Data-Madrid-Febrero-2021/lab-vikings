
# Soldier


class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    def attack (self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health -= damage
        if (self.health > 0):
            return f'{self.name} has received {damage} points of damage'
        if (self.health == 0):
            return f'{self.name} has died in act of combat'
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        if self.health == 0:
            return f'A Saxon has died in combat'


# War

class War:
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        pass  

    def saxonAttack(self):
        pass
        
    def showStatus(self):
        if self.saxonArmy == 0:
            return "Vikings have won the war of the century!"
        if self.vikingArmy == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thinck of battle"


