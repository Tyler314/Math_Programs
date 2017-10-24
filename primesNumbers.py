import numpy as np
n = 0;
isPrime = True;

while(n>=0):
    print('')
    primes = []
    n = int(input("How far along the number line do you want the prime numbers to be listed?\n"));
    if(n<0):
        break
    elif(n==0):
        print("There are no prime numbers <= 0")
        continue
    elif(n==1):
        print("1 is the only prime number <=1")
        continue
        
    for i in range(2,n+1):
        for j in range(1,len(primes)): # j used for indexing "primes" list
            if(i%primes[j]==0):
                isPrime=False
                break
            
        if(isPrime==True):
            primes.append(i)
        # Set isPrime back to True for next i loop iteration
        isPrime = True
            
    for k in range(len(primes)-1)
        print(primes[k],end=',')
    print(primes[len(primes)-1])
        
    print("There are {} prime numbers <={}".format(len(primes),n))
    print("π({})={}".format(n,n/np.log(n)))
    
