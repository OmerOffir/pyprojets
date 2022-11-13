
'''
This script create encryption with shifting 
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(message, shift):
    Enc_word = list()
    for letter in message:
        x = alphabet.index(letter)
        x = x + shift
        new_letter = alphabet[x]
        Enc_word.append(new_letter)
    Enc_word = ''.join(Enc_word)
    return Enc_word
        
    
def decode(message, shift):
    dec_word = list()
    for letter in message:
        x = alphabet.index(letter)
        x = x - shift
        new_letter = alphabet[x]
        dec_word.append(new_letter)
    dec_word = ''.join(dec_word)
    return dec_word
        

if __name__ == "__main__":

    while True:
        direction = input ("Type 'e' to encrtpt, type 'd' to decrypt  ")
        text = input ("type your message ").lower()
        shift = int(input("Type the shift numberr "))

        if direction == 'e':
            new_word = encrypt(text, shift)
            print(f"The encyption word is: {new_word}")
        if direction == 'd':
            new_word = decode(text, shift)
            print(f"The word is: {new_word}")







