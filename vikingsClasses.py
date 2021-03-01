
# Soldier
'''Modify the `Soldier` constructor function and add 2 methods to its prototype: `attack()`, and `receiveDamage()`.

#### constructor function

- should receive **2 arguments** (health & strength)
- should receive the **`health` property** as its **1st argument**
- should receive the **`strength` property** as its **2nd argument**

#### `attack()` method

- should be a function
- should receive **0 arguments**
- should return **the `strength` property of the `Soldier`**

#### `receiveDamage()` method

- should be a function
- should receive **1 argument** (the damage)
- should remove the received damage from the `health` property
- **shouldn't return** anything

---
'''

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage



# Viking


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
