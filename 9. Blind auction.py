# Blind auction project

bids = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))

    bids[name] = bid
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n" * 20)

    if other_bidder != "yes":
        break

print(f"Bid auctions list: \n{bids}")

highest_bid = 0
winner = ""

for person in bids:
    if bids[person] > highest_bid:
        highest_bid = bids[person]
        winner = person

print(f"The winner is {winner} with a bid of ${highest_bid}")
    
