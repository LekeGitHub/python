# A - Z 65 - 90
# a - z 97 - 122
# ord(your_letters)
# chr(your_code)

# Hints
# Use is upper() to decide which unicodes to work with
# Add the key (number of characters to shift) and if the key is bigger
# if smaller, then the unicode for A, Z, a, z increase or decrease by 26

# Receive the message to encrypt and the number of characters to shift

message = input("Enter message to be encrypted : ")
shift_key = int(input("How many characters shift(1 - 26) : "))

# Prepare the secret_message
secret_message = ""

# Cycle through each char in message
for word in message:
    # if it isn't a letter then keep it as it is
    if word.isalpha():
        char_code = ord(word)
        char_code += shift_key

        # If uppercase then compare to uppercase unicodes
        if word.isupper():
            # If bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
            # If Smaller than A subtract 26
            if char_code < ord('A'):
                char_code += 26

        # If lowercase then compare to lowercase unicodes
        else:
            # If bigger than z subtract 26
            if char_code > ord('z'):
                char_code -= 26
            # If Smaller than a subtract 26
            if char_code < ord('a'):
                char_code += 26
        # Convert from code to letter and add to message
        secret_message += chr(char_code)

    else:
        secret_message += word
print("Encrypted : ", secret_message)

# Decryption

shift_key = - shift_key
message = ""
for word in secret_message:
    # if it isn't a letter then keep it as it is
    if word.isalpha():
        char_code = ord(word)
        char_code += shift_key

        # If uppercase then compare to uppercase unicodes
        if word.isupper():
            # If bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
            # If Smaller than A subtract 26
            if char_code < ord('A'):
                char_code += 26

        # If lowercase then compare to lowercase unicodes
        else:
            # If bigger than z subtract 26
            if char_code > ord('z'):
                char_code -= 26
            # If Smaller than a subtract 26
            if char_code < ord('a'):
                char_code += 26
        # Convert from code to letter and add to message
        message += chr(char_code)

    else:
        message += word
print("Decrypted : ", message)
