
def fibb(n):
    """Lists the Fibonacci sequence up to n, and prints the sum"""
    l=[1];
    
    if(n!=1):
        l.append(1);
    
    if(n>2):     
        i=1
        while(i < n-1):
            l.append(l[i-1]+l[i]);
            i+=1;

    print("Fibonacci Sequence: ",end="");
    for i in range(len(l)-1):
        print(l[i],end=",");
    print(l[-1]);
    print("Sum of the first {} Fibonacci numbers = {}".format(n,sum(l)));