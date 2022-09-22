from replit import clear
from art import logo

print(logo)

bidding = True
bids = {}

def find_highest_bidder(bidding_record):
    winner = ""
    win_price = 0
    for bidder in bidding_record:
        if bidding_record[bidder] > win_price:
            winner = bidder
            win_price = bidding_record[bidder]
    print(f"{winner} wins with a bid of ${win_price}!")

while bidding:
    name = input("What is your name\n")
    price = int(input("What is your bid?\n$"))
    bids[name] = price
    
    another = input("Are there more bidders? Enter Yes or No.").lower()
    if another == "no":
        bidding = False
    clear()

find_highest_bidder(bids)
