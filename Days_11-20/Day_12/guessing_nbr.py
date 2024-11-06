# Guessing number game
import random

# Declaring constants of 'easy' and 'hard' levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# function to check the user's guess against the actual number
def guess_number(user_guess, actual_number, turns):
    """Checks guess against answer, and returns the number of turns remaining."""
    if user_guess > actual_number:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_number}.")


# function to set difficulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    

# main function
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    
    turns = set_difficulty()
    guess = 0
    
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = guess_number(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
