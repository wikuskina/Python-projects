# Importing the welcome picture for the game
import art
print(art.logo)
import random

# Deck is unlimited (items in the list have equal chance of being drawn), no jokers
# Jack / queen / king count as 10
# Ace count as 11 or 1
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]
want_play = "Do you want to play a game of Blackjack? Type 'y' or 'n'."
play_or_pass = "Type 'y' to get another card, or type 'n' to pass"
continue_playing = "y"

# Functions to deal cards
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
    # Print(f"chosen card 3 {chosen_card3}")
    return chosen_card3

# Program starts
# Continue_playing allows continuos run of the program
while continue_playing == "y":
    print("-----------------------------------")
    start = input(want_play).lower()
    # Program will be tested against this condition and won't continue if game_over is True
    game_over = False
    # If start is chosen as "n" - the program will exit
    
    if start == "y":
        print("LET'S PLAY!")
        print("-----------------------------------")
        # Cards are given to the player and computer. Computer has only his first card displayed
        player_cards = deal_player()
        player_sum_cards = player_cards[0]+ player_cards[1]
        print(f"Your cards: {player_cards}. Current score: {player_sum_cards}")
        computer_cards = deal_computer()
        computer_sum_cards = computer_cards[0] + computer_cards[1]
        print(f"Computer's first card: {computer_cards[0]}.")
        # Checking if computer or player have won or lost immediately (e.g. 21 drawn)
        
        if player_sum_cards == 21 and computer_sum_cards == 21:
            print("Push! You got equal score of 21 so nobody wins")
            game_over = True
            break
            
        elif player_sum_cards == 21 and computer_sum_cards != 21:
            print(f"You won! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
            print(f"Computer's cards were: {computer_cards}")
            game_over = True
            break
            
        elif computer_sum_cards == 21 and player_sum_cards !=21 :
            print(f"You lost! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
            print(f"Computer's cards were: {computer_cards}")
            game_over = True
            break
            
        elif player_sum_cards < 21 and computer_sum_cards > 21:
            print(f"You won! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
            print(f"Computer's cards were: {computer_cards}")
            game_over = True
            break
            
        elif player_sum_cards > 21 and computer_sum_cards > 21:
            print(f"You both lost. Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
            print(f"Computer's cards were: {computer_cards}")
            game_over = True
            break
            
        elif player_sum_cards > 21 and computer_sum_cards < 21 :
            print(f"You lost! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
            print(f"Computer's cards were: {computer_cards}")
            game_over = True
            break
            
        else:
            # Asking if player wants to get more cards, or pass choosing another card?
            # If they select to choose another card - another card will be drawn and added to the sum (same for computer)
            # If they select to NOT choose another card - else statement will be executed where current sums of cards will be compared
            # And winner chosen
            
            print("-----------------------------------")
            # Player will be continuously asked to draw more cards until they or computer will reach 21
            # Or they chose to not draw more cards
            while game_over == False:
                more_card = input(play_or_pass).lower()
                
                if more_card == 'y' and game_over == False:
                    player_one_more_card = another_card()
                    player_cards.append(player_one_more_card)
                    player_sum_cards = player_sum_cards + player_one_more_card
                    print(f"Your cards: {player_cards}, current score: {player_sum_cards}")
                    computer_one_more_card = another_card()
                    computer_cards.append(computer_one_more_card)
                    computer_sum_cards = computer_sum_cards + computer_one_more_card
                    print(f"Computer's first card: {computer_cards[0]}")
                    
                    # Checking if computer or player won already
                    if player_sum_cards == 21 and computer_sum_cards == 21:
                        print("Push! You got equal score of 21 so nobody wins")
                        game_over = True
                    elif player_sum_cards == 21 and computer_sum_cards != 21:
                        print(f"You won! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
                        print(f"Computer's cards were: {computer_cards}")
                        game_over = True
                    elif player_sum_cards < 21 and computer_sum_cards > 21:
                        print(f"You won! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
                        print(f"Computer's cards were: {computer_cards}")
                        game_over = True
                    elif player_sum_cards > 21 and computer_sum_cards > 21:
                        print(f"You both lost. Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
                        print(f"Computer's cards were: {computer_cards}")
                        game_over = True
                    elif player_sum_cards > 21 and computer_sum_cards < 21:
                        print(f"You lost! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
                        print(f"Computer's cards were: {computer_cards}")
                        game_over = True


                else:
                    if computer_sum_cards > player_sum_cards:
                        print(f"You lost! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
                        print(f"Computer's cards were: {computer_cards}")
                        print(f"Your cards were: {player_cards}")
                        game_over = True
                        break
                    else:
                        print(f"You won! Your score is: {player_sum_cards}, computer score is {computer_sum_cards}")
                        print(f"Computer's cards were: {computer_cards}")
                        print(f"Your cards were: {player_cards}")
                        game_over = True
                        break

else:
    continue_playing = "n"
    exit()



