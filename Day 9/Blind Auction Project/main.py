# "Secret" auction: asks user for Name and Bid amount,
# compares bid amounts and chooses the highest amount -- > winner

import art # where the logo is
print(art.logo)
print("WELCOME to the secret auction. Let's find the highest bidder!")

data = {} # where data will be stored

bidders = "YES" # if there are any more bidders, program keeps asking for user input
while bidders == "YES":
    username = input("Please enter your name: ")
    bid = input("Please enter your bid price: ")
    bid_int = int(bid)

    def add_data (username, bid_int):
        data[username]=bid_int
        #print(data)

    bidders = input("Are there more bidders? Say Yes or No: ").upper()
    # continue asking for more names and bids if yes
    print("\n" * 100) # to clear the screen

    add_data(username, bid_int) # run function

# print(f"All bids: {data}")
# find the highest bidder out of all participants

highest_bid = max(data, key=data.get) # display key (name) with maximum bid
print(f"Winner is: {highest_bid}! Congratulations. ")





