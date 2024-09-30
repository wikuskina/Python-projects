import random

# Password generator from letters, numbers, and symbols
# Lists of available items to choose password from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Asking user for a number of each (letter, symbol, number) in their password
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Setting a variable for a final password (list)
final_password = []

# Selecting letters, numbers, symbols as per users request from the original lists
chosen_letters = random.choices(letters, k=nr_letters)
print(f"These are chosen letters: {chosen_letters}")
chosen_symbols = random.choices(symbols, k=nr_symbols)
print(f"These are chosen symbols: {chosen_symbols}")
chosen_numbers = random.choices(numbers, k=nr_numbers)
print(f"These are chosen numbers: {chosen_numbers}")

# Iterating over newly created 3 lists of chosen symbols, numbers, and letters and adding all to one final "password list"
for letter in chosen_letters:
    final_password.append(letter)
for symbol in chosen_symbols:
    final_password.append(symbol)
for number in chosen_numbers:
    final_password.append(number)

# Converting final list into a string (ready to use password)
final_final_password = ""
for i in final_password:
    final_final_password = i + final_final_password

print(f"This is your new super secure password: {final_final_password}")

# to make the password even more secure, items in the password can be made random
# using random shuffle () function. It accepts a list and returns sequence (not a list). Can be looped through and made into a string
random.shuffle(final_password)
password2= ""
for char in final_password:
    password2 += char

print(f"This is your new EVEN MORE secure password: {password2}")
