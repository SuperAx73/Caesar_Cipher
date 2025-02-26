alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','_']

direction = input('type "encode" to encript and "decode" to decrypt:\n ')
text = input('type your message:\n ').lower()
shift = int(input('type the shift number:\n '))

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        shited_position = alphabet.index(letter) + shift
        shited_position %= len(alphabet)
        cipher_text += alphabet[shited_position]

    print(f'Here is the encoded result:\n{cipher_text}')

def decrypt(text, shift):
    output_text = ""
    for letter in text:
        shiftted_position = alphabet.index(letter) - shift
        shiftted_position %= len(alphabet)
        output_text += alphabet[shiftted_position]
    print(f'Here is the encoded result:\n{output_text}')

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print('Type "encode" to encrypt, "decode" to decrypt!')