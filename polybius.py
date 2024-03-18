

# Polybius Cipher Implementation :

# Polybius Square :

'''square = [['\0', 'A', 'B', 'C', 'D', 'E'],
         ['A',   'p', 'h', 'q', 'g', 'm'],
         ['B',   'e', 'a', 'y', 'l', 'n'],
         ['C',   'o', 'f', 'd', 'x', 'k'],
         ['D',   'r', 'c', 'v', 's', 'z'],
         ['E',   'w', 'b', 'u', 't', 'i']]'''


#                 1    2    3    4    5    6    7    8    9    10
square = [['\0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
         ['A',   'p', 'h', 'q', 'g', 'm', '4', 'P', 'H', 'Q', 'G'],  # 1
         ['B',   'e', 'a', 'y', 'l', 'n', '5', 'E', 'A', 'Y', 'L'],  # 2
         ['C',   'o', 'f', 'd', 'x', 'k', '6', 'O', 'F', 'D', 'X'],  # 3
         ['D',   'r', 'c', 'v', 's', 'z', '7', 'R', 'C', 'V', 'S'],  # 4
         ['E',   'w', 'b', 'u', 't', 'i', '8', 'W', 'B', 'U', 'T'],  # 5
         ['F',   'j', '0', '1', '2', '3', '9', 'J', 'M', 'N', 'K'],  # 6
         ['G',   'Z', 'I', '!', '"', '#', '$', '%', '&', '\\', "'"],  # 7
         ['H',   '(', ')', '*', '+', ',', '-', '.', '/', ':', ';'],  # 8
         ['I',   '<', '=', '>', '?', '@', '[', ']', '^', '_', '`'],  # 9
         ['J',   '{', '|', '}', '~']]  # 10


# Function to encrypt plain text using Polybius Cipher :
def encrypt(P) :
    
    # Resultant cipher text.
    C = ''
    
    for char in P :
        
        # Searching in polybius square.
        for row in range(1, len(square)) :
            if char in square[row][1:] :
                
                # Adding corresponding first column letter of current row :
                C += square[row][0]
                
                # Adding corresponding first row letter of current column :
                
                # Finding column.
                col = square[row].index(char)
                
                C += square[0][col]
    
    return C


# Function to decrypt plaintext using Polybius Cipher :
def decrypt(C) :
    
    C = C.upper()
    
    # Resultant plain text.
    P = ''
    
    # Initializing a row variable.
    row = -1
    
    for i in range(0, len(C), 2) :
        
        # Finding row of corresponding plain text.
        for j in range(1, len(square)) :
            if square[j][0] == C[i] :
                row = j
                break

        # Finding column of corresponding plain text.
        col = square[0].index(C[i + 1])
        
        P += square[row][col]
    
    return P

