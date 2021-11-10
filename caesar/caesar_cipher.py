import caesar_art


def caesar(plain_text, shift_amnt, chosen_direc):
    text_ind = 0
    for let in text:
        if let in alphabet:
            if chosen_direc.lower() == "encode":
                if alphabet.index(let) + shift > 25:
                    text_ind = (alphabet.index(let) + shift - 1) - 25
                else:
                    text_ind = alphabet.index(let) + shift
                cipher_text_list.append(alphabet[text_ind])
            elif chosen_direc.lower() == "decode":
                text_ind = (alphabet.index(let) - shift)
                cipher_text_list.append(alphabet[text_ind])
        else:
            cipher_text_list.append(let)
        # cipher_text_list.append(alphabet[text_ind])
    return (f"The encrypted text is: {input_text.join(cipher_text_list)}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(caesar_art.logo)

play = True

while play:
    text_list = []
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift_check = True
    shift = int(input("Type the shift number:\n"))
    while shift_check:
        if shift > 26:
            shift = int(input("shift number exceeded maximum. Please enter a new shift number: "))
        else:
            shift_check = False
    input_text = ""
    cipher_text_list = []

    # for t in text:
    #     for let in alphabet:
    #         if t == let:
    print(caesar(plain_text=text, shift_amnt=shift, chosen_direc=direction))
    play = False
    again = input("would you like to go again? (yes/no): ")
    if again.lower() == "y" or again.lower() == "yes":
        play = True
