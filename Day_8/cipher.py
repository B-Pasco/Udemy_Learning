# Ceaser cipher message
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

# Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabets by the shift amount and print the encrypted text.
def encrypt(original_text, shift_amount):

    cipher_text = ""

    for letter in original_text:
        shift_position = alphabet.index(letter) + shift_amount
        # What happens if you try to shift z forwards by 9? can you fix the code?
        shift_position %= len(alphabet) # to make sure it is in range.
        cipher_text += alphabet[shift_position]
    print(f"Here is the encoded result: {cipher_text.capitalize()}")

def decrypt(original_text, shift_amount):

    output = ""

    for letter in original_text:
        shift_position = alphabet.index(letter) - shift_amount
        # What happens if you try to shift z forwards by 9? can you fix the code?
        shift_position %= len(alphabet) # to make sure it is in range.
        output += alphabet[shift_position]
    print(f"Here is the output for cipher: {output.capitalize()}")


# Call the 'encrypt()' function and pass in the user inputs. you should be able to test the code and encrypt a message.
decrypt(original_text = text, shift_amount = shift)
