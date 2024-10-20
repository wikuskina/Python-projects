alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
new_text_list = []

def encrypt(original_text,shift_amount):
    for letter in original_text:
        # finding location of letters in original text in the alphabet, e.g. their original spot e.g. A = 0
        letter_location = alphabet.index(letter)
        # moving location of letters by shift amount
        new_letter_location = letter_location + shift_amount
        if new_letter_location < 26:
            # getting the new letter
            temp_letter = alphabet[new_letter_location]
            # appending to new text list
            new_text_list.append(temp_letter)
        else:
            # preventing program from running into error if list index is out of range (e.g. z is shifted by 9)
            new_letter_location = new_letter_location - 26
            # getting the new letter
            temp_letter = alphabet[new_letter_location]
            # appending to new text list
            new_text_list.append(temp_letter)

# call function
encrypt(text,shift)

# convert to string
new_text_string = ""
for l in new_text_list:
    new_text_string += l

print(f"Here is the encoded result '{new_text_string}'.")

