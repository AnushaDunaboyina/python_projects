alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = input("Type the shift number: \n")


def encrypt(text, shift):
    encrypt_text = ""
    
    for letter in text:
        if letter in alphabet:
            new_index = (int(alphabet.index(letter)) + int(shift)) % 26
            encrypt_text += alphabet[new_index]
        else:
            encrypt_text += letter          # spaces or symbols

    print(f"Encrypted text = {encrypt_text}")       

encrypt(text, shift)

