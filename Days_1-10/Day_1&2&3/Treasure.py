# Treasure hunting game as the learning out come (Day_3).

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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')

# Let's begin to built the game.
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure on this Island.")

choice_1 = input('You are at crossroad, Where do you want to go?, Type "Left" or "Right" ').lower()

# condition statement to be met.
if choice_1 == 'left':
    choice_2 = input('You\'ve to the lake. '
                     'There is an island in the milddle of the lake. '
                      ' Type "wait" to wait for a boat, or Type "swim" to swim across the lake.\n').lower()
    if choice_2 == 'wait':
        choice_3 = input('You arrived at the island unharmed, '
                         'There is 3 doors; one is Red '
                         'one yellow and one blue '
                         'Which one do you choose? \n').lower()
        if choice_3 == 'yellow':
            print("You found treasure and you won!!!.")
        elif choice_3 == 'red':
            print("You enter a room of fire. Game over")
        elif choice_3 == 'blue':
            print("You enter a room full of beasts. Game over!")
        else:
            print("You chose the door doesn't exist. Game Over!")
    else:
        print("You have attacked by angry sharks. Game Over!") 
else:
    print("You fell into the hole. Game Over")


# The End of the Game.

