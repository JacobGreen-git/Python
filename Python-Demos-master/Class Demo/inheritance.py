class Animal:
    def __init__(self, name, species, region, is_extinct=False):
        self.name = name
        self.species = species
        self.region = region
        self.is_extinct = is_extinct
    
    def eat(self):
        print("The animall is eating!")
    
    def sleep(self):
        print("The animall is sleeping!")
    
    def mating(self):
        print("The animall is mating!")

class Lion(Animal):
    def __init__(self, name, species, region, is_extinct=False):
        super().__init__(name, species, region, is_extinct)
        self.name = name
        self.species = species
        self.region = region
        self.is_extinct = is_extinct

    def noise(self):
        print("rawr".upper())

class Rabbit(Animal):
    def __init__(self, name, species, region, is_extinct=False):
        super().__init__(name, species, region, is_extinct)
        self.name = name
        self.sleep = species
        self.region = region
        self.is_extinct = is_extinct

    def eat(self):
        print("The rabbit is eating a carrot...")

class Dinosaur(Animal):
    def __init__(self, name, species, region, is_extinct=False):
        super().__init__(name, species, region, is_extinct)
        self.name = name
        self.sleep = species
        self.region = region
        self.is_extinct = is_extinct
        self.legs = 4



simba = Lion("Simba", "Cat", "Africa")
mufasa = Lion("Mufasa", "Cat", "Africa")
bugs_bunny = Rabbit("Bugs Bunny", "Rabbit", "America")
little_foot = Dinosaur("Little Foot", "Dinosaur", "North America")

little_foot.is_extinct = True
print(little_foot.is_extinct)

print(simba.name, mufasa.name)

print(little_foot.legs)