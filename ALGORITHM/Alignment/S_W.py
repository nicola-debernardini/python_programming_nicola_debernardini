'''
What does the algorithm does? 
The algorithm take in input two DNA sequences and a scoring matrix and compute the best local alignment.

The algorithm implement a dinamic programming approach that make the computation feaseble by reducing the complexity of the naif algorithm.
In particular the agorithm performs the optimal local alignment between two sequences proceeding step by step 
choosing between the higher score among the following possibility:
- previous score + gap penalties
- previous score + match 
- previous score + mismatch 
- 0

              | F(i-1,j-1) + s(Pi,Bj)
F(i,j) = Max {  F(i-1,j) -d
              | F(i,j-1) -d
			  | 0

The substitution score is independent from the position in the sequence and the gap penalties type is linear. 
The output are the two local aligned sequences.

#############################
PSEUDOCODE:

- Input the two DNA sequences
- Define the gap penalties, match and mismatch 

Define a function to initialize a matrix (two sequences):
	- Calculate the length of the two sequence 
	- Generate a matrix that has a number of colums equal to the number character of the first sequence +1 and number of row equal to the number of character of the second sequence +1
	- Initialize the matrix filling the frist row and colum with 0
	- Return the matrix 

Define a function to initialize a traceback (two sequences):
	- Calculate the length of the two sequence 
	- Generate a matrix that has a number of colums equal to the number character of the first sequence +1 and number of row equal to the number of character of the second sequence +1
	- Initialize the matrix filling the frist row and colum with 'Ter'
	- Return the matrix 
	
Define a fuction to calculate the max score of a specific cell (score of the up cell, left cell, diag cell, gap, match, mismatch, character(seq1), character(seq2)):
	- define the variable: DIR to store the direction 
	- variable 'left' = left score + gap 
	- variable 'up' = up score + gap 
	if char(seq1) == char(seq2):
		- variable 'diag' = score diag + match 
	else:
		- 'diag' = score diag + mismatch  

	m = store the max between ('diag', 'left', 'up',0)
	if m == diag: 
		DIR = Diagonal 
	else, if m == left:
		DIR = left
	else 
		DIR = up

	return: m and DIR


Define the Smith-Waterman algorithm function (seq1, seq2, gap, mismatch, match):
	matrix = call the function to initialize the matrix 
	traceback = call the function to initialize a traceback matrix 
	define a variable Pos_matrix_max to determine which is the cell with the higher score 
	define a variable matrix_max to determine which is the higher score in the matrix

	for cycle that iterates through the colum number:
			for cycle that iterates through the row number:
				matrix [i][j] (Assign to the cell in position i, j) = call the finction to calculate the max score of a specific cell 
				if matrix [i][j] it is now higer of matrix_max:
					save the value of matrix [i][j] in matrix_max
					Pos_matrix_max equal to the position of this cell

	Create two variable (data structure type: string: alignment 1 and 2)
	while the value in the cell take into cosideration is not 'Ter': 
		Starting form the cell correspondent to (Pos_matrix_max) 
		if the value in the cell is 'diag':
			add the correcpondent character to alignmet 2 and 1 
            if the two character are =:
				insert '|'  in variable is_match
			else:
				insert '.' in variable is_match 

			subtract -1 to both j and i
		
		elif the value in the cell is 'up':
			insert a gap ('-') in the variable 'alingment 1'
			and add the charcter correspondent to the seq2(position y of the cell) to 'alignment 2'
            and insert (' ') a space in variable is_match
			subtract -1 to j

        else:
			insert a gap in the variable 'aligment 2'
			and add the charcter correspondent to the se1(position x of the cell) to alignment 1
            and insert (' ') a space in variable is_match
			subtract -1 to i

		move in the new position
	
	reverse alignment 1 alignment 2 and is_match 
	
	print alignment 1
	print match 
	print alignment 2

	return the alingment 1 and 2 and is_match 

call the Needlman and Wunsh function
'''

# Function to print matrix in a nice way:
def prettymatrix(M):
	for i in M:  # i assume the value of every line of the matrix 
		print(i) # print the matrix line by line 


# Scoring matrix initializing function:
def scoringMatrix (seq1,seq2):
	c = len(seq1)+1 # num colum 
	r = len(seq2)+1 # num row 
	scoring_matrix = [[0 for i in range(c)]for j in range (r)] # new scoring matrix with c columns and r rows  
	return scoring_matrix

# Traceback matrix inizializing finction 
def tracebackMatrix (seq1,seq2):
	c = len(seq1)+1 # num colum 
	r = len(seq2)+1 # num row 
	Traceback = [[' ' for i in range(c)]for j in range (r)]  # new traceback matrix with c columns and r rows  
	for i in range(c): # iterate through the columns 
		Traceback [0][i] = 'T' # print 'T' in all the cell of the first row
	for j in range(r):
		Traceback [j][0] = 'T'
	return Traceback


# Function to calculate me max among the scores
#				| 0
# 				| F(j,i-1) - d
# F(j,i) = MAX {  F(j,i) + S(Pj,Bi)
#				| F(j-1,i) -d
def scoring_function(left, up, diag, gap, match, mismatch, char_seq1, char_seq2):
	DIR = None
	L = left + gap # F(j,i-1) - d
	U = up + gap   # F(j-1,i) - d
	if char_seq1 == char_seq2: # if Pj == Bi
		D = diag + match # F(j,i) + S(Pj,Bi)
	else:
		D = diag + mismatch # F(j,i) + S(Pj,Bi)
	
	Max = max(L,D,U,0)

	# the order in which the following condition are verified matters   
	if Max == 0:
		DIR = 'T' # if the max value among the once calulated is zero return 'T' as direction
	elif Max == U:
		DIR = 'up'
	elif Max == L:
		DIR = 'left'
	else:
		DIR = 'diag'
	return Max, DIR


# Smith_Waterman function
def S_W (seq1, seq2, gap, match, mismatch):
	try: # verify if the sequence is a DNA sequence 
		if (set(seq1) != {'A','G','C','T'} or set(seq2) != {'A','G','C','T'}):
			error = float(' ') # if it is not a DNA sequence return an error thus it perform the exception
	except:
		print ('Program usage: python S_W.py <DNA_Seq1> <DNA_Seq2>')
		print ('where <DNA_Seq1> <DNA_Seq2> are DNA sequences composed at least by one or more of the nucleic acids bases: A, T, G and C') #specify to the user that the sequences must be DNA
		raise SystemExit 
	else:
		c = len(seq1)+1 # num colum 
		r = len(seq2)+1 # num row 
		scores_matrix = scoringMatrix (seq1,seq2) # call the scoringMatrix function and define the scoring matrix
		traceback_matrix = tracebackMatrix (seq1,seq2)
		Max_matrix = float('-inf')
		Pos_matrix_max = (0,0)
		
		##################
		# Iteration #
		# For cycles through the cells of the matrix to fill them in 
		for j in range(1,r):
			for i in range (1,c):
				scores_matrix [j][i], traceback_matrix [j][i] = scoring_function (scores_matrix [j-1][i], scores_matrix [j][i-1], scores_matrix [j-1][i-1], gap, match, mismatch, seq1[i-1], seq2[j-1]) 
				
				# assessed condition to determine which is the cell containing the higher score in the whole matrix
				if scores_matrix [j][i] > Max_matrix:
					Max_matrix = scores_matrix [j][i] # higher score in the cell
					Pos_matrix_max = (j,i) # position of the cell

		# print the two matrix	
		prettymatrix(traceback_matrix)			
		prettymatrix(scores_matrix)

		# define the variables to save the alignment 
		alignment1 = ''
		alignment2 = ''
		is_match = ''
		maxj = Pos_matrix_max[0]
		maxi = Pos_matrix_max[1]
		print (maxj,maxi)

		#######################
		# Traceback #
		while traceback_matrix [maxj][maxi] != 'T': # Until the value of the cell in traceback matrix do not become 'T' --> termination, continue to do ...
			if traceback_matrix [maxj][maxi] == 'diag': # if in the trace backmatrix the value is diag move of a diagonal step in the matrix  
				alignment1 += seq1[maxi-1]
				alignment2 += seq2[maxj-1]
				if seq1[maxi-1] == seq2[maxj-1]:
					is_match += '|'
				else:
					is_match += '·'

				maxi -= 1
				maxj -= 1

			elif traceback_matrix [maxj][maxi] == 'left':
				alignment1 += seq1[maxi-1]
				alignment2 += '-'
				is_match += ' '
				
				maxi -= 1
				maxj -= 0

			else:
				alignment1 += '-'
				alignment2 += seq2[maxj-1]
				
				is_match += ' '
				
				maxi -= 0
				maxj -= 1
			print(maxj,maxi)


		alignment1 = alignment1 [::-1]
		alignment2 = alignment2 [::-1]
		is_match = is_match [::-1]
	
	print (alignment1)
	print (is_match) 
	print (alignment2)

	return alignment1, alignment2, is_match
		 
if __name__ == '__main__':
	import sys 
	try:
		seq1 = sys.argv[1]
		seq2 = sys.argv[2]
	except: 
		print('Program usage: python S_W.py <Seq1> <Seq2>')
		raise SystemExit 
	else:
		#Parameter of the scoring matrix 
		gap = -2
		match = 1
		mismatch = -2	
		
		al1, al2, mat = S_W (seq1, seq2, gap, match, mismatch)
		