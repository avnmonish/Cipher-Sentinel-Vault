
# ADFGVX Cipher implementation :

# Function to generate the ADFGVX grid based on a given keyword.
def generate_grid(keyword):
   
    keyword = keyword.upper()
    
    # The alphabet and digits used in the grid.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
   
    # Combining the keyword and alphabet, removing duplicates, and maintaining the original order.
    key = keyword + alphabet
    key = ''.join(sorted(set(key), key=key.index))
   
    
    # Creating a 6x6 grid.
    grid = [list(key[i:i+6]) for i in range(0, len(key), 6)]
    
    return grid

# Function to encrypt a plaintext using the ADFGVX cipher.
def encrypt(plaintext, keyword) :
   
    keyword = keyword.upper()
   
    # Generating the ADFGVX grid.
    grid = generate_grid(keyword)
   
    # The ADFGVX characters.
    adfgvx = "ADFGVX"
   
    result = ""
   
    # Loop through each character in the plaintext.
    for char in plaintext:
        # Loop through the rows in the grid.
        for row in grid:
            # Check if the character is in the current row.
            if char.upper() in row:
                # Add the corresponding ADFGVX characters to the result.
                result += adfgvx[grid.index(row)]
                result += adfgvx[row.index(char.upper())]
   
    return result

# Function to decrypt a ciphertext using the ADFGVX cipher.
def decrypt(ciphertext, keyword) :
    
    keyword = keyword.upper()
   
    # Generating the ADFGVX grid.
    grid = generate_grid(keyword)
   
    # The ADFGVX characters.
    adfgvx = "ADFGVX"
   
    result = ""
    i = 0
   
    # Loop through the ciphertext.
    while i < len(ciphertext):
        # Get the first ADFGVX character.
        adfg = ciphertext[i].upper()
        i += 1
       
        # Get the second ADFGVX character.
        vx = ciphertext[i].upper()
        i += 1
       
        # Find the corresponding plaintext character from the grid and add it to the result.
        result += grid[adfgvx.index(adfg)][adfgvx.index(vx)]
   
    return result