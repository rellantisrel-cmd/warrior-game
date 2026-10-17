import random


class Warrior:
    def attack(self, enemy):
        enemy.health -= 20
        print(f"{self.name} attack {enemy.name}. "
              f"У {enemy.name} have health: {enemy.health}")
unit1 = Warrior()
unit1.name = 'warrior1'
unit1.health = 100
unit2 = Warrior()
unit2.name = 'warrior2'
unit2.health = 100

while unit1.health > 0 and unit2.health > 0:
    attacker, defender = random.choice([(unit1, unit2), (unit2, unit1)])
    attacker.attack(defender)
if unit1.health > 0:
    print(f"{unit1.name} winner!")
else:
    print(f"{unit2.name} winner!")
