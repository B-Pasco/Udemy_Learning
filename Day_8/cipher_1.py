#  for make this cipher more simple and few code from cipher.py

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(original_text, shift_amount, encode_or_decode):

    output = ""

    if encode_or_decode == "decode":
                shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output += letter
        else:
            shift_position = alphabet.index(letter) + shift_amount
            # What happens if you try to shift z forwards by 9? can you fix the code?
            shift_position %= len(alphabet)
            output += alphabet[shift_position]

    print(f"Here is the {encode_or_decode}d result: {output.capitalize()}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar_cipher(original_text = text, shift_amount = shift, encode_or_decode = direction)

    restart = input("\nType 'Yes' if you want to go again. Otherwise 'No'\n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye!")
