# Bid Auction project

# TODOs:
# Asking the user the name

# Saving the name into the dictionary {name:value}
# checking for the highest bid
def find_highest_bid(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"\n\nThe winner is {winner} with the bid of a ${bid_amount}\n\n")

# Check whether the new bid is needed to be added
bids = {} # initiating the bid dictionary

continue_bidding = True

while continue_bidding:
    name = input("\nWhat is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any bidders?, Type 'yes' or 'no'\n")
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bid(bids)
    elif should_continue == 'yes':
        print("\n" * 10)


