# importing the welcome picture for the game
import art
print(art.logo)
import random

# deck, unlimited, no jokers
# jack / queen / king count as 10
# ace count as 11 or 1
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
want_play = "Do you want to play a game of Blackjack? Type 'y' or 'n'."
play_or_pass = "Type 'y' to get another card, or type 'n' to pass"
continue_playing = "y"

# function to deal cards
def deal_player():
    chosen_card1 = random.choice(cards)
    chosen_card2 = random.choice(cards)
    chosen_cards = [chosen_card1,chosen_card2]
    return chosen_cards

def deal_computer():
    chosen_card1 = random.choice(cards)
    chosen_card2 = random.choice(cards)
    chosen_cards = [chosen_card1, chosen_card2]
    return chosen_cards

start = input(want_play).lower()
if start == "y":
    while continue_playing == "y":
        player_cards = deal_player()
        sum_cards = player_cards[0]+ player_cards[1]
        print(f"Your cards: {player_cards}. Current score: {sum_cards}")
        computer_cards = deal_computer()
        sum_cards = computer_cards[0] + computer_cards[1]
        print(f"Computer's first card: {computer_cards[0]}.")
        break
else:
    exit()


