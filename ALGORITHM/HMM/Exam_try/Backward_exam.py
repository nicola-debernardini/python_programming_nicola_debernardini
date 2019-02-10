'''
BACKWARD ALGORITHM

-------------------------------------------------
Input:
The backward algorithm take in input a sequence and the parameters that the scribe a hidden markov model. The markovian models are probabilistic models 
able to generate sequences with different probability, and they are decribed by transition porbabilities between states ex. k to l (akl), and emissions porbabilities 
of a character (c) from each state k (ekc). Each sequence is the results of two stochastic processes:
- the generation of a path as a sequence of states 
- generation of a sequence of characters for each state 
and the results is strictly related to the parameters that describe the models. 

Algorithm at work:
The backward algorithm is able to calculate the probability of the sequence (took as input) given the model -> P(s|M) by summing up the probability of each different
path to generate the sequence -> SUM P(s,path|M)
In particular during the computation the program implement the folloing formula:
Bk(i-1) = SUM [ Bl(i) * akl * el(i) ]
It is the probability of generation the last part of the sequence up to the character (i) ending in the state (k) -> P(s(i) s(i+1) ... s(T), path(i-1)=k|M)

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
  { OR:
	m = []
	for r in range(n_row):
		m.append([])
		for c in range(n_col):
			m[r].append(0)
	print (m)
  }

- Define the backward function (seq,t,e,states):
	- ncol = calculate the number of columns as the length of character of the sequence plus 2 
	- nrow = calculate the number of row as the number of states of the model (length of the states list)
	- generate a matrix m using the function matrix (ncol, nrow)

	# Initialize the matrix writing in the last cell: 1
	- m [nrow-1][ncol-1] = 1

	# Start filling in the matrix 
	# second last column:
	- For cycle that iterates through the rows:
		- Write in every cell the product of the transition probability from the 'E' state to the 'k' state
		m [r][ncol-2] = states['E'][states[r]]

	# Iteration:
	# Three nested for cycle to fill in the matrix implemnting the formula: Bk(i-1) = SUM [ Bl(i) * akl * el(i) ]
	- For cycle that iterates from the tird last column to the second column (except the first two and the last one): # it is important that the iteration occours through the columns while it is occuring also through the rows 
		- For cycle that iterates through the rows (except the first and the last):
			-For cycle that iterates through the states (except the 'B' an the 'E' states):
				- m [r][c] += m[r][c+1] * t[states[r]][states[stat]]* e[states[stat]][seq[c]]
			

	# Termination:
	# Sum the value for every states stored in the second column in the cell m[0][0]
	- For cycle through the row of the second column:
		m[0][0] += m[r][1] 
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



def prettymatrix (M):
    for i in range(len(M)):
        print (M[i])

def matrix (num_col,num_row):
    matr = [[0 for col in range(num_col)]for row in range (num_row)]
    return matr

## Backward function ##
def backward (seq,t,e,states):
    n_col =len(seq)+2
    n_row = len(states)
    m = matrix(n_col,n_row)

# Initialization
    m[n_row-1][n_col-1] = 1
    for r in range(1,n_row-1):
        m[r][n_col-2]= t[states[r]]['E']

# Iterations
    for c in range (n_col-3,0,-1):
        for r in range (1,n_row-1):
            for stat in range(1,n_row-1):
                
                m[r][c] += m[stat][c+1]*t[states[r]][states[stat]]*e[states[stat]][seq[c]] ###################################àà
                print ('m[r][c]                    ', m[r][c])
                print ('m[stat][c+1]               ', m[stat][c+1])
                print ('t[states[stat]][states[r]] ', t[states[stat]][states[r]])
                print ('e[states[stat]][seq[c]]    ', e[states[stat]][seq[c]])

# Termination     
    for r in range(1,n_row-1):

        m[0][0] += m[r][1]*t['B'][states[r]]*e[states[r]][seq[0]]
    prob_s = m[0][0]
    prettymatrix(m)
    return prob_s

############################
# Main #
if __name__=='__main__':
    seq = 'ATGC'
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
    BW = backward(seq,t,e,states)
    print ('P(%s|M): ' %seq,BW)
