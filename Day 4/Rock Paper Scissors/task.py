
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

play_again = "Y"
while play_again == "Y":
    # putting all options into a list to choose from
    # 0 = Rock, 1 = Paper, 2 = Scissors. Indexes in the list
    list_of_options = [rock, paper, scissors]

    # # introducing game to the player and asking to make a choice
    print("Let's play Rock, Paper, Scissors. Which one do you choose?")
    print("Type 0 for Rock, 1 for Paper, 2 for Scissors.")
    user_choice = int(input())

    # computer making a choice from 0 to 2
    computer_choice = random.randint(0,2)

    # print visuals of the game
    print(f"User chose: {list_of_options[user_choice]}, Computer chose: {list_of_options[computer_choice]}")
    # calculating choices and determining a winner
    if user_choice == computer_choice:
        print("Nobody wins! You chose the same option. Try again.")
    # user Rock, Computer Paper
    elif user_choice == 0 and computer_choice == 1:
        print("Computer wins! Rock covers the paper.")
    # user Rock, Computer Scissors
    elif user_choice == 0 and computer_choice == 2:
        print("User wins! Rock smashes the scissors.")
    # user Paper, Computer Scissors
    elif user_choice == 1 and computer_choice == 2:
        print("Computer wins! Scissors cut the paper.")
    # user Paper, Computer Rock
    elif user_choice == 2 and computer_choice == 1:
        print("User wins! Paper covers the rock.")
    # user Scissors, Computer Paper
    elif user_choice == 2 and computer_choice == 1:
        print("User wins! Scissors cut the paper")
    # user Scissors, Computer Rock
    else:
        print("Computer wins. Rock crushes the scissors.")

    play_again = input("Want to play again? Type Y for yes, N for no.").upper()






