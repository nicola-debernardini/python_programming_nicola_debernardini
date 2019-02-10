# HMM - backword 

############
# Print a matrix:
def prettyMatrix (M):
	for i in range(len(M)):
		print(M[i])

############
# Data
t = {
	'B':{'Y':0.2,'N':0.8}, \
	'Y':{'Y':0.7,'N':0.2,'E':0.1}, \
	'N':{'Y':0.1,'N':0.8,'E':0.1} \
    }

e = {
	'Y':{'A':0.1,'C':0.4,'G':0.4,'T':0.1}, \
	'N':{'A':0.25,'C':0.25,'G':0.25,'T':0.25} \
    }

seq = 'ATCG'

states = ['B','Y','N','E']


############
def backward(s,states,t,e):
	
	c = len(s)+2 #numero colonne 
	r = len(states) #numero righe 

	# Define a matrix:
	B = [[0.0 for i in range(c)] for j in range(r)]
	
# Inizializazione 
	B [r-1][c-1] = 1
	for i in range(1,r-1):
		B [i][len(s)] = B [r-1][c-1]*t[states[i]]['E']
	
# Iteration
	for j in range(len(s)-1,0,-1):

		
		for i in range(1,r-1):
			score = 0
				
			for stat in range(1,r-1):
				score += B [stat][j+1]*t[states[i]][states[stat]]*e[states[stat]][seq[j]]
			B [i][j] = score 		 

# Terminazione 
	score = 0.0
	for stat in range(1,r-1):

		score += B [stat][1]*t['B'][states[stat]]*e[states[stat]][seq[0]] 
	B [0][0] = score

	return B

#############################
# HMM - forward

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
for cycle in range(2): #Number or iteration to generate the best parameters
	
	For = None 
	For = forward(seq,states,t,e)
	prettyMatrix(For) 

	print('\n\n')

	Back = None 
	Back = backward(seq,states,t,e)
	prettyMatrix(Back) 

#print('\n\nLa probabilità è calcolata per la seguente sequenza: ',seq) 
#print('P(s|M) =', Back[0][0])
#print('P(s|M) =', For[len(states)-1][len(seq)+1])

######################

#Baum-Welch

	char = ['A','C','G','T']
	c = len(seq)+2 #numero colonne 
	r = len(states) #numero righe 
	P_seq = Back[0][0]




	# A(kl) and E(kl):
	A_kl = {
		'B':{'Y':0.0,'N':0.0}, \
		'Y':{'Y':0.0,'N':0.0,'E':0.0}, \
		'N':{'Y':0.0,'N':0.0,'E':0.0} \
		}

	E_kc = {
		'Y':{'A':0.0,'C':0.0,'G':0.0,'T':0.0}, \
		'N':{'A':0.0,'C':0.0,'G':0.0,'T':0.0} \
		}



	# A_ki and E_kd:

	A_ki = {
		'B':0.0, \
		'Y':0.0, \
		'N':0.0 \
		}

	E_kd = {
		'Y':0.0, \
		'N':0.0 \
		}


########### Computations ############
# A(kl) and E(kl) ### A_ki and E_kd:

	for j in range(1,c-1):
		for i in range(1,r-1):

			E_kc [states[i]][seq[j-1]] = E_kc [states[i]][seq[j-1]] +  (For[i][j]*Back[i][j]/P_seq)
#			print('Forward  backward  Ekc',For[i][j],Back[i][j], E_kc [states[i]][seq[j-1]], [seq[j-1]])
			for character in range(len(char)):
				E_kd [states[i]] = E_kd [states[i]] + E_kc [states[i]][char[character]]

#			print ('A_kl::: ',A_kl [states[i]])
			
			if j == c-2:
				continue
			for stat in range(1,r-1):
				A_kl [states[i]][states[stat]] = A_kl [states[i]][states[stat]] + ((For[i][j]*Back[stat][j+1]*t[states[i]][states[stat]]*e[states[stat]][seq[j]])/P_seq)
				A_ki [states[i]] = A_ki [states[i]] + A_kl [states[i]][states[stat]]
			
			
# A(Bl) 
	for stat in range(1,r-1): 
		A_kl ['B'][states[stat]] = ((For[0][0]*Back[stat][1]*t[states[0]][states[stat]]*e[states[stat]][seq[0]])/P_seq)

# A(lE)
	for stat in range(1,r-1): 
		A_kl [states[stat]]['E'] = ((For[stat][c-2]*Back[r-1][c-1]*t[states[stat]]['E'])/P_seq) 

# A_Bi
	for stat in range(1,r-1): 
		A_ki ['B'] = A_ki ['B'] + A_kl ['B'][states[stat]]

#	print('\n A_kl\n',A_kl)
	print('\n E_kc\n',E_kc)
#	print('\n A_ki\n',A_ki)
	print('\n E_kd\n',E_kd)


#################
# New: t and e

	for i in range(1,r-1):
		for stat in range(1,r):
			t [states[i]][states[stat]] = A_kl [states[i]][states[stat]]/A_ki[states[i]]
			e [states[i]][char[stat]] = E_kc [states[i]][char[stat]]/E_kd [states[i]]	

# t: B to l
	for i in range(1,r-1):
		t['B'][states[i]] = A_kl ['B'][states[i]]/A_ki['B']

	print('\n New_t %d:\n' %cycle, t)
	print('\n New_e %d:\n' %cycle, e)







