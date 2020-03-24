###Implementation of Dynamic Programming Algorithm

def DP_align_matrix(x,y):
    '''Function that receives as input 2 sequence strings x and y with
    sizes m and n, respectively, and generate two matrixes of dimensions 
    (m+1)x(n+1). The matrix M computes the similarity score between 
    each possible pair of prefixes of the 2 strings, and the matrix D 
    saves the arrows which indicate the optimal alignment for an 
    entry [i,j]
    
    Input:
    - x and y: strings
    
    Output:
    - M: matrix with similarity scores for pair x[0:i] and y[0:j] at entry
    [i,j]
    - D: matrix with arrow for pair x[0:i] and y[0:j] at entry
    [i,j] (either 'N','W' or 'NW')
    
    '''
    #get the length of each string 
    m = len(x)
    n = len(y)
    
    #Redefining x and y with a space as the first character
    x = '-' + x
    y = '-'+ y
    
    #Create empty matrixes of dimensions (m+1)x(n+1). 
    M = [[0 for i in range(n+1)] for i in range(m+1)]
    D = [['' for i in range(n+1)] for i in range(m+1)]
    
    #Fill position [0,0]
    M[0][0] = 0
    D[0][0] = None # no arrow at position [0,0]
    
    #Start by filling out the first row and column of matrix M
    for i in range(1, m+1): #filling first column starting from 1
        #because position 0,0 has been filled
        M[i][0] = i*(-2) #value will be the number of nonempty
        #spaces multipled by -2(score for a space)
        D[i][0] = 'N' #for first column, only possible direction
        #is up
    
    #filling first row
    for j in range(1,n+1):#starting from 1 because 0 has been filled
        M[0][j] = j*(-2) #value will be the number of nonempty
        #spaces multipled by -2(score for a space)
        D[0][j] = 'W' #for first row, only possible direction if left
    
    
    #filling matrices row by row from left to right. 
    for i in range(1,m+1):
        for j in range(1,n+1):
            #calculate p(i,j)
            if x[i] == y[j]: #if characters match
                p = 1
            elif x[i] != y[j]: #if characters don't match
                p = -1
            else:
                raise 'Error'
            #Entry [i,j] will be the max value of the 3 possible
            #scenarios. The max function in python deals with ties
            #by returning the first maximal value it finds, so we use
            #the same logic to fill in the matrix D
            
            options = ['','','']
            options[0] = M[i-1][j] - 2 #vertical option ('N')
            options[1] = M[i-1][j-1] + p #diagonal option('NW')
            options[2] = M[i][j-1] - 2 #horizontal option ('W')
            
            #Replicate the max function for the 3 elements
            max_v = 0 #variable that takes the value of 0,1 or 2
            #indicating the indice of the maximal candidate
            if options[1] > options[max_v]:
                max_v = 1
            if options[2] > options[max_v]:
                max_v = 2         
            
            #Fill entry [i,j] of matrix M with the largest value
            M[i][j] = options[max_v]
            
            #Check which one of the 3 candidates was the max to fill
            #entry [i,j] of the matrix D
            if max_v == 0:
                D[i][j] = 'N'
            elif max_v == 1:
                D[i][j] = 'NW'
            elif max_v == 2:
                D[i][j] = 'W'
            else:
                raise 'Error'
    return M,D #outputs the matrices

def DP_generate_alignment(D, x, y):
    '''Function that receives as input the matrix D with the directions
    to generate the optimal alignment and uses it to outputs 2 strings
    with '-' to represent the positions which spaces were inserted arbitrarily
    and that generate the optimal alignment between the 2 sequences x and y
    
    Inputs:
    -D: matrix with 'N', 'NW' or 'W' to represent that arrows pointing
    at the previous maximal value -> subproblem which is combined with
    the solution of other subproblems to generate the optimal alignment
    -x and y: sequence strings
    
    Outputs:
    -x_aligned and y_aligned: strings of same size which when positioned
    one over the other generate the optimal alignment between x and y
    '''
    
    #Starting indices at the position mxn of the matrix
    i = len(x) 
    j = len(y) 
    
    #Redefining x and y with a space as the first character
    x = '-' + x
    y = '-'+ y
    
    #Initialize output
    x_aligned = ''
    y_aligned = ''
    
    #Follow the arrows until reaching the position [0,0] 
    while (i,j) != (0,0):
        if D[i][j] == 'NW': #if the arrow is the diagonal, 
            #the comparison will be x[i] to y[j], so add
            #these characters to the output and update the indices
            x_aligned = x[i] + x_aligned 
            y_aligned = y[j] + y_aligned 
            i -= 1
            j -= 1
        elif D[i][j] == 'N': #For the vertical, will match x[i] 
            #with a space represented by '-'
            x_aligned = x[i] + x_aligned 
            y_aligned = '-' + y_aligned
            i -= 1
        elif D[i][j] == 'W': #For the horizontal line, will match
            #y[j] with a space represented by '-'
            x_aligned = '-' + x_aligned  
            y_aligned = y[j] + y_aligned 
            j -= 1
        else:
            raise 'Error'    
    return x_aligned, y_aligned    
    
#Testing the function   
x, y = 'AAAC', 'AGC' # defining 2 strings
M, D = DP_align_matrix(x,y) #generating the matrices
P, Q = DP_generate_alignment(D,x,y) #saving and printing out 
#the optimal alignment
print(P)
print(Q)
#print the similarity score of the selected alignment
print(M[len(x)][len(y)])
