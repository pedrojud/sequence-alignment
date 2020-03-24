import time
import matplotlib.pyplot as plt
import random
import string

n = 10#determine max value of input size used for simulation

ys_DP = [] #time for dynamic programming approach
ys_BF = [] #time for brute force approach
ys_G = [] #time for greedy approach
xs = list(range(1,n+1)) #create array of x values: range from 1 to n

for i in range(1,n+1): #for each value of x, create array of size x and
    #calculate the y value by calling each function and computing
    #running time for each one and averaging out over 50 times
    
    #Initialize time counter for each
    tot_DP = 0
    tot_BF = 0
    tot_G = 0
    
    #Generate 2 random strings with length i
    x = ''.join([random.choice(string.ascii_uppercase) for n in range(i)])
    y = ''.join([random.choice(string.ascii_uppercase) for n in range(i)])
    
    for j in range(50): #compute running time 50 times to average out results
        
        #Dynamic Programming
        start = time.time()
        M, D = DP_align_matrix(x,y) #generating the matrices
        DPx, DPy = DP_generate_alignment(D,x,y) #saving and printing out        
        end = time.time()
        tot_DP += (end-start)

        #Greedy Approach
        start = time.time()
        gx,gy = greedy_alignment(x,y)
        end = time.time()
        tot_G += (end-start)
    
    #I didn't average out the BF approach because even for relatively
    #small inputs(length=10) it takes too long
    start = time.time()
    BFx, BFy = BF_alignment(x,y)        
    end = time.time()
    tot_BF += (end-start)
    
    #Appending averages to lists to generate plot
    ys_DP.append(tot_DP/50)
    ys_BF.append(tot_BF)
    ys_G.append(tot_G/50)        
        
        
    

#Create plot with all 3 running times
plt.plot(xs, ys_DP)
plt.plot(xs, ys_BF)
plt.plot(xs, ys_G)

plt.xlabel('Input Size (Length of Sequences)')
plt.ylabel('Running Time(s)')
plt.title('Constrasting Running Time of Algorithms for Sequence Alignment')
plt.legend(['Dynamic Programming', 'Brute-force', 'Greedy Approach'], 
           loc='upper left')

plt.show()



#Create plot with just dynamic programming and greedy approaches

#We can now utilize largest inputs and still
#generate the graphs in reasonable time


n = 100#determine max value of input size used for simulation

ys_DP = [] #time for dynamic programming approach
ys_G = [] #time for greedy approach
xs = list(range(1,n+1)) #create array of x values: range from 1 to n

for i in range(1,n+1): #for each value of x, create array of size x and
    #calculate the y value by calling each function and computing
    #running time for each one and averaging out over 50 times
    
    #Initialize time counter for each
    tot_DP = 0
    tot_BF = 0
    tot_G = 0
    
    #Generate 2 random strings with length i
    x = ''.join([random.choice(string.ascii_uppercase) for n in range(i)])
    y = ''.join([random.choice(string.ascii_uppercase) for n in range(i)])
    
    for j in range(50): #compute running time 50 times to average out results
        
        #Dynamic Programming 
        start = time.time()
        M, D = DP_align_matrix(x,y) #generating the matrices
        DPx, DPy = DP_generate_alignment(D,x,y) #saving and printing out        
        end = time.time()
        tot_DP += (end-start)
        
        #Greedy Approach
        start = time.time()
        gx,gy = greedy_alignment(x,y)
        end = time.time()
        tot_G += (end-start)
    
    #Appending averages to lists to generate plot
    ys_DP.append(tot_DP/50)
    ys_G.append(tot_G/50)  

plt.plot(xs, ys_DP)
plt.plot(xs, ys_G)

plt.xlabel('Input Size (Length of Sequences)')
plt.ylabel('Running Time(s)')
plt.title('Constrasting Running Time of Algorithms for Sequence Alignment')
plt.legend(['Dynamic Programming','Greedy Approach'], 
           loc='upper left')

plt.show()
