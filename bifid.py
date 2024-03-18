

# Bifid Cipher implementation :

# Key Matrix.
key = [['P', 'H', 'Q', 'G', 'M', '4'],
       ['E', 'A', 'Y', 'L', 'N', '5'],
       ['O', 'F', 'D', 'X', 'K', '6'],
       ['R', 'C', 'V', 'S', 'Z', '7'],
       ['W', 'B', 'U', 'T', 'I', '8'],
       ['J', '0', '1', '2', '3', '9']]

# Grouping length.
period = 5

# Function to encrypt using Bifid Cipher :
def encrypt(P) :
    
    C = ''  # Resultant cipher.
    rows = []
    cols = []
    
    # Traversing each character of the password to get it's row and column in the key matrix :
    for char in P :
        
        for i in range(len(key)) :

            if char in key[i] :
                
                rows.append(i)
                
                col = key[i].index(char)
                cols.append(col)
    
    
    midCipher = ''
    rowLen = len(rows)
    
    # Grouping the row, column indices and joining :
    for i in range(0, rowLen, period) :
        
        for j in range(i, min(i + period, rowLen)) :
            midCipher += str(rows[j])
        
        for j in range(i, min(i + period, rowLen)) :
            midCipher += str(cols[j])

    # Creating cipher with coresponding row and column after grouping :
    for i in range(0, len(midCipher), 2) :
        row = int(midCipher[i])
        col = int(midCipher[i + 1])
        
        C += key[row][col]
    
    return C

# Function to decrypt using Bifid Cipher :
def decrypt(C) :
    
    
    P = ''
    rows = []
    cols = []
    
    # String that stores the row and col of each character in Cipher text.
    midCipher = ''
    

    # Finding row and column of each char of Cipher text :
    for char in C :
        
        for i in range(len(key)) :

            if char in key[i] :
                
                # If current character is found in the ith row of the key then append the row to the string "midCipher".
                midCipher += str(i)
                
                col = key[i].index(char)  # Corresponding column.
                
                midCipher += str(col)


    # Re-grouping the row and column indices :
    for i in range(0, len(midCipher), period + period) :
        
        if i + period + period <= len(midCipher) :
            rows += list(midCipher[i : period + i])
            cols += list(midCipher[period + i: period + period + i])
        
        
        else :
            Len = len(midCipher) - i
            rows += list(midCipher[i : i + Len // 2])
            cols += list(midCipher[i + Len // 2 :])

    # Finding corresponding plain text :
    for i in range(len(rows)) :
        
        P += key[int(rows[i])][int(cols[i])]


    return P
