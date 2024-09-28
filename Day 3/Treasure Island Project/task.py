print('''
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
start = "Y"
while start == "Y":
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    # Create different choices for the game player. Every choice determines whether he continues the game or loses.
    print("You are at the crossroad. Where do you want to go? Type 'left' or 'right'.")
    crossroad = input()
    # correct choice is left. Going right kills the player.
    if crossroad == "left":
        print("You have come to a lake. There is an island in the middle of the lake.")
        print("Type 'wait' to wait for the boat. Type 'swim' to swim acros.")
        lake = input()
        # waiting for the boat is correct choice. Swimming across kills the player.
        if lake == 'wait':
            print("You arrive to the island unharmed. There is a house with three doors. Red, yellow and blue.")
            print("Which colour do you choose?")
            door = input()
            # yellow is correct choice. Other doors lead the end of the game.
            if door == "yellow":
                print("You found the treasure! You WIN!")
            elif door == "red":
                print("It's a room full of fire. Game over.")
            elif door == "blue":
                print("You enter a room full of beasts. Game over.")
            else:
                pass
        else:
            print("You get attacked by an angry trout. Game over.")
    else:
        print("You fell into a hole. Game over.")


    print("Start over? Y / N")
    start = input()

