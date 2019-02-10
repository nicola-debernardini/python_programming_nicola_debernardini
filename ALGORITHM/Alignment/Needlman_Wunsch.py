'''
What does the algorithm does? 
The algorithm take in input two DNA sequences and a scoring matrix and compute their global alignment.

The algorithm implement a dinamic programming approach that make the computation feaseble. In particular
the agorithm performs the optimal alignment between the two sequences (progressing step by step) 
by chose the solution that maximize the score of the substring between the following possibility:
previous score + gap penalties
previous score + match 
previous score + mistmatch 
The substitution score is independent from the position and the gap penalties is linear. 

The output are the two aligned sequences.

#############################à
PSEUDOCODE:

- Input the two DNA sequences
- Calculate how long are the sequences
- Define the gap penalties 

Define a function to initialize a matrix (two sequences, gap penalties):
	- Calculate the length of the two sequence 
	- Generate a matrix that has a number of colums equal to the number character of the first sequence +1 and number of row equal to the number of character of the second sequence +1
	- Initialize the matrix filling it with 0 in cell [0][0] and with gap penalties multiplied by the row and colum index in the frist row and colum 
	- Return the matrix 

Define a fuction to calculate the max score of a specific cell (score of the up cell, left cell, diag cell, gap, match, mismatch, character(seq1), character(seq2)):
	- variable 'left' = left score + gap 
	- variable 'up' = up score + gap 
	if char(seq1) == char(seq2):
		- variable 'diag' = score diag + match 
	else:
		- 'diag' = score diag + mismatch  
	m = store the max between ('diag', 'left', 'up')
	return( )


Define the Needleman-Wunsh algorithm function (seq1, seq2, gap, mismatch, match):
	matrix = call the finction to initialize the matrix 
	for cycle that traverse the colum:
			for cycle that traverse the row:
				call the finction to calculate the max score of a specific cell 

	Create two variable (data structure type: string: alignment 1 and 2)
	while the cell take in cosideration is not the cell [0][0]: 
		Startin form the last cell (down,right) determin which of the three value (up, down or diag) is the higner and save its position 
		if the upper value in the higher:
			insert a gap ('-') in the variable 'alingment 1'
			and add the charcter correspondent to the seq2(position y of the cell) to 'alignment 2'
		elif the left value is the higher:
			insert a gap in the variable 'aligment 2'
			and add the charcter correspondent to the se1(position x of the cell) to alignment 1
		else:
			add the correcpondent character to alignmet 2 and 1 

		move in the new position
	
	reverse alignment 1 alignment 2 and match 
	
	print alignment 1
	print match 
	print alignment 2

	return the alingment 1 and 2
'''

# Implementation of the local alignment algorithm
#ACTGG
#ACT

# DEFIN A MATRIX WHERE TO SAVE THE RESULT 
#   0   A   C   T   G   G 
# 0   
#    
# A 
#         
# C 
#PYTHON

def prettyMatrix(m):
	for y in range(0,len(m)):
		print (m[y])

def brutalMatrix(c,r):
	m = []
	for x in range(0,r):
		m.append([])
		for y in range(0,c):
			m[x].append(0)
	return m

def sc(a,b):
	if a == b:
		v = 1
	else:
		v = -1
	return v
		

#Input sequences
seq1 = 'AGTGAGTCGTCGATCGAGACTTAGCGATCGA'
seq2 = 'AGTCATGACTACGGTACGTAGCTGGCTAGCTATCGTAGC'


#Scores
#match = 1
#mismatch = -1
#gap
d = -1


# HOW TO CREATE THE MATRIX

c = len(seq1) +1
r = len(seq2) +1

# score_matrix = [['0']*n_col]*n_row]
score_matrix = [[0 for col in range(c)]for row in range(r)]
# score_matrix [0][0] = 1

traceback = [['0' for col in range(c)]for row in range(r)]
# sc = {'MATCH':1,'MISMATCH':-1,'GAP':-1}

#inizialization 
score_matrix [0][0] = 0
for j in range(1,c):
	score_matrix [0][j] = score_matrix [0][j-1] +d
for i in range(1,r):
	score_matrix [i][0] = score_matrix [i-1][0] +d

# prettyMatrix(score_matrix)

scores = [0,0,0]

##test
#print(len(score_matrix))
#print(len(score_matrix[0]))
#print(c)
#print(r)
######

for i in range(1,r):
	for j in range(1,c):
#		print(score_matrix[i-1][j])
#		print(score_matrix[i][j-1])
#		print(j)
#		print(score_matrix[i-1][j-1]+sc(seq1[j-1],seq2[i-1]),'diag')
#		print(score_matrix[i-1][j]+d,' up')
#		print(score_matrix[i][j-1]+d,' laterlral')
		scores = [score_matrix[i-1][j-1]+sc(seq1[j-1],seq2[i-1]),score_matrix[i-1][j]+d,score_matrix[i][j-1]+d]
#		print(scores)
		score_matrix[i][j] = max(scores)

		if max(scores) == scores[0]:
			traceback[i][j] = 'D'
		elif max(scores) == scores[1]:
			traceback[i][j] = 'U'
		elif max(scores) == scores[2]:
			traceback[i][j] = 'L'
# max_score = float("-inf")
# max_position = None			

#print('\n')
prettyMatrix(score_matrix)
#print('\n')
prettyMatrix(traceback)	
	
maxI = r -1
maxJ = c -1

print(maxI)
print(maxJ)

#alin1 = ['0']
#alin2 = ['0']
#alig1 = seq1[maxJ-1]
alig1 = ''
#alig2 = seq2[maxI-1]
alig2 = ''


while maxI != 0 and maxJ != 0:
	up_element = score_matrix[maxI-1][maxJ]
	left_element = score_matrix[maxI][maxJ-1]
	diag_element = score_matrix[maxI-1][maxJ-1]
	direction = [up_element,left_element,diag_element]
	DIR = max(direction)

	if DIR == diag_element:
		alig1 += seq1[maxJ-1]
		alig2 += seq2[maxI-1]
		maxI = maxI-1
		maxJ = maxJ-1
	
	elif DIR == left_element:
		
		alig1 += seq1[maxJ-1]
		alig2 += '-'	
		maxJ = maxJ-1
	
	elif DIR == up_element:
		alig1 += '-'
		alig2 += seq2[maxI-1]
		maxI = maxI-1
	#	alin1.append('-')
	#	alin2.append('-')

	max_score = DIR

print(seq1)
print(seq2)
print(alig1[::-1])
print(alig2[::-1])


	
		
