#python is an oop language
#classes are blueprints for creating objects
#good practice to have class name singular and capitalized
from email.message import Message


class Animal:
    #constructor are the properties of the class
    def __init__(self, name, species, region="EARTH"):
        self.name = name
        self.species = species
        self.region = region
    
    def message(self):
        print("This one goes out to my homie Sean!")
        return self

    def add(self, num1, num2):
        print(f"{self.name} is doing arithmetic! {num1} + {num2} = {num1+num2}")
        return self


#here we are creating an object of the class Animal
lion = Animal("Lion","Cat", "Africa")
penguin = Animal("Penguin","Bird/Mammal?", "Antartica")

print(lion.region)

# penguin.message().add(7,3)

# lion.region = "Africa/America"

# print(lion.region)