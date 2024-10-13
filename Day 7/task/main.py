import random
word_list = ["aardvark", "baboon", "camel"]

# Picking a random word from the list
picked_word = random.choice(word_list)
print(f"You picked: {picked_word}")

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

while not game_over:
    guessed_letter = input("Guess a letter:\n").lower()
    print(f"You guessed: {guessed_letter}")

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

    print(displayed_word)


    if "_" not in displayed_word:
        game_over = True
        print("You win.")
    else:
       game_over = False
       print("You didn't win.")
