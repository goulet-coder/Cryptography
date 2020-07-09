# The following code is from: 
# https://stackoverflow.com/questions/36188226/substitution-cipher-python
import random

#Normal Alphabet list to compare to.
alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '

#Substitution values
key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'

# The message we want to encrypt or decrypt
plaintext = "Hey, this is really fun!"

def encrypt(plaintext, key, alphabet):
    # Makes a dictionary (data structure) that matches a key
    # to a value. For example, a matches to n.
    keyMap = dict(zip(alphabet, key))
    
    # Uses the dictionary to convert each character from 
    # the alphabet to the substitution key.
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

def decrypt(cipher, key, alphabet):
    # Same idea as the encrypt function, except we do it in 
    # reverse.
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)

cipher = encrypt(plaintext, key, alphabet)

print(plaintext)
print(cipher)
print(decrypt(cipher, key, alphabet))
