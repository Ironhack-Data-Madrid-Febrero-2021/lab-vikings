import unittest
from vikingsClasses import Saxon
from inspect import signature


class TestSaxon(unittest.TestCase):

    class Saxon(Soldier):

        def __init__(self,health,strength):
            self.health = health
            self.strength = strength
        

    def receiveDamage(self,damage):
        self.health=damage
        if self.health>0:
                return f"A Saxon has received {damage} points of damage"
        if self.health<0:
                return "A Saxon has died in act of combat"

    def testSaxonShouldReceiveTwoParams(self):
        self.assertEqual(len(signature(Saxon).parameters), 2)

    def testHealth(self):
        self.assertEqual(self.saxon.health, self.health)

    def testStrength(self):
        self.assertEqual(self.saxon.strength, self.strength)

    def testAttack(self):
        self.assertEqual(callable(self.saxon.attack), True)

    def testAttackShouldReceiveNoParams(self):
        self.assertEqual(len(signature(self.saxon.attack).parameters), 0)

    def testAttackREturnStrength(self):
        self.assertEqual(self.saxon.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        self.assertEqual(callable(self.saxon.receiveDamage), True)

    def testReceiveDamageShouldReceiveOneParam(self):
        self.assertEqual(
            len(signature(self.saxon.receiveDamage).parameters), 1)

    def testReceiveDamage(self):
        self.saxon.receiveDamage(1)
        self.assertEqual(self.saxon.health, self.health - 1)

    def testReceiveDamageString45(self):
        self.assertEqual(self.saxon.receiveDamage(
            45), 'A Saxon has received 45 points of damage')

    def testReceiveDamageString10(self):
        self.assertEqual(self.saxon.receiveDamage(
            10), 'A Saxon has received 10 points of damage')

    def testReceiveDamageStringDied(self):
        self.assertEqual(self.saxon.receiveDamage(self.health),
                         'A Saxon has died in combat')


if __name__ == '__main__':
    unittest.main()
