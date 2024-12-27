# Encryption Program
import random
import string

# Create a character set and a shuffled key
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# print(f"chars: {chars}")
# print(f"keys: {key}")

# ENCRYPTION
plain_text = input("ENTER A MESSAGE TO ENCRYPT: ")
cipher_text = ""

for letter in plain_text:
    if letter in chars:
        index = chars.index(letter)
        cipher_text += key[index]
    else:
        cipher_text += letter  # Handle characters not in `chars`

print(f"Cipher Text: {cipher_text}")

# DECRYPTION
cipher_text = input("ENTER A MESSAGE TO DECRYPT: ")
plain_text = ""

for letter in cipher_text:
    if letter in key:
        index = key.index(letter)
        plain_text += chars[index]
    else:
        plain_text += letter  # Handle characters not in `key`

print(f"Plain Text: {plain_text}")
