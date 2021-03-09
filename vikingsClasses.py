
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

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return f"Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return ("A Saxon has received {} points of damage").format (damage)
        else:
            return "A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.Viking = Viking
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.Saxon = Saxon
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        import random
        sa_ = random.choice(self.saxonArmy)
        va_ = random.choice(self.vikingArmy)
        Saxon.receiveDamage(Viking.strength) 
        for a in saxonArmy:
            if sa_ <= 0:
                saxonArmy.pop(sa_)
        return Saxon.receiveDamage(Viking.strength)

    def saxonAttack(self):
        import random
        sv = random.choice(self.vikingArmy)
        sa = random.choice(self.saxonArmy)
        Viking.receiveDamage(Saxon.strength) 
        for a in vikingArmy:
            if sv_ <= 0:
                vikingArmy.pop(sv)
        return Viking.receiveDamage(Saxon.strength) 

    def showStatus(self):
        if saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        elif len(saxonArmy) >= 1 and len(vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
        
