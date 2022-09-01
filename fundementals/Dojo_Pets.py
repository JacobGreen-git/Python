class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self): 
        print(f"{self.first_name} walked their pet.")
        Fluffy.play()

    def feed(self):
        print(f"{self.first_name} fed their pet.")
        Fluffy.eat()

    def bathe(self):
        print(f"{self.first_name} is bathing their pet.")
        Fluffy.noise()



class Pet:
    def __init__(self, name, type, tricks, health, energy, sound):
        self.name = name
        self.type = type
        self. tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound
        
    def sleep(self):
        self.energy += 25
        print(f"{self.name} is feeling rested after a long sleep! \n {self.energy} Energy")

    def play(self):
        self.health += 10
        print(f"{self.name} is feeling healthy. \n {self.health}")

    def eat(self):
        self.health += 10
        self.energy += 5
        print(f"{self.name} is feeling healthy and energetic. \n {self.health} HP \n {self.energy} Energy")

    def noise(self):
        print(f"{self.name} let out a ferocious {self.sound}!!")


Joe = Ninja('Joe', 'Shmo', 'Fluffy', 'Bones', 'Kibble')
Fluffy = Pet('Fluffy', 'Dog', 'Backflip', 10, 9000, 'meow')


Joe.feed()
Joe.walk()
Joe.bathe()

Fluffy.sleep()