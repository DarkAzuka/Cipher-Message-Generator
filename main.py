from ascii import ascii
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(ascii)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(p_text, a_shift):
  cipher_text = ""
  for letter in p_text:
    position = alphabet.index(letter)
    new_position = position + a_shift
    new_letter = alphabet[new_position] 
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

def decrypt(d_text, a_shift):
  decipher_text = ""
  for letter in d_text:
    position = alphabet.index(letter)
    new_position = position - a_shift
    new_letter = alphabet[new_position] 
    decipher_text += new_letter
  print(f"The decoded text is {decipher_text}")

if direction == "encode":
  encrypt(p_text=text, a_shift=shift)
elif direction == "decode":
  decrypt(d_text=text, a_shift=shift)
    