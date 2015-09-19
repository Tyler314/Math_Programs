import sys

def lookAndSay(N):
    """Prints the "Look-And-Say" sequence.
    
    Parameters:
    N - Number of sequences to be printed out
    """
    m=[];
    m=[[1],[1,1]]; #Initialize the first two sequences in matrix m
    #Handle the cases where the user requests an invalid integer, or just 1 or
    #2 sequences
    if(N<1):
        print("You must enter an integer that is greater than 0.")
    elif(N==1):
        print(m[0][0])
    elif(N==2):
        print(m[0][0])
        print("".join(str(m[1][e]) for e in m[1]))
    else:
        l=[]; #initialize this list to hold an entire sequence, that will be added
              #to the collection of sequences m held in the matrix m
    
        for j in range(1,N): #Iterate through all of the sequences
            count=1; #Counts the number of integers there are in a given sequence
            n=m[j][0]; #Get first element of the array m, this is the starting
                        #point of the sequence being evaluated
            for i in range(1, len(m[j])): #Iterate through a single sequence
                if(n==m[j][i]):#The number being evaluated is the same as the previous
                    count+=1;
                else: #The number being evaluated is not the same as the previous one
                    l.append(count);
                    l.append(n); #Collect data
                    count=1; #Reset count back to 1
                    n=m[j][i]; #Reset n to be the next integer to be evaluated
                if(len(m[j])-1==i):#Checks if at end of sequence being evaluated
                                    #Boundry Condition
                    #Must check for 2 seperate circumstances of the boundry condition
                    if(m[j][-1]!=n):#If the last element is not the same as n
                        l.append(1);#There is only 1 instance of this integer in this case
                        l.append(m[j][-1]);#append that integer at the boundry
                    else:
                        #in this case, the element in the boundry case has already been
                        #taken into account, so the sequence l must be updated
                        l.append(count);
                        l.append(n);
            #END OF INNER FOR LOOP
            m.append(l); #Append the sequence l, to the collection of sequences m
            l=[]; #Reset l
        
        #Prints the collection of sequences on consecutive lines
        print(m[0][0])
        for i in range(1,len(m)):
            for j in range(len(m[i])):
                print(m[i][j], end="")
            print("")

try:
    n = int(sys.argv[1])
except:
    n = 1

lookAndSay(n)
