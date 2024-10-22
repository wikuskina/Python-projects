# caesar cipher to encode and decode messages
# plain text is moved bt a SHIFT amount

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# created a caesar function that combined two previous functions:
# one to decode and another to encode the messages 
# direction variable determines which one is used
def caesar(original_text,shift_amount):
    if direction == "encode":
        encrypted_text = []
        for letter in original_text:
            # finding location of letters in original text in the alphabet, e.g. their original spot e.g. A = 0
            letter_location = alphabet.index(letter)
            # moving location of letters by shift amount
            new_letter_location = letter_location + shift_amount
            # using modulo to prevent number of new letter location going beyond list length
            new_letter_location = new_letter_location % len(alphabet)
            # getting the new letter
            temp_letter = alphabet[new_letter_location]
            # appending to new text list
            encrypted_text.append(temp_letter)
        # convert to string
        encrypted_string = ""
        for l in encrypted_text:
            encrypted_string += l
        print(f"Here is the encoded result '{encrypted_string}'.")

    else:
        decrypted_text = []
        for letter in original_text:
            letter_location = alphabet.index(letter)
            new_letter_location = letter_location - shift_amount
            new_letter_location = new_letter_location % len(alphabet)
            # print(new_letter_location)
            temp_letter = alphabet[new_letter_location]
            decrypted_text.append(temp_letter)
        # convert to string
        decrypted_string = ""
        for l in decrypted_text:
            decrypted_string += l
        print(f"Here is the decoded result '{decrypted_string}'.")



# call function
caesar(text, shift)
