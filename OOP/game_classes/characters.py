class Character:
    def __init__(self): #constructor
        self.health = 100
        self.level = 1
        self.mana = 100
        self.strength = 10
        self.defense = 5

#attack method
    def attack(self, target):
        print("Attacking" + target)
        target.defend(self.strength)
        return self

#defend method
    def defend(self, damage):
        print("Defending")
        actual_damage = damage - self.defense
        self.health -= actual_damage

def print_info(self):
    print(f'health {self.health} strength {self.strength}')