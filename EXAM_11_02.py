# Pretty matrix
def prettymatrix (M):
    for i in range(len(M)):
        print (M[i])

# Initialize a matrix
def matrix(ncol,nrow,typ):
    if typ==int:
        m = [[0 for col in range(ncol)]for row in range(nrow)]
    else:
        m = [['0' for col in range(ncol)]for row in range(nrow)]
    return m 

#################
# Smith Waterman function 
def SW (seq1,seq2, gap ,sub_matrix):
    n_col = len(seq1)+1
    n_row = len(seq2)+1

    # generate the score and the trace back matrix 
    m_sco = matrix( n_col,n_row,type(1))
    m_t = matrix (n_col,n_row,type('0'))

    best_s = float('-inf')
    best_p = (0,0)
    direction = ['0','D','L','U']
    
    # Iterations
    for c in range(1,n_col):
        for r in range(1,n_row):
            
            scores = [0]
            score = float('-inf')
            
            # diag score
            score = m_sco[r-1][c-1]+ sub_matrix[seq1[c-1]][seq2[r-1]]
            scores.append(score)

            # left score
            score = m_sco[r][c-1]+gap    
            scores.append(score)

            # up score
            score = m_sco[r-1][c]+gap
            scores.append(score)

            # determine the higher score 
            DIR = '' 
            max_score = float('-inf')
            for i in range (len(scores)):
                if scores[i] > max_score:
                    max_score = scores[i]
                    DIR = direction[i]
            
            m_sco[r][c] = max_score # fill in the score matrix
            m_t[r][c] = DIR # fill in the traceback matrix

            # determine the best score
            if max_score >= best_s:
                best_s = max_score
                best_p = (r,c)
    
    # Traceback
    al1 = ''
    al2 = ''
    
    x_row = best_p[0]
    y_col = best_p[1]

    while m_t[x_row][y_col] != '0': # Until the value in the cell of the traceback is different from '0'
        if m_t[x_row][y_col] == 'D':
            al1 += seq1[y_col-1]
            al2 += seq2[x_row-1]
            y_col -=1
            x_row -=1

        elif m_t[x_row][y_col] == 'L':
            al1 += seq1[y_col-1]
            al2 += '-'
            y_col -= 1

        else:
            al1 += '-'
            al2 += seq2 [x_row-1] 
            x_row -= 1

    al1 = al1 [::-1]
    al2 = al2 [::-1]

    #print (al1)
    #print (al2)
    return (m_sco,m_t,best_p)


if __name__=='__main__':

    import sys  
    try:
        seq1 = sys.argv[1]
        seq2 = sys.argv[2]
    except:
        print('Program usage: python S_W.py <Seq1> <Seq2>')
        raise SystemExit
    
    else:    
        Score_dict = {'A':{'A':1,'T':0.5,'C':-1,'G':-1}, \
                    'T':{'A':0.5,'T':1,'C':-1,'G':-1}, \
                    'C':{'A':-1,'T':-1,'C':1,'G':0.5}, \
                    'G':{'A':-1,'T':-1,'C':0.5,'G':1} \
                    }
        gap = -1
        best_pos = None
        m_score, m_trace, best_pos = SW(seq1, seq2, gap, Score_dict)

        print('\nThe matrix containing the scores is:')
        prettymatrix(m_score)
        print('\nThe traceback matrix is:')    
        prettymatrix(m_trace)    
        print('\nThe coordinates of the cell containing the best score are: row(%d) column(%d)\n' %(best_pos[0],best_pos[1]))


