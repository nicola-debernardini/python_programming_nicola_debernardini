################################################
# Needlman Wunsh: no gaps penalties at the end #
################################################

def prettyMatrix (M):
    for i in range(len(M)):
        print(M[i])
    return

def initial_matrix (seq1,seq2,gap):
    S1 = len(seq1)
    S2 = len(seq2)
    matrix = [[0 for col in range (S1+1)] for row in range (S2 +1)]
    return matrix


def maxScore(up, left, diag, gap, match, mismatch, char_seq1, char_seq2):
    if char_seq1 == char_seq2:
        D = diag + match 
    else:
        D = diag + mismatch

    L = left + gap
    U = up + gap
    Max = max(D,L,U)
    return Max    


def N_W(seq1, seq2, gap, mismatch, match):
    
    S1 = len(seq1)
    S2 = len(seq2)
    Score_matrix = initial_matrix (seq1, seq2, gap)

    # Iteration --> fill the matrix with the scores of the optimal sustring alignment 
    for row in range (1, S2+1): #traverse the row
        for col in range (1, S1 +1): #traverse the colum
            Score_matrix [row][col] = maxScore(Score_matrix [row-1][col], Score_matrix [row][col-1], Score_matrix [row-1][col-1], gap, match, mismatch, seq1[col-1], seq2[row-1])#assign to the current cell the max value among the three

    # Traceback --> prooced backward from the last cell until the first cell (up,left), following the cell containing the higher scores
    alignment1 = ''
    alignment2 = '' 
    is_match = ''

    # Find the cell containg the higher score 
    cell_max = float('-inf')
    cell_max_pos = None 
    for row in range(1,S2+1):
        if Score_matrix [row][S1] > cell_max:
            cell_max = Score_matrix [row][S1]
            cell_max_pos = (row, S1)

    for col in range(1,S1+1):
        if Score_matrix [S2][col] > cell_max:
            cell_max = Score_matrix [S2][col]
            cell_max_pos = (S2, col)
    
    c_row = cell_max_pos[0]
    c_col = cell_max_pos[1]

    ##############
    # Traceback 
    if c_row == S2:
        num_gap = S1 - c_col 
        for i in range(S1,S1-num_gap,-1):
            alignment1 += seq1[i-1]
        alignment2 = '-'*num_gap 
    elif c_col == S1:
        num_gap = S2 - c_row 
        for j in range(S2,S2-num_gap,-1):
            alignment2 += seq2[j-1]
        alignment1 = '-'*num_gap 


    while (c_col > 0 and c_row > 0): # while the current position of the cell is not Score_matrix [0][0] 
        aroundMax = float('-inf') # initialize a variable to minus infinit  
        Max_position = None
        aroundMax = max(Score_matrix [c_row-1][c_col-1], Score_matrix [c_row][c_col-1], Score_matrix [c_row-1][c_col])
        
        if  aroundMax == Score_matrix [c_row-1][c_col-1]: 
            alignment1 += seq1 [c_col-1]
            alignment2 += seq2 [c_row-1]

            if seq1[c_col-1] == seq2[c_row-1]:
                is_match += '|'
            else:
                is_match += '?'    
            
            c_col -= 1
            c_row -= 1

        elif aroundMax == Score_matrix [c_row][c_col-1]:
            alignment1 += seq1 [c_col-1]
            alignment2 += '-'
            is_match += ' '
            c_col -= 1

        elif aroundMax == Score_matrix [c_row-1][c_col]:
            alignment1 += '-'
            alignment2 += seq2 [c_row-1]
            is_match += ' '
            c_row -= 1
    
    if c_col == 0:
        while c_row != 0:
            alignment1 += '-'
            alignment2 += seq2 [c_row-1]
            is_match += ' '
            c_row -= 1
    
    if c_row == 0:
        while c_col != 0:
            alignment2 += '-'
            alignment1 += seq1 [c_col-1]
            is_match += ' '
            c_col -= 1

    alignment1 = alignment1[::-1]
    alignment2 = alignment2[::-1]
    is_match = is_match[::-1]

    #prettyMatrix(Score_matrix)
    print (alignment1)
    print (is_match) 
    print (alignment2)

    return alignment1, alignment2, is_match, Score_matrix  



if __name__ == '__main__':
    seq1 = 'AGCGTATTCTCCTAACGATCGTC' 
    seq2 = 'TTCTGCTAA'

    print (seq2,seq1)

    gap = -1
    mismatch = -1
    match = 1
    al1, al2, is_match, score_matrix = N_W (seq1, seq2, gap, mismatch, match)
    prettyMatrix(score_matrix)