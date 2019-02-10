def matrix (row, col,t):
    if t == int:
        m = [[0 for c in range (col)]for r in range (row)]
    else:
        m = [['0' for c in range (col)]for r in range (row)]
    return m

def prettymatrix (M):
    for i in range(len(M)):
        print(M[i])

def viterbi (seq, t, e, states):
    c = len(seq)+2
    r = len(states)

    m_scores = matrix (r,c,type(1))
    m_vit = matrix (r-2,c,type('a'))



    m_scores [0][0] = 1
    for row in range (r-2):
        m_vit [row][0] ='B'
    for row in range (1,r-1):
        m_scores [row][1] = t['B'][states[row]]*e[states[row]][seq[0]]
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
    print(states [max_state+1])

    m_scores[r-1][c-1]= score
    m_vit [max_state][c-1] = 'T'

    prettymatrix(m_scores)
    prettymatrix(m_vit)
    
    path = ''
    for i in range(c):
        path += m_vit[max_state][i]
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