

# Pretty matrix
def prettymatrix (M):
    for i in range(len(M)):
        print (M[i])

# Brutal matrix
def brutalMatrix(c,r):
	m = []
	for x in range(0,r):
		m.append([])
		for y in range(0,c):
			m[x].append(0)
	return m
    
# Initialize a function
def matrix(ncol,nrow,typ):
    if typ==int:
        m = [[0 for col in range(ncol)]for row in range(nrow)]
    else:
        m = [['0' for col in range(ncol)]for row in range(nrow)]
    return m 