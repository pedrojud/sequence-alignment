def similarity_score(x,y):
    '''Function that receives as input 2 strings x and y
    of same length representing an alignment and calculates
    the similarity score of the alignment and outputs the score
    
    Input:
    -x,y: strings of same length
    
    Output:
    -sim_score: int indicating similarity score of alignment
    
    '''
    #Raise error if strings don't have the same size
    if len(x) != len(y):
        raise 'Error: Not Applicable Alignment'
    
    #Initialize the length of the strings
    n = len(x)
    
    #Intialize variable to save the total similarity score
    sim_score = 0
    
    #Create for loop to check every position
    for i in range(n):
        if x[i] == y[i]: #same character: +1
            sim_score += 1
        else: #characters are different
            if x[i] == '-' or y[i] == '-':
                #if space in one of the strings: -2
                sim_score -= 2
            else: #different characters but no spaces: -1
                sim_score -= 1
    
    #output the score after checking all columns
    return sim_score


def BF_alignment (x, y): 
    '''Function that receives 2 strings and implements a brute-force
    algorithm to generate all possible alignments recursively and 
    find the one with the highest similarity score.
    
    Inputs:
    -x,y: sequence strings to be aligned
    
    Output:
    -2 strings of same size representing an optimal alignment
    
    '''
    
    if len(x) == 0 or len(y) == 0: # if either string is empty
        #complete it with spaces until it reaches the length of
        #the second. This will be the base case of the optimal
        #alignment, since the optimal alignment between an empty
        #string and another string is the as many spaces as the 
        #second string's length 
        while len(x) < len(y): 
            x = x + '-' #add spaces until size of x is not smaller 
            #than y
        while len(y) < len(x): #add spaces until size of y is not
            #smaller than x
            y = y + '-'
        return x, y #return both strings
    else:#recursion is still occurring
        # try with no space
        (x0, y0) = BF_alignment(x[1:],y[1:])#recursively call function
        #for next characters
        score_no_space = similarity_score(x0, y0) # get the score of the rest
        
        #if first characters are the same add 1
        if x[0] == y[0]: 
            score_no_space += 1
        else: #if different then subtract 1
            score_no_space -= 1 
        
        # try inserting a space in x (no match for y[0])
        (x1, y1) = BF_alignment(x, y[1:])
        score_space_x = similarity_score(x1, y1) - 2
        
        # try inserting a space in y (no match for x[0])
        (x2, y2) = BF_alignment(x[1:], y) #recursively call function
        score_space_y = similarity_score(x2, y2) - 2 #calculate similarity score
        
        #Comparing the 3 options and seeing which one has the largest score
        if score_no_space >= score_space_x and score_no_space >= score_space_y:
            return x[0] + x0, y[0] + y0 #no space was best option, so return the 
        #first characters concatenated with x0, which is found by recursively calling
        #the function, which will ultimately test all other possible space insertions
        elif score_space_x >= score_space_y: #when inserting a space in x gives the largest 
            #possible score, then add space to x1 and return y1
            return '-' + x1, y[0] + y1
        else: #final option: if the largest score is when adding a space to y
            return x[0] + x2, '-' + y2


#Testing the function with same strings  
x, y = 'AAAC', 'AGC' # defining 2 strings

P, Q = BF_alignment(x,y) #saving and printing out 
#the optimal alignment
print(P)
print(Q)
#print the similarity score of the selected alignment
print(similarity_score(P,Q))
