seq1 ='AGACTAGCATGCTAGCATGCGATCGTATGCATG'
seq2 = 'GGAGAGTTACACTATTCTATCT'
gap = -1
Score_dict = {'A':{'A':1,'T':0.5,'C':-1,'G':-1}, \
              'T':{'A':0.5,'T':1,'C':-1,'G':-1}, \
              'C':{'A':-1,'T':-1,'C':1,'G':0.5}, \
              'G':{'A':-1,'T':-1,'C':0.5,'G':1} \
            }

keys = ['A','T','C','G']

def prettymatrix (M):
    for i in range(len(M)):
        print (M[i])

########
# generate a matrix
def matrix(ncol,nrow,typ):
    if typ==int:
        m = [[0 for col in range(ncol)]for row in range(nrow)]
    else:
        m = [['0' for col in range(ncol)]for row in range(nrow)]
    return m 

###############################################################
# NW
def NW(seq1,seq2,keys,gap,Score_dict):
    ncol = len(seq1)+1
    nrow = len(seq2)+1
    m_sco = matrix (ncol,nrow,type(0))
    m_tr = matrix(ncol,nrow,type('0'))

    directions = ['D','L','U']

###############################
# fill the matricies:

    for c in range (1,ncol):
        for r in range(1,nrow):
            scores = []
            s = m_sco [r-1][c-1] + Score_dict[seq1[c-1]][seq2[r-1]]
            scores.append(s)

            s = m_sco [r][c-1] +gap
            scores.append(s)

            s = m_sco[r-1][c] +gap
            scores.append(s)

            max_v = float('-inf')
            DIR = ''

            for i in range (len(scores)):
                if scores[i] > max_v:
                    max_v = scores[i]
                    DIR = directions[i]
            
            m_sco [r][c] = max_v
            m_tr [r][c] = DIR
    prettymatrix(m_sco)
    prettymatrix(m_tr)

##################
# Determine the best score and its position
    best_s = float('-inf')
    best_pos = (0,0)

    for i in range (1,ncol): # look in the last row
        if m_sco [nrow-1][i] >= best_s:
            best_s = m_sco [nrow-1][i]
            best_pos = (nrow-1,i)
        
    for j in range (1,nrow): # look in the last column 
        if m_sco [j][ncol-1] >= best_s:
            best_s = m_sco [j][ncol-1]
            best_pos = (j,ncol-1)

####################
# traceback
    x_row = best_pos [0]
    y_col = best_pos [1]
    al1 = ''
    al2 = ''
    is_match = ''

    dif_r = nrow-1-x_row
    dif_c = ncol-1-y_col

# First step
    if x_row == nrow-1:
        al1 += seq1[ncol-1:y_col-1:-1] #PERCHE
        al2 += '-'*dif_c
    
    elif y_col == ncol-1:
        al1 += '-'*dif_r
        al2 += seq2[nrow-1:x_row-1:-1] #PERCHE
    #print ('\n'+al1+'\n'+al2)    
    #print (x_row,y_col)

# Through the matrix
    while x_row != 0 and y_col != 0:
        if m_tr [x_row][y_col] == 'D':
            al1 += seq1[y_col-1]
            al2 += seq2[x_row-1]
            x_row -=1
            y_col -= 1

        elif m_tr [x_row][y_col] == 'L':
            al1 += seq1[y_col-1]
            al2 += '-'
            y_col -= 1
        
        else:
            al2 += seq2[x_row-1]
            al1 += '-'
            x_row -= 1  

    #print ('These are the lign: \n'+al1+'\n'+al2)

# last step
    if x_row == 0 and y_col != 0:
        al1 += seq1[0:y_col-1]
        al2 += '-'*y_col

    
    elif y_col == 0 and x_row != 0:
        al2 += seq2[0:x_row-1]   
        al1 += '-'*x_row

    al1 = al1[::-1]
    al2 = al2[::-1]

    return al1,al2
######################## THE END ############

alignment1, alignment2 = NW(seq1,seq2,keys,gap,Score_dict)
print ('\nThe original sequences are:\n%s\n%s' %(seq1,seq2))


print ('\n\nAlignment is: ',alignment1)
print ('              ',alignment2)