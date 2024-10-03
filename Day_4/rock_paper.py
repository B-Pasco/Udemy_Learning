# this is rock, paper, and scissors game for practicing python programming.

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# putting the in the list
game_img = [rock, paper, scissors]

# taking user input
user_choice = int(input("What do you chose? Type 0 for rock, 1 for paper, and 2 for scissors \t"))
print(game_img[user_choice])

# Taking random nbr of computer
computer_choice = random.randint(0, 2)
print("Computer Choice: \n")
print(game_img[computer_choice])


# Checking condition of the game to win or lose.
if user_choice >= 3 or user_choice < 0:
    print("You typed Invalid choice. You lose..")
elif user_choice == 0 and computer_choice == 2:
    print('You win!!!...')
elif computer_choice == 0 and user_choice == 2:
    print('You lose!!!...')
elif computer_choice > user_choice:
    print("You lose!...")
elif computer_choice < user_choice:
    print("You win!!!...")
