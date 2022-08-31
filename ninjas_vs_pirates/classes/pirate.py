class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.range = 15

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print(self.name + " attacked " + ninja.name + ".")
        print(f"{ninja.name} now has {ninja.health} HP.")
        return self

#Add an ammunition?
    def cannonBall(self, ninja):
        ninja.health -= self.range
        print(self.name + " used a cannon on " + ninja.name + ".")
        print(f"{ninja.name} now has {ninja.health} HP.")
        return self

    def eatOrange(self):
        self.health = self.health + 10
        print(self.name + " ate an orange.")
        print(f"{self.name} has {self.health} HP.")
        return self