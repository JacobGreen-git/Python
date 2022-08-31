from characters import Character

class mage(Character):
    def __init__(self, move):
        super().__init__() #using super to call parent's constructor
        self.move = move

    def level_up(self):
        self.level += 1
        self.strength += 1
        self.defense += 1 

    def print_info(self):
        super().print_info()
        print(self.move)

Veigar = mage('Fire Ball')
print(Veigar.health)

Veigar.print_info()
Veigar.level_up()
Veigar.print_info()