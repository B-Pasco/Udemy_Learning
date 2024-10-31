import random


def deal_card():
    """
    Returns a random card from the deck.
    The deck includes numbers 2-10 and four 10s for the face cards, with an 11 for Ace.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 11 represents an Ace.
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    Take a list of cards and return the score calculated from the cards.
    A score of 0 represents Blackjack (an Ace and a 10-card).
    If there’s an Ace (11) and the score goes over 21, it counts as 1 instead.
    """
    # Check for a blackjack (a hand with only two cards: an Ace and a 10-value card)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 is used as a marker for Blackjack.

    # Adjust for Ace if the score is over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # Change Ace from 11 to 1.

    return sum(cards)

def compare(u_score, c_score):
    """
    Compare the final scores of the user and the computer to determine the result.
    Returns a string indicating the outcome.
    """
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Lose, opponent has Blackjack!"
    elif u_score == 0:
        return "Win with a Blackjack!"
    elif u_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
        return "Opponent went over. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """
    Main function to control the flow of the game.
    Initializes hands, checks for Blackjack, and allows the user to draw more cards.
    """

    # 
    print("""
================================================================
        WELCOME TO BLACKJACK GAME!!!...LET'S PLAY!!!
================================================================
    """)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Each player draws two cards to start
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Continue game until the user decides to stop or goes over 21
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Displaying the given card for both players.
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for Blackjack or if user goes over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn: draw cards until score is at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final results as we conclude whose the winner of the game.
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Run the game repeatedly by asking user if want to play
while input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    # print("\n" * 2)
    play_game()

"""===========================THE END OF THE GAME CODE!!!.=================================="""
