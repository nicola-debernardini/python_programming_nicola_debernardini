'''
VITERBI ALGORITHM

-------------------------------------------------
Input:
The VITERBI algorithm take in input a sequence and the parameters that the scribe a hidden markov model. The markovian models are probabilistic models 
able to generate sequences with different probability, and they are decribed by transition porbabilities between states ex. k to l (akl), and emissions porbabilities 
of a character (c) from a state k (ekc). Each sequence is the results of two stochastic processes:
- the generation of a path as a sequence of states 
- generation of a sequence of characters for eache state 
and the results is strictly related to the parameters that describe the models.

Algorithm at work:
The Viterbi algorithm uses a dynamic programming approach and it is able to calculate which is the path that maximize the probability of the path given the
 sequence and the model -> P(path*|s,M) 
Thus, it selects step by step the path that has the higher probability to generate the sequence given the model -> P(path,s|M)

In particular during the computation the program implement the follwing formula:
Vk(i+1) = ek(i+1) * MAX [ Vl(i) * alk ]

Output:
The output is the viterbi path of the sequence

--------------------------------------------------

PSEUDOCODE 

- Define a function (prettymatrix) to print matrix in a nice way:
	- Fro i that iterates through the length of the matrix:
		- print every line of the matrix 

- Define a function (matrix) to generate a matrix of dimensions (n_col, n_row, type):
    - if the type is interger fill in the matrix with 0:
    	- generate a matrix using two for cycle = [[0 for col in range(c_col)]for r in range(n_row)] 
	- else: # fill in the matrix with '0':
        - generate a matrix using two for cycle = [['0' for col in range(c_col)]for r in range(n_row)] 
    return the matrix m

- Define the viterbi function (seq,t,e,states):
	- ncol = calculate the number of columns as the length of character of the sequence plus 2 
	- nrow = calculate the number of row as the number of states of the model (length of the states list)
	- generate a matrix m using the function matrix (ncol, nrow, type (0))
    - generate a matrix m_vit using the function matrix (ncol, nrow, type ('0'))

	# Initialize the matrices writing:
	- m [0][0] = 1 
    - for r that iterates through the row of the first column of the m_vit matrix:
        - m_vit [r][0] = 'B'

	# Start filling in the matrix 
	# second column:
	- For cycle that iterates through the rows (except the first and the last):
		- Write in every cell the product of the transition probability from the 'B' state to the 'k' state and the emission prob of the first character of the sequence from the state 'k'
		m [r][1] = states['B'][states[r]]*e[states[r]][seq[0]]

	# Iteration:
	# Three nested for cycle to fill in the matrix implemnting the formula: Vk(i+1) = ek(i+1) * MAX [ Vl(i) * alk ]
	- For cycle that iterates through the columns (except the first two and the last one): # it is important that the iteration occours through the columns while it is occuring also through the rows 
		- For cycle that iterates through the rows (except the first and the last):
            - Initialize an empty list where to store the score [ Vl(i) * alk ]
			-For cycle that iterates through the states (except the 'B' an the 'E' states):
				- scor = m[r][c-1] * t[states[stat]][states[r]] 
                - append scor to the list scores 

            # Find the max in the list and save the state that generates it: 
            - Initialize a variable max_score
            - Initialize a variable which_state
            - For i that iterates through the scores lists:
                - If the score in position i of the list (scores[i]) is higher than max_score:
                - max_score = scores[i]
                - which_state = i+1 # save the position of the max in the list plus one 
			- m [r][c] =  max_score * e[states[r]][seq[c-1]] # In order to reduce the number of calculations is possible to multiply the emissions probability only at the end of the previous counts
            - m_vit [r-1][c-1] = states[which_state] # store the state that most likely generates the character 

	# Termination:
	# Determine which of the path ending in the state 'k' is the viterbi path by multipying the Vk(i) by the transition probability from 'k' to the 'E' state 
	- For cycle through the second last column (except the first and the last rows):
		-If m[r][ncol-2] * t[states[r]]['E'] is > m [nrow][ncol]: 
            - m [nrow-1][ncol-1] = m[r][ncol-2] * t[states[r]]['E'] # store the higher alue in the last cell (bottom, right)
            - Save the state in Which_state = r
    - m_vit [r-1][ncol-2] = states[r]
    - for r that iterates trough the last columns (except the first and the last rows):
        - m_vit [r-1][ncol-1] = 'T'  # write in every cell of the m_vit matrix 'T'
    - Initialize a variable (Viterbi_path) = ''
    - Viterbi_path = join the list of the viterbi path (''.join(m_vit [r-1]))
	- Return Viterbi_path

# define the main of the script
if __name__ =='__main__':
	- Initialize a variable (seq) containing the sequence 
	- Initialize a dictionary (t) containing the transition probability  
	- Initialize a dictionary (e) containing the emission probability 
	- Initialize a list containing the states of the model (B,Y,N,E)	
	- P_s = Call the function: viterbi (seq,t,e,states)
	- Print the sequence and the viterbi path

----------------------------------------------------
'''
# matrix
def matrix (row, col,t):
    if t == int:
        m = [[0 for c in range (col)]for r in range (row)]
    else:
        m = [['0' for c in range (col)]for r in range (row)]
    return m

# pretty matrix
def prettymatrix (M):
    for i in range(len(M)):
        print(M[i])

## Viterbi ##
def viterbi (seq, t, e, states):
    c = len(seq)+2
    r = len(states)

    m_scores = matrix (r,c,type(1))
    m_vit = matrix (r-2,c,type('a'))

# Initialization
    m_scores [0][0] = 1
        
    for row in range (1,r-1):
        m_vit [row-1][0] ='B'
        m_scores [row][1] = t['B'][states[row]]*e[states[row]][seq[0]]

# Iteration
    for col in range(2,c-1):
        for row in range (1,r-1):
            scores =[]
            score = 0
            for stat in range (1,r-1):
                score = m_scores[stat][col-1]*t[states[stat]][states[row]]
                scores.append(score)

            max_scores = float('-inf')
            max_state = 0

            for i in range(len(scores)):
                if (scores[i]) > max_scores:
                    max_scores = scores[i]
                    max_state = i

            m_scores[row][col] = max_scores
            m_vit [row-1][col-1] = states[max_state+1]

    score = float('-inf')
    for row in range(1,r-1):
        if m_scores[row][c-2]*t[states[row]]['E'] > score:
            score = m_scores[row][c-2]*t[states[row]]['E']
            max_state = row -1

    m_vit[max_state][c-2] = states [max_state+1]

    m_scores[r-1][c-1]= score
    m_vit [max_state][c-1] = 'T'

    prettymatrix(m_scores)
    prettymatrix(m_vit)

    path = ''
    path = ''.join(m_vit [max_state])

#   for i in range(c):
#        path += m_vit[max_state][i]
  
    return path


if __name__=='__main__':
    seq = 'AGCGTAGCATC'
    t = {
	    'B':{'Y':0.2,'N':0.8}, \
	    'Y':{'Y':0.7,'N':0.2,'E':0.1}, \
	    'N':{'Y':0.1,'N':0.8,'E':0.1} \
        }

    e = {
	    'Y':{'A':0.1,'C':0.4,'G':0.4,'T':0.1}, \
	    'N':{'A':0.25,'C':0.25,'G':0.25,'T':0.25} \
        }
    
    states = ['B','Y','N','E']
    vit = viterbi(seq,t,e,states)
    print(' '+seq+' '+'\n'+vit)