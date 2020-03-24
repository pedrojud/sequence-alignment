def greedy_alignment (x,y):
    '''Function that receives as inputs 2 strings x and y with lengths
    m and n and outputs 2 strings of same length representing an alignment
    which replicates a greedy approach of always maximizing the current
    column similarity score'''
    
    #Create variables with the length of each string
    m = len(x)
    n = len(y)
    
    #If the first string is shorter, add as many spaces
    #as |m-n| to it and output the second string as it is
    if m <= n:
        return x + '-'*(m-n), y
    else:#If the second string is shorter, add as many spaces
    #as |m-n| to it and output the first string as it is
        return x, y + '-'*(m-n)
    
    

#Testing the function 
x, y = 'CAGCACTTGGATTCTCGG', 'CAGCGTGG' # defining 2 strings

#Generating alignment with greedy algorithm
gx,gy = greedy_alignment(x,y)

#printing out the alignment and its similarity score
print(gx)
print(gy)
print(similarity_score(gx,gy))


#For contrast, generating and printing out the optimal alignment
#generated using the dynamic programming approach and the similarity
#score of its output
M, D = DP_align_matrix(x,y) #generating the matrices
DPx, DPy = DP_generate_alignment(D,x,y) #saving and printing out 
print(DPx)
print(DPy)
print(similarity_score(DPx,DPy))
