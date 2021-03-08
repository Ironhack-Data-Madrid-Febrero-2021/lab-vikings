
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health  = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, the_damage):
        self.health -= the_damage
        

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def attack(self):
        return self.strength
    def receiveDamage(self, the_damage):
        self.health -= the_damage
        if self.health > self.the_damage:
            print ("Viking", "{self.name}," "still alive has received", "{self.damage}" "points of damage") 
        else:
            print ("Viking dies" "{self.name}," "has died in act of combat")

    def battleCry(self):
        return "Odin Owns You All!"
    
        
    
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
