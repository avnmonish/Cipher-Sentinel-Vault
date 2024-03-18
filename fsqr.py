


# Four Square Implementation :


S1 = [['A', 'B', 'C', 'D', 'E'],
      ['F', 'G', 'H', 'I', 'K'],
      ['L', 'M', 'N', 'O', 'P'],
      ['Q', 'R', 'S', 'T', 'U'],
      ['V', 'W', 'X', 'Y', 'Z']]

S4 = [['V', 'W', 'X', 'Y', 'Z'],
      ['Q', 'R', 'S', 'T', 'U'],
      ['L', 'M', 'N', 'O', 'P'],
      ['F', 'G', 'H', 'I', 'K'],
      ['A', 'B', 'C', 'D', 'E'],
      ['J']]

# Function to generate squares :
def generate_squares(k1, k2) :
    
    k1 = k1.upper()
    k2 = k2.upper()
    
    # Appending alplhabets to keys :
    S2 = k1 + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    S3 = k2 + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    # Removing duplicates :
    S2 = ''.join(sorted(set(S2), key = S2.index))
    S3 = ''.join(sorted(set(S3), key = S3.index))

    # Splitting as table :
    S2 = [list(S2[i : i + 5]) for i in range(0, 25, 5)]
    S3 = [list(S3[i : i + 5]) for i in range(0, 25, 5)]
    
    return S2, S3
    

# Function to encrypt plain text :
def encrypt(P, k1, k2) :

    P = P.upper()
    
    # Making length of plaintext even :
    if len(P) % 2 == 1 :
        P += 'Y'

    # Key Matrices.
    S2, S3 = generate_squares(k1, k2)
    
    # Resultant Cipher text.
    C = ''
    
    S1r = 0
    S1c = 0
    S4r = 0
    S4c = 0
    
    # Traversing each character of plaintext :
    for j in range(0, len(P), 2) :
        
        # Row, col index in S1 :
        for i in range(0, 5) :

            if P[j] in S1[i] :
                S1r = i
                S1c = S1[i].index(P[j])
                break
        
        # Row, col index in S4 :
        for i in range(0, 5) :
            
            if P[j + 1] in S4[i] :
                S4r = i
                S4c = S4[i].index(P[j + 1])
                break
        
        
        C += S2[S1r][S1c] + S3[S4r][S4c]

    return C


# Function to decrypt the plain text :
def decrypt(C, k1, k2) :
    
    # Resultant Plain text.
    P = ''
    
    C = C.upper()
    
    # Key Matrices.
    S2, S3 = generate_squares(k1, k2)
    
    S2r = 0
    S2c = 0
    S3r = 0
    S3c = 0
    
    # Traversing each character of ciphertext :
    for j in range(0, len(C), 2) :
        
        # Row, col index in S2 :
        for i in range(0, 5) :

            if C[j] in S2[i] :
                S2r = i
                S2c = S2[i].index(C[j])
                break
        
        # Row, col index in S3 :
        for i in range(0, 5) :

            if C[j + 1] in S3[i] :
                S3r = i
                S3c = S3[i].index(C[j + 1])
                break
        
        
        P += S1[S2r][S2c] + S4[S3r][S3c]
    
    return P if P[-1] != 'Y' else P[:-1]


# Input plaintext will only be adfgvx.

