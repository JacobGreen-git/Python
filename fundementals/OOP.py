#OOP
#Objects - things, items, they can do things, they have properties / attributes that describe
#emphasizes grouping data and functionality together in entities known as objects

cat1 = {
    'name': 'scar',
    'color': 'brown',
    'age': 3, #   Each additional cat will require a manual entry
    'breed': 'lion'
}

cat1 = {
    'name': 'garfield',
    'color': 'orange',
    'age': 5,
    'breed': 'lasagna'
}


#With a class, you can create a blueprint
class Cat():
    all_cats = []
    def __init__(self, name, color, age, breed):   #This is a class definition  #self is like "this" in JS  #_init_ = initialization
        self.name = name
        self.color = color
        self.age = age
        self.breed = breed
        Cat.all_cats.append(self)

#instance methods
    def print_info(self):
        print(f"Name: {self.name} Color: {self.color}")
        return self #this returns "cat1" to the next function when chaining

    def meow(self):
        print(f"{self.name} let out a cry!")
        return self

#class methods
    @classmethod
    def all_cats(cls):
        for cat in cls.all_cats:
            # print(cat)
            cat.print_info

#static method - somehow does something related to your class
    @staticmethod
    def convert_to_cat_years(years):
        return years * 7

age = 20
cat_years = Cat.convert_to_cat_years(age)
print(cat_years)


Cat.print_all_cats()
#class method, takes in cls and not self, references 

#instances are the things we make with the class blueprint

cat1 = Cat("scar", "black", 3, "lion") #we made cat1 from the Cat() class inputting the values in parenthesis

print(cat1.color)

cat1.print_info()
cat1.meow()

# for one_cat 

#chaining, adding multiple functions on the same line #Need to add "return self" to the function so that 'cat1' is returned to the next function and not the results of the previous function
# cat1.print_info().meow().meow().meow()


#when you call a function its called an argument
#when you define a function its a parameter



#########################


class Toy():
    def __init__(self, type, color, action):
        self.type = type
        self.color = color
        self.action = action

ball = Toy('ball', 'red', "bounces on florr")

cat1.fav_toy = ball

print(cat1.fav_toy.type)