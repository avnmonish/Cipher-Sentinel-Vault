

# Random password generator Implementation :


import random
import string

# Function to generate a random password of given length.
def password(length):
    
    # String of all(lowercase, uppercase, digits, special characters) characters.
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Returning a random password of given length
    return ''.join(random.choice(characters) for _ in range(length))


'''
random_length = random.randint(8, 15)
random_string = generate_random_string(random_length)
'''
