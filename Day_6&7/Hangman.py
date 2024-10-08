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

Guess = input("Guess a letter: ").lower()
print(Guess)


display = ""

for letter in chosen_word:
    if letter == Guess:
        display += letter
    else:
        display += "_"

print(display)
