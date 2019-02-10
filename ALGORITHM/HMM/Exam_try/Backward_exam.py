def matrix (num_col,num_row):
    matr = [[0 for col in range(num_col)]for row in range (num_row)]
    return matr

def prettymatrix (M):
    for i in range(len(M)):
        print (M[i])


def backward (seq,t,e,states):
    n_col =len(seq)+2
    n_row = len(states)
    m = matrix(n_col,n_row)
    m[n_row-1][n_col-1] = 1

    for r in range(1,n_row-1):
        m[r][n_col-2]= t[states[r]]['E']

    for c in range (n_col-3,0,-1):
        for r in range (1,n_row-1):
            
            for stat in range(1,n_row-1):
                
                m[r][c] += m[stat][c+1]*t[states[r]][states[stat]]*e[states[stat]][seq[c]]
                print ('m[r][c]                    ', m[r][c])
                print ('m[stat][c+1]               ', m[stat][c+1])
                print ('t[states[stat]][states[r]] ', t[states[stat]][states[r]])
                print ('e[states[stat]][seq[c]]    ', e[states[stat]][seq[c]])

    
    for r in range(1,n_row-1):

        m[0][0] += m[r][1]*t['B'][states[r]]*e[states[r]][seq[0]]
    prob_s = m[0][0]
    prettymatrix(m)
    return prob_s

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
