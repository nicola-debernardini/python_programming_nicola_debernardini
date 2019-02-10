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
#           
# T 

# BUILDING A MATRIX
# n° colonne = len(seq1)+1
# n° righe = len(seq2)+1

# DEFINING GAP PENALTIES
# gap_pen = -1

# DEF A FUNCTION 
# s(a,b) --> a=b 1
#        --> a != b -1

# INITIALIZATION 
# colum1 = 0 
# row1 = 0
# DEFIN A MATRIX WHERE TO SAVE THE RESULT 
#   0   A   C   T   G   G 
# 0 0   0   0   0   0   0 
#    
# A 0
#         
# C 0
#           
# T 0  

# COMPUTATION 
#   0   A   C   T   G   G 
# 0 0   0   0   0   0   0 
#     \
# A 0   1   0   0   0   0 
#         \
# C 0   0   2   1   0   0
#             \
# T 0   0   1   3 <-2 <-1

# REMEMBER TRACEBACK BY BUILDING AN OTHER MATRIX
#   0   A   C   T   G   G 
# 0 0   0   0   0   0   0 
#     
# A 0   D 
#      
# C 0   0   D   R      
#             
# T 0   0   C   D   R   R


# FIND THE HIGHEST VALUE IN THE MATRIX
# find the index (i,j) with the highest value 


# READ THE TRACEBACK
# i,j = 3,3
# this is the first match 
# w = '' + seq1[i-1]
# z = '' + seq2[j-1]

# let start to move
# if D:
# i = -1
# j = -1
# w = w + seq1[i-1]
# z = z + seq2[j-1]

# if R: 
# i = i 
# j = -1
# w = w + '-'
# z = z + seq2[j-1]

# if C: 
# i = -1 
# j = j
# w = w + seq1[i-1]
# z = z + '-'


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
seq1 = 'AGTGAAGTCTGATCGGGACGCTAGCG'
seq2 = 'AGTCAACACTAGGTACGTATCGGGGATC'


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
for j in range(c):
	score_matrix [0][j] = 0
for i in range(r):
	score_matrix [i][0] = 0

# prettyMatrix(score_matrix)

scores = [0,0,0,0]
max_score = 0
pos_max = [0,0]

##test
#print(len(score_matrix))
#print(len(score_matrix[0]))
#print(c)
#print(r)
######

for i in range(1,r):
#	print(i,' questo è i')
	for j in range(1,c):
#		print(score_matrix[i-1][j])
#		print(score_matrix[i][j-1])
#		print(j)
#		print(score_matrix[i-1][j-1]+sc(seq1[j-1],seq2[i-1]),'diag')
#		print(score_matrix[i-1][j]+d,' up')
#		print(score_matrix[i][j-1]+d,' laterlral')
		scores = [score_matrix[i-1][j-1]+sc(seq1[j-1],seq2[i-1]),score_matrix[i-1][j]+d,score_matrix[i][j-1]+d,0]
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
		
		if max(scores) > max_score:
			max_score = max(scores)
			pos_max = (i,j)

print('\n',pos_max,' ',max_score)				

#print('\n')
#prettyMatrix(score_matrix)
#print('\n')
#prettyMatrix(traceback)	
	
maxI = pos_max[0]
maxJ = pos_max[1]

#alin1 = ['0']
#alin2 = ['0']
#alig1 = seq1[maxJ-1]
alig1 = ''
#alig2 = seq2[maxI-1]
alig2 = ''


while max_score != 0:
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
#		maxI = maxI-1
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


	
		
		







