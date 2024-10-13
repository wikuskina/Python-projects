import random
import hangman_words
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Picking a random word from the list of words
# list is stored in another module called hangman.words
picked_word = random.choice(hangman_words.word_list)
# print(f"You picked: {picked_word}")

picked_word_hidden = ""
number_of_letters = len(picked_word) #length of the picked word
for letter in range(0,number_of_letters):
    picked_word_hidden += "_"

print(picked_word_hidden)

# Ask user to guess a letter in a word
# Add while loop for user to guess again

# setting a game_over variable that at some point will end the game + end the loop
game_over = False

# creating a list of letters where each correctly guessed letter will be added
# FOR loop will be used to loop through this list and a letter that user is guessing at the time
correct_letters = []

# setting variable called lives to track lives (6) left
lives = 6

while not game_over:
    guessed_letter = input("Guess a letter:\n").lower()
    print(f"You guessed: {guessed_letter}")

    # remove a life if guess is incorrect
    if guessed_letter in picked_word:
        print(f"Correct guess! LIVES LEFT: {lives}")
    else:
        lives = lives - 1
        print(f"Wrong guess. LIVES LEFT: {lives}")

# a list of word displayed to user
    displayed_word = ""
    for letter in picked_word:
        if  letter == guessed_letter:
            # letter that is being looped through added to the list + display if matches the letters in the chosen word
            displayed_word += letter
            correct_letters.append(guessed_letter)
        # if the letter was previously added into correct letters list, this letter will be looped though along with user's guess and added to the display
        # so essentially it will be looping through several letters at a time and adding them all
        elif letter in correct_letters:
            displayed_word += letter
        else:
            displayed_word += "_"

    print(f"The letters you have guessed so far: {displayed_word}")
    # to check how many lives left and print corresponding image
    if lives == 5:
        print(stages[5])
    elif lives == 4:
        print(stages[4])
    elif lives == 3:
        print(stages[3])
    elif lives == 2:
        print(stages[2])
    elif lives == 1:
        print(stages[1])
    elif lives == 0:
        print(stages[0])
    print("--------------------------------------------------------")


    if "_" not in displayed_word:
        game_over = True
        print("You win!")
    elif lives == 0:
        gave_over = False
        print("You lost all your lives. Game over.")
    else:
       game_over = False

