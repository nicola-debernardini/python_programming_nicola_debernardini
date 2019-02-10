'''
--------------------------------------------

Needlman-Wunsh algorithm:

Input:
The algorithm take in input two DNA sequences and a scoring matrix and compute their global alignment.

Algorithm at work:
The algorithm implement a dinamic programming approach that by reducing the complexity of the naif algorithm make the computation feaseble. 
In particular the agorithm performs the optimal alignment by adding one gap or one character at the time to substrings of the sequences.
The optimal solution is choose by selecting the one of the folloing result that maximize the alignment score of every pair of substring:
- previous left_score + gap penalties
- previous score + match/mismatch
- previous up_score + gap penalties 
The substitution score is independent from the position of the character in the sequence and the type of gap penalties adopted is linear. 

Output:
The output is the global alignment between the two sequences.

-----------------------------------------------

PSEUDOCODE:

- Define a function to initialize a matrix (two sequences, gap penalties):
	- Calculate the length of the two sequence 
	- Generate a matrix (length of the first sequence +1) X (length of the second sequence +1) 
	- Initialize the matrix filling it with 0 in cell [0][0] and with gap penalties multiplied by the row and colum index in the frist row and colum 
	- Return the matrix 

#############
- Define a function to intialize a traceback matrix (seq1, seq2):
    - Calculate the length of the two sequence 
	- Generate a matrix (length of the first sequence +1) X (length of the second sequence +1) 
	- Initialize the matrix filling it with '0' the cell [0][0] with 'L' the cell in the first row and with 'U' the cell in the first column  
	- Return the matrix 
#############

- Define a fuction to calculate the max score of a specific cell (score of the up cell, left cell, diag cell, gap, match, mismatch, character(seq1), character(seq2)):
	- variable 'left' = left score + gap 
	- variable 'up' = up score + gap 
	- if char(seq1) == char(seq2):
		- variable 'diag' = score diag + match 
	- else:
		- 'diag' = score diag + mismatch  
	- m = store the max between ('diag', 'left', 'up')
	- return( )


- Define the Needleman-Wunsh algorithm function (seq1, seq2, gap, mismatch, match):
	- matrix = call the finction to initialize the matrix 
	- for cycle that traverse the columns:
			- for cycle that traverse the rows:
				- matrix [i][j] (cell in a specific position) = call the finction to calculate the max score of a specific cell 

	Create two variable (data structure type: string: alignment 1 and 2)
	while the cell take in cosideration is not the cell [0][0]: 
		Startin form the last cell (down,right) determin which of the three value (up, down or diag) is the higner and save its position 
		if the upper value in the higher:
			insert a gap ('-') in the variable 'alingment 1'
			and add the charcter correspondent to the seq2(position y of the cell -1) to 'alignment 2'
            and insert ' '  a space in variable is_match
        elif the left value is the higher:
			insert a gap in the variable 'aligment 2'
			and add the charcter correspondent to the se1(position x of the cell -1) to alignment 1
            and insert ' '  a space in variable is_match
        else:
			add the correcpondent character to alignmet 2 and 1 
            and insert '|'  in variable is_match
		move in the new position
	
	reverse alignment 1 alignment 2 and is_match 
	return the alingment 1 and 2 and is_match 

###############
# Main:

- Input the two DNA sequences
- Define the gap penalties, match and mismatch 
- call the Needlman and Wunsh function
- print to the screen the sequences and the global alignment 
'''

################### NEEDLMAN_WUNSH ####################



###########
def initial_matrix (seq1,seq2,gap):
    S1 = len(seq1)
    S2 = len(seq2)
    matrix = [[0 for i in range (S1+1)] for j in range (S2 +1)]
    for i in range(S1 +1):
        matrix [0][i] = gap * i
    for j in range(S2 +1):
        matrix [j][0] = gap * j
    return matrix

#############
# function to calculate the max score of each cell
def maxScore(up, left, diag, gap, match, mismatch, char_seq1, char_seq2):
    L = left + gap
    U = up + gap
    if char_seq1 == char_seq2:
        D = diag + match 
    else:
        D = diag + mismatch
    Max = max(D,L,U)
    return Max

############
# Needlman Wunsh 
def N_W(seq1, seq2, gap, mismatch, match):
    
    S1 = len(seq1)
    S2 = len(seq2)
    Score_matrix = initial_matrix (seq1, seq2, gap)

    # Iteration --> fill the matrix with the scores of the optimal sustring alignment 
    for i in range (1, S2+1): #traverse the row
        for j in range (1, S1 +1): #traverse the colum
            Score_matrix [i][j] = maxScore(Score_matrix [i-1][j], Score_matrix [i][j-1], Score_matrix [i-1][j-1], gap, match, mismatch, seq1[j-1], seq2[i-1])#assign to the current cell the max value among the three

    # Traceback --> prooced backward from the last cell until the first cell (up,left), following the cell containing the higher scores
    alignment1 = ''
    alignment2 = '' 
    is_match = ''

    while (i != 0 and j != 0): # while the current position of the cell is not Score_matrix [0][0] 
        aroundMax = float('-inf') # initialize a variable to minus infinit  
        Max_position = None
        aroundMax = max(Score_matrix [i-1][j-1], Score_matrix [i][j-1], Score_matrix [i-1][j])
        if  aroundMax == Score_matrix [i-1][j-1]:
            alignment1 += seq1 [j-1]
            alignment2 += seq2 [i-1]
            if seq1[j-1] == seq2 [i-1]:
                is_match += '|'
            else:
                is_match += '.'    
            
            i -= 1
            j -= 1

        elif aroundMax == Score_matrix [i][j-1]:
            alignment1 += seq1 [j-1]
            alignment2 += '-'
            is_match += ' '
            j -= 1

        else:
            #aroundMax == Score_matrix [i-1][j]:
            alignment1 += '-'
            alignment2 += seq2 [i-1]
            is_match += ' '
            i -= 1
  

    alignment1 = alignment1[::-1]
    alignment2 = alignment2[::-1]
    is_match = is_match[::-1]
    return alignment1, alignment2, is_match, Score_matrix  

###########
def prettyMatrix (M, file_out):
    for i in range(len(M)):
        j = str(M[i])
        file_out.write(j+'\n')
    return

###########
# Main: TAke the input and writhe the output from two different file

if __name__ == '__main__':
    import sys
    READ = sys.argv[1] # Take an input from the keybord 
    WRITE = sys.argv[2]
    file_read = open(READ) # Open a file 
    file_out = open(WRITE, 'w') # Open a writable file 
    
    l = []
    for i in file_read:
        i = i.strip() # Strip a string 
        print(len(i)) 
        l.append(i) # Append an element to a list 
    
    seq1 = l[0] 
    seq2 = l[1]

    print (seq2,seq1)

    gap = -1
    mismatch = -1
    match = 1
    al1, al2, is_match, score_matrix = N_W (seq1, seq2, gap, mismatch, match)
    
    file_out.write(al1+'\n') # Write the output in a file ... NB it accpet only one argument 
    file_out.write(is_match+'\n')
    file_out.write(al2+'\n\n')
    prettyMatrix(score_matrix, file_out)
    file_out.close() # Close the file 