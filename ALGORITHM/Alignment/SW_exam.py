def matrix(ncol,nrow,typ):
    if typ==int:
        m = [[0 for col in range(ncol)]for row in range(nrow)]
    else:
        m = [['0' for col in range(ncol)]for row in range(nrow)]

    return m 

def prettymatrix (M):
    for i in range(len(M)):
        print (M[i])

def SW(s1,s2,match,gap,mismatch):
    n_col = len(s1)+1
    n_row = len(s2)+1
    m = matrix( n_col,n_row,type(1))
    m_t = matrix (n_col,n_row,type('0'))

    prettymatrix(m)
    prettymatrix(m_t)
    
    max_cell = float('-inf')
    max_pos = None
    direction = ['0','D','L','U']
    
    # Iterations
    for c in range(1,n_col):
        for r in range(1,n_row):
            
            scores = [0]
            sc =  0
            if s1[c-1] == s2 [r-1]:
                sc = m[r-1][c-1]+match
                scores.append(sc)
            else:
                sc = m[r-1][c-1]+mismatch
                scores.append(sc)

            sc = m[r][c-1]+gap    
            scores.append(sc)

            sc = m[r-1][c]+gap
            scores.append(sc)

            DIR = 0 
            score = 0
            for i in range (len(scores)):
                if score < scores[i]:
                    score = scores[i]
                    DIR = i
            
            m[r][c] = score 
            m_t[r][c] = direction[DIR]
            #print (scores[DIR])

            if max_cell <= score:
                max_cell = score
                max_pos = (r,c)
            
    al1 = ''
    al2 = ''
    is_match = ''
    x = max_pos[1]
    y = max_pos[0]
    print (x,y)

    while (m_t[y][x] != '0'):
        if m_t[y][x] == 'D':
            al1 += s1[x-1]
            al2 += s2[y-1]
            if s1[x-1] == s2 [y-1]:
                is_match += '|'
            else:
                is_match += ' '
            y -=1
            x -=1

        elif m_t[y][x] == 'L':
            al1 += s1[x-1]
            al2 += '-'
            is_match +=' '
            x -= 1
        else:
            al1 += '-'
            al2 += s2 [y-1] 
            is_match += ' '
            y -= 1

    al1 = al1 [::-1]
    al2 = al2 [::-1]
    is_match = is_match[::-1]
    prettymatrix(m)
    prettymatrix(m_t)

    return (al1,al2,is_match)


seq1 = 'AGCATGC'
seq2 = 'AGCACTATA'

match = 1
mismatch = -1
gap = -1
alignment1, alignment2, mat = SW(seq1,seq2,match,gap,mismatch)
print(alignment1)
print(mat)
print(alignment2)