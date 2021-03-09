
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health -= damage

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War
import numpy as np
import random

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        receiveDamage(Saxon) == Viking.strength
        if receiveDamage(Saxon) < 0:
            self.saxonArmy -= 1
        else:
            self.saxonArmy += 0
    def saxonAttack(self):
        receiveDamage(Viking) == Saxon.strength
        if receiveDamage(Viking) < 0:
            self.vikingArmy -= 1
        else:
            self.vikingArmy += 0
    def showStatus(self):
        if saxonArmy < 1 and vikingArmy >= 1:
            return "Vikings have won the war of the century!"
        elif vikingArmy < 1 and saxonArmy >=1:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
