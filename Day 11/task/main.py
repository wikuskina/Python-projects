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
game_over = False

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

def another_card():
    chosen_card3 = random.choice(cards)
    #print(f"chosen card 3 {chosen_card3}")
    return chosen_card3

start = input(want_play).lower()
if start == "y":
    while continue_playing == "y":
        player_cards = deal_player()
        player_sum_cards = player_cards[0]+ player_cards[1]
        print(f"Your cards: {player_cards}. Current score: {player_sum_cards}")
        computer_cards = deal_computer()
        computer_sum_cards = computer_cards[0] + computer_cards[1]
        print(f"Computer's first card: {computer_cards[0]}.")
        print("-----------------------------------")
        if player_sum_cards == 21 and computer_sum_cards == 21:
            print("Push! You got equal score of 21 so nobody wins")
            game_over = True
            break
        elif player_sum_cards == 21 and computer_sum_cards != 21:
            print(f"You won! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
            game_over = True
            break
        elif computer_sum_cards == 21 and player_sum_cards !=21 :
            print(f"You lost! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
            game_over = True
            break
        elif player_sum_cards < 21 and computer_sum_cards > 21:
            print(f"You won! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
            game_over = True
            break
        elif computer_sum_cards < 21 and player_sum_cards > 21:
            print(f"You lost! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
            game_over = True
            break
        else:
            # further play or pass?
            more_card = input(play_or_pass).lower()
            if more_card == 'y' and game_over == False:
                player_one_more_card = another_card()
                player_cards.append(player_one_more_card)
                player_sum_cards = player_sum_cards + player_one_more_card
                print(f"Your cards: {player_cards}, current score: {player_sum_cards}")
                computer_one_more_card = another_card()
                computer_cards.append(computer_one_more_card)
                computer_sum_cards = computer_sum_cards + computer_one_more_card
                print(f"Computer's first card: {player_cards[0]}")
                #print(f"All computer cards: {computer_cards} and their sum {computer_sum_cards}")
                if player_sum_cards == 21 and computer_sum_cards == 21:
                    print("Push! You got equal score of 21 so nobody wins")
                    game_over = True
                elif player_sum_cards == 21 and computer_sum_cards != 21:
                    print(f"You won! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
                    game_over = True
                elif computer_sum_cards == 21 and player_sum_cards != 21:
                    print(f"You lost! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
                    game_over = True
                elif player_sum_cards < 21 and computer_sum_cards > 21:
                    print(f"You won! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
                    game_over = True
                elif computer_sum_cards < 21 and player_sum_cards > 21:
                    print(f"You lost! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
                    game_over = True
            else:
                game_over = True
                break



else:
    exit()


