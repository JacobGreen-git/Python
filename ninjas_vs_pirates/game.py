from classes.ninja import Ninja
from classes.pirate import Pirate
import random


ninjas = {
    "1" : Ninja("Michelanglo"),
    "2" : Ninja("Naruto"),
    "3" : Ninja("Jacob"),
    "4" : Ninja('Shay'),
    "5" : Ninja("Kevin"),
    "6" : Ninja('Taylor')
}

pirates = {
    "1" : Pirate("Jack Sparrow"),
    "2" : Pirate("Maverick"),
    "3" : Pirate("Reece"),
    "4" : Pirate("Kyva"),
    "5" : Pirate("Leo"),
    "6" : Pirate("Koda"),
}



roll = ""
ninjaName = ""
pirateName = ""
response = ""


while(response != "Q"):
    response = input ("Select your character: \n 1) Michelanglo \n 2) Naruto \n 3) Jacob \n 4) Shay \n 5) Kevin \n 6) Taylor \n Q) Quit \n")
    if response in ninjas:
        ninjaName = ninjas[response]
    else:
        while(response != 'Q'):
                    print("Please pick a valid option")
                    response = input("Select your character: \n 1) Michelanglo \n 2) Naruto \n 3) Jacob \n 4) Shay \n 5) Kevin \n 6) Taylor \n Q) Quit \n")

    while(response != "Q"):
        response = input ("Select your enemy: \n 1) Jack Sparrow \n 2) Maverick \n 3) Reece \n 4) Kyva \n 5) Leo \n 6) Koda \n Q) Quit \n")
        if response in pirates:
            pirateName = pirates[response]       
        else:
            while(response != 'Q'):
                        print("Please pick a valid option")
                        response = input("Select your enemy: \n 1) Michelanglo \n 2) Naruto \n 3) Reece \n 4) Kyva \n 5) Leo \n 6) Koda \n Q) Quit \n")

        while(ninjaName.health > 0 and pirateName.health > 0):
            response = input(f"You're {ninjaName.name}, will you attack or meditate? \n 1) attack \n 2) Meditate \n 3) Range Attack \n 4) Show Stats \n")
            if response == '1':
                ninjaName.attack(pirateName)
            elif response == '2':
                ninjaName.meditate()
            elif response == '3':
                ninjaName.ninjaStar(pirateName)
            elif response == '4':
                ninjaName.show_stats()
            else:
                while(response != '1' and response != '2' and response != '3'and response != '4'):
                    print("Please pick a valid option")
                    response = input(f"You're {ninjaName.name}, will you attack or meditate? \n 1) attack \n 2) Meditate \n 3) Range Attack \n 4) Show Stats \n")
            
            roll = random.randint(1,3)
            if roll == 1:
                pirateName.attack(ninjaName)
            elif roll == 2:
                pirateName.eatOrange()
            elif roll == 3:
                pirateName.cannonBall(ninjaName)

        if ninjaName.health <= 0:
            print("You are dead.")
