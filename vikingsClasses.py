
# Soldier

import random

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
        super().__init__(health,strength)
        self.name = name
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if (self.health > 0):
            return f'{self.name} has received {damage} points of damage'
        if (self.health <= 0):
            return f'{self.name} has died in act of combat'
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)


    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        if self.health <= 0:
            return f'A Saxon has died in combat'


# War

class War:
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)  
    def addSaxon(self, Saxon):
        #if isinstance(saxon, Saxon)
        self.saxonArmy.append(Saxon)



    def vikingAttack(self):
        elegido_vikin = random.choice(self.vikingArmy)
        elegido_saxon = random.choice(self.saxonArmy)
        result = elegido_saxon.receiveDamage(elegido_vikin.attack()) 

        if result ==  'A Saxon has died in combat':
            self.saxonArmy.remove(elegido_saxon)
        return result












    def saxonAttack(self):
        elegido_vikin = random.choice(self.vikingArmy)
        elegido_saxon = random.choice(self.saxonArmy)
        resulta = elegido_vikin.receiveDamage(elegido_saxon.attack())

        if resulta == f"{elegido_vikin.name} has died in act of combat":
            self.vikingArmy.remove(elegido_vikin)
        return resulta
        



    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

           


