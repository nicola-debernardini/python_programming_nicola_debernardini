'''
FORWARD ALGORITHM

-------------------------------------------------
Input:
The forward algorithm take in input a sequence and the parameters that the scribe a hidden markov model. The markovian models are probabilistic models 
able to generate sequences with different probability, and they are decribed by transition porbabilities between states ex. k to l (akl), and emissions porbabilities 
of a character (c) from a state k (ekc). Each sequence is the results of two stochastic processes:
- the generation of a path as a sequence of states 
- generation of a sequence of characters for eache state 
and the results is strictly related to the parameters that describe the models.

Algorithm at work:
The forward algorithm is able to calculate the probability of the sequence (took as input) given the model -> P(s|M) by summing up the probability of each different
path to generate the sequence -> SUM P(s,path|M)
In particular during the computation the program implement the folloing formula using a dynamic programming approach:
Fk(i) = ek(i) * SUM [ Fl(i-1) * alk ]
It is the probability of generating the sequence up to the (i) character ending in the state (k) -> P(s1 s2 s3 ... si, path(i)=k|M)

Output:
The output is the probability of the sequence given the model -> P(s|M)

--------------------------------------------------

PSEUDOCODE 

- Define a function (prettymatrix) to print matrix in a nice way:
	- Fro i that iterates through the length of the matrix:
		- print every line of the matrix 

- Define a function (matrix) to generate a matrix of dimensions (n_col, n_row):
	generate a matrix using two for cycle = [[0 for col in range(c_col)]for r in range(n_row)] 
	return the matrix m
	OR:
	m = []
	for r in range(n_row):
		m.append([])
		for c in range(n_col):
			m[r].append(0)
	print (m)

- Define the forward function (seq,t,e,states):
	- ncol = calculate the number of columns as the length of character of the sequence plus 2 
	- nrow = calculate the number of row as the number of states of the model (length of the states list)
	- generate a matrix m using the function matrix (ncol, nrow)

	# Initialize the matrix writing in the first cell: 1
	- m [0][0] = 1

	# Start filling in the matrix 
	# second column:
	- For cycle that iterates through the rows:
		- Write in every cell the producto of the transition probability from the 'B' state to the 'k' state and the emission prob of the first character of the sequence from the state 'k'
		m [r][1] = states['B'][states[r]]*e[states[r]][seq[0]]

	# Iteration:
	# Three nested for cycle to fill in the matrix implemnting the formula: Fk(i) = ek(i) * SUM [ Fl(i-1) * alk ]
	- For cycle that iterates through the columns (except the first two and the last one): # it is important that the iteration occours through the columns while it is occuring also through the rows 
		- For cycle that iterates through the rows (except the first and the last):
			-For cycle that iterates through the states (except the 'B' an the 'E' states):
				- m [r][c] += m[r][c-1] * t[states[stat]][states[r]] # the value in the current position is equal to SUM [ Fl(i-1) * alk ]
			- m [r][c] =  m [r][c] * e[states[r]][seq[c-1]] # In order to reduce the number of calculations is possible to multiply the emissions probability only at the sum of the previous count

	# Termination:
	# Sum the value for every states stored in the cecond last column in the cell m[nrow][ncol]
	- For cycle through the second last column:
		m[nrow-1][ncol-1] += m[r][ncol-2] 
	- Return the probability of the sequence stored in the last cell

# define the main of the script
if __name__ =='__main__':
	- Initialize a variable (seq) containing the sequence 
	- Initialize a dictionary (t) containing the transition probability  
	- Initialize a dictionary (e) containing the emission probability 
	- Initialize a list containing the states of the model (B,Y,N,E)	
	- P_s = Call the function: forward (seq,t,e,states)
	- Print the sequence and the probability of the sequence(P_s)

----------------------------------------------------
'''
# HMM - FORWARD

############
# Print a matrix:
def prettyMatrix (M):
	for i in range(len(M)):
		print(M[i])

############
t = {
	'B':{'Y':0.2,'N':0.8}, \
	'Y':{'Y':0.7,'N':0.2,'E':0.1}, \
	'N':{'Y':0.1,'N':0.8,'E':0.1} \
    }

e = {
	'Y':{'A':0.1,'C':0.4,'G':0.4,'T':0.1}, \
	'N':{'A':0.25,'C':0.25,'G':0.25,'T':0.25} \
    }

seq = 'ATGC'
states = ['B','Y','N','E']

############
def forward(s,states,t,e):
	c = len(s)+2 #numero colonne 
	r = len(states) #numero righe 

	# Define a matrix:
	F = [[0.0 for col in range(c)] for row in range(r)]

# Inizializazione 
	F [0][0]= 1
	for i in range(1,r-1):
		F [i][1] = t['B'][states[i]]*e[states[i]][seq[0]]
	
# Iteration
	for j in range(2,c-1):
		for i in range(1,r-1):
			score = 0

			for stat in range(1,r-1):
				score += F [stat][j-1]*t[states[stat]][states[i]]
			F [i][j] = score*e[states[i]][seq[j-1]] 		 

# Terminazione 
	score = 0.0

	for stat in range(1,r-1):
		score += F [stat][c-2]*t[states[stat]]['E'] 
	
	F [r-1][c-1] = score
	return F
############

M = None 
M = forward(seq,states,t,e)

prettyMatrix(M) 
P_s = M[len(states)-1][len(seq)+1]
print('\nP(s|M) = %f' %P_s)
print('La probabilità è calcolata per la seguente sequenza: ',seq) 
