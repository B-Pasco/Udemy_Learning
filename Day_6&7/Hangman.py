# we are writing code for game called Hangman.

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

lives = 6
game_over = False
correct_letter = []

while not game_over:
    Guess = input("Guess a letter: ").lower()
    print(Guess)


    display = ""

    for letter in chosen_word:
        if letter == Guess:
            display += letter
            correct_letter.append(Guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)


    if Guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose!...")


    if "_" not in display:
        game_over = True
        print("You win!...")
