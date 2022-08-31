class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.range = 15
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        print(f"{self.name} attacked {pirate.name}.")
        print(f"{pirate.name} now has {pirate.health} HP.")
        return self

    def ninjaStar(self, pirate):
        pirate.health -= self.range
        print(f"{self.name} used a ninja star on {pirate.name}.")
        print(f"{pirate.name} now has {pirate.health} HP.")
        return self

    def meditate(self):
        self.health = self.health + 10
        print(self.name + " meditated.")
        print(f"{self.name} has {self.health} HP.")
        return self