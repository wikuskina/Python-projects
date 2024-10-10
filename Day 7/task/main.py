import random
word_list = ["aardvark", "baboon", "camel"]

# Picking a random word from the list
picked_word = random.choice(word_list)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

picked_word_hidden = ""
number_of_letters = len(picked_word) #length of the picked word
for letter in range(0,number_of_letters):
    picked_word_hidden += "_"

print(picked_word_hidden)

# Ask user to guess a letter in a word
guessed_letter = input("Guess a letter:\n").lower()
print(guessed_letter)


# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.


# Checking if guessed letter is in the picked word
for letter in picked_word:
    if letter == guessed_letter:
        print("Right!")
    else:
        print("Wrong!")