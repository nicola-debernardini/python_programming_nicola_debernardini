#################################
## dummy transition probabilities
## MEMO: to ... from ...
t = {   "B": {"B":0.0, "Y":0.0, "N":0.0,  "E":0.0}, \
        "Y": {"B":0.2, "Y":0.7, "N":0.2,  "E":0.0}, \
        "N": {"B":0.8, "Y":0.1, "N":0.8,  "E":0.0}, \
        "E": {"B":0.0, "Y":0.1, "N":0.1,  "E":0.0},
        }

#print("dictionary t, key Y is: "t["Y"])

###############################
## dummy emission probabilities
e = {   "Y": {"A":0.1, "C":0.4, "G":0.4, "T":0.1}, \
        "N": {"A":0.25, "C":0.25, "G":0.25, "T":0.25}}


#################
## dummy sequence
s = "AGCGTAGCATC"

#################
## list of states
## order of states is meaningful
## order of states is the same as in the viterbi matrix
states = ["B", "Y", "N", "E"]
#print(len(s))

################
#Print a matrix
def prettyMatrix(M):
    for i in range(0,len(M)):
        print(M[i])

###################
## viterbi path function
def viterbi(s, t, e, states):
    n = len(s) + 1 ## number of cols of V
    m = len(states) ## number of rows of V

    V = [[0 for col in range(n + 1)] for row in range(m)] #matrix to calculate all the scores 

    Viterbi = [['0' for col in range(n)] for row in range(1, m - 1)] #matrix to store the possible viterbi path 
    
    ## Initialization
    V[0][0] = 1.0

    ## Iteration
    for j in range(1, n): # parsing of the colum 

        for i in range(1, m -1): # parsing or the row 

            scores = [] # empty list to store the scores comming from the different states

            #Initialization of the first colum
            if j == 1:
                V[i][1] = t[states[i]]['B']*e[states[i]][s[j - 1]] 
                Viterbi[i-1][j-1] = 'B'
                #states = ["B", "Y", "N", "E"]

            else:
            ## for each cell i,j of the matrix V
            ## I need to iterate on the previous states
            ## retrieving the score of i-1,*state*:
                for state in range(1,len(states)-1):  # range: 1 and 2
                    score = V[state][j-1] * t[states[state]][states[i]] 
#                    print ('Parti da %s score in the previous cell (state-riga: %d) (colonna: %d) (value %f)' %(states[state],state,j-1,V[state][j-1]))
#                   print ('transition probability %s -- %s: ' %(t[states[state]],t[states[state]][states[i]]))
#                    print ('emission probability ', e[states[i]][s[j - 1]])
                #print(states[i],states[state],round(score,2),t[states[i]][states[state]])
                    scores.append(score)
             
                print (scores,'\n\n')                
                max_score,max_state = find_max(scores,states)
                V[i][j] = max_score*e[states[i]][s[j - 1]] 
#                print (V[i][j])

                Viterbi[i-1][j-1] = states[max_state] 
  

  ##################
    # Termination:
    best_path = float('-inf')
    path_num = None 
    last_score = []
    for top in range(1, m-1):
        score = V[top][j]*t['E'][states[top]] 
        last_score.append(score)

    for which in range(m-2):
        if last_score [which] > best_path:
            best_path = last_score[which]
            path_num = which 
   
    V[m-1][n] = max(last_score)
    Viterbi[path_num][j] = states[path_num+1]          

    return(V,Viterbi,path_num)

#################

def find_max(score,states):
    max_score = 0
    for i in range(0,len(score)):
        if score[i] > max_score:
            max_score = score[i]
            max_state = i+1
    return max_score,max_state 

    ## use index i to retrieve max_score and max_state
    ## the order in scores and states is consistent

M,vit,path_number = viterbi(s, t, e, states)



print('\nmatrix of the scores:')
prettyMatrix(M)

print('\nmatrix of the viterbis path for each states:')
prettyMatrix(vit)

final_vit =''.join(vit[path_number])
print ('\nThe viterbi path of the sequence %s is:' %s, final_vit)



