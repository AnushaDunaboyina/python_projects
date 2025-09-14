alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def caesor(original_text, shift_amount, encode_or_decode):
    result_text = ""

    for letter in original_text:

        if encode_or_decode == "encode":
            if letter in alphabet:
                new_index = (int(alphabet.index(letter)) + int(shift_amount)) % len(alphabet)
                result_text += alphabet[new_index]
            else:
                result_text += letter
        
        else:
            if letter in alphabet:
                new_index = int((alphabet.index(letter)) - int(shift_amount)) % len(alphabet)
                result_text += alphabet[new_index]
            else:
                result_text += letter        

    print(f"Result text = {result_text}")

    
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = input("Type the shift number: \n")

    caesor(text, shift, direction)

    go_again = input("Type 'yes' if you want to go again. Otherwise, type 'no': ")
    if go_again != "yes":
        break







