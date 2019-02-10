# HMM - backword 

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
def backward(s,states,t,e):
	
	c = len(s)+2 #numero colonne 
	r = len(states) #numero righe 

	# Define a matrix:
	B = [[0.0 for i in range(c)] for j in range(r)]

# Inizializazione 
	for i in range(1,r-1):
		B [i][len(s)] = t[states[i]]['E']
	
# Iteration
	for j in range(len(s)-1,0,-1):

		
		for i in range(1,r-1):
			score = 0
				
			for stat in range(1,r-1):
				score += B [stat][j+1]*t[states[i]][states[stat]]*e[states[stat]][seq[j]]
				print ('B [i][j]                    ', score)
				print ('B [stat][j+1]               ', B [stat][j+1])
				print ('t[states[i]][states[stat]]  ', t[states[i]][states[stat]])
				print ('e[states[stat]][seq[j]]     ', e[states[stat]][seq[j]]) 	
			B [i][j] = score
	 

# Terminazione 
	score = 0.0
	for stat in range(1,r-1):

		score += B [stat][1]*t['B'][states[stat]]*e[states[stat]][seq[0]] 
	B [0][0] = score

	return B
############

M = None 
M = backward(seq,states,t,e)

prettyMatrix(M) 
print(seq)
print('\nP(s|M) =', M[0][0])


