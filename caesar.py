alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alpha_key = 38
digit_key = 39
plaintext = "thereareEXACTLY400treesOverThere"
ciphertext = ""
for letter in plaintext:
    index = (alphabet.index(letter) + alpha_key) if letter.isalpha() else (alphabet.index(letter) + digit_key)
    ciphertext += alphabet[index % len(alphabet)]

print(ciphertext)