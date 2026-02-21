print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
start = input("Do you want to go left or right?")
if start == "left":
    print ("You have decided to go through the mystical forrest")
    Track_1 = input("Do you want to take the path less taken or through the path of warriors who died trying?")
    if Track_1 == "path less taken":
        print("Congratulations! You will survive this level")
        doors = input("There are three doors at the end of the forrest trail, only one of them holds the tressure you desire, pick red, blue or green")
        if doors == "red":
            print("You have chosen the door to hell, you have died")
        elif doors == "blue":
            print("You have chosen the door to the ice age, you have died")
        else:
            print("COngratulations! You have the right door, the tressure is yours.")
    else:
        print("You have died. Start Over")
else :
    print ("You have decided to go through the sea of monsters")
    dec_1 = input("Do you want to start swimming or wait for the pirate ship to give you a ride?")
    if dec_1 == "wait":
        print("The pirates rob you and turn you into mulch")
    else:
        print("Courage is always rewarded, you survive the journey!")
        doors = input(
            "There are three doors at the end of the forrest trail, only one of them holds the tressure you desire, pick red, blue or green")
        if doors == "red":
            print("You have chosen the door to hell, you have died")
        elif doors == "blue":
            print("You have chosen the door to the ice age, you have died")
        else:
            print("COngratulations! You have the right door, the tressure is yours.")

