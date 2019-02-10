# HMM
# 'y' is the state: GpC Island
# 'n' is the state: Non-GpC Island


def prettyMatrix(m):
	for y in range(0,len(m)):
		print (m[y])

# function to calculate F(i+1)
def next_y(from_yes,from_no,char_seq):
	
	next = from_yes*transit_prob['y']['y']*emis_prob['y'][str(char_seq)]+from_no*transit_prob['n']['y']*emis_prob['y'][str(char_seq)]
	
	return next

def next_n(from_yes,from_no,c):
	next = from_no*transit_prob['n']['n']*emis_prob['n'][str(c)]+from_yes*transit_prob['y']['n']*emis_prob['n'][str(c)]

	return next


beginning_prob ={'y':0.2,'n':0.8}
transit_prob ={'y':{'y':0.7,'n':0.2,'e':0.1},'n':{'y':0.1,'n':0.8,'e':0.1}} 
emis_prob ={'y':{'A':0.1,'C':0.4,'G':0.4,'T':0.1},'n':{'A':0.25,'C':0.25,'G':0.25,'T':0.25}}

seq = 'ATGC'
c = len(seq) +2

# Initialization
matrix = [[0 for col in range(c)]for row in range(4)] 
matrix[0][0] = 1

seq_pos = 0

#first step 
matrix[1][1] = beginning_prob['y']*matrix[0][0]*emis_prob['y'][str(seq[0])]
matrix[2][1] = beginning_prob['n']*matrix[0][0]*emis_prob['n'][str(seq[0])]


#print(c,c-1)

#Iteration
for i in range (2,c-1):
	seq_pos += 1
	
#	print (i)
	for j in range(1,3):
#		print(j)

		if j==1:
			matrix[j][i] = next_y(matrix[j][i-1],matrix[j+1][i-1],seq[seq_pos])  	  


		else:
			matrix[j][i] = next_n(matrix[j-1][i-1],matrix[j][i-1],seq[seq_pos])


#Termination
matrix[3][c-1] = matrix[j-1][i]+matrix[j][i]
prettyMatrix(matrix)
print (matrix[3][c-1])
