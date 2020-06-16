# Reverse Cipher


# You insert the message, either encrypted or decrypted, here
# For most other ciphers, we would encrypt it or decrypt it. However
# due to the nature of this cipher, encrypting and decrypting our 
# message will be the same.
message = 'Welcome to Python!'

# This is the translated message that we will print. This should always 
# be blank
translated = ''

# We use a while-loop to iterate through the message backwards, copying each letter
# to our translated string. We print it when we are done.
i = len(message)-1
while i >= 0:
    translated = translated + message[i]
    i = i - 1
print(translated)
