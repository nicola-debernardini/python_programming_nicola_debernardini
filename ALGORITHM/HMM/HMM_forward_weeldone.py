# HMM - forward

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
	F = [[0.0 for i in range(c)] for j in range(r)]

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

print('\nP(s|M) =', M[len(states)-1][len(seq)+1])
print('La probabilità è calcolata per la seguente sequenza: ',seq) 
