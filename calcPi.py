import numpy as np

def calcPi(n):
    """Use Riemann Zeta fucntion evaluated at 2 to approximate pi out to n summations"""
    result=0
    for i in range(1,n+1):
        result += (i**2)**-1
        
    result *= 6
    result = np.sqrt(result)
    return result
    
