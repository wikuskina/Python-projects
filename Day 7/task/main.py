import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# Picking a random word from the list
picked_word = random.choice(word_list)
print(picked_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# Ask user to guess a letter in a word
guessed_letter = input("Guess a letter:\n").lower()
print(guessed_letter)

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

# Checking if guessed letter is in the picked word
for letter in picked_word:
    if letter == guessed_letter:
        print("Right!")
    else:
        print("Wrong!")