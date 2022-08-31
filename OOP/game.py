from game_classes.characters import Character
from game_classes.mage import mage

bob = Character()
Veigar = mage.mage('Fire Ball')

while(bob.health > 0 and Veigar > 0):
    response = input("You're Bob, will you attack or defend? \n 1) Attack \n 2) Defend)")
    if response == '1':
        bob.attack(Veigar)
    elif response == '2':
        bob.defend()
    else:
        print("Please pick a valid option")