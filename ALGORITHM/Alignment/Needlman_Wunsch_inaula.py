seqA = 'ACGTATGAAT'
seqB = 'CGTCTGA'

c = len(seqA)+1
r = len(seqB)+1

match = 1
mismatch = -1 
gap = -2

matrix=[]
for row in range(r):
	matrix.append([])
	for col in range(c):
		matrix[row].append([0]) 

print(matrix)


