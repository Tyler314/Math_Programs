def calcEulerNumber(n):
    ans=0
    for i in range(n):
        ans+=1/math.factorial(i)
    return ans
    
print(calcEulerNumber(400))
print(math.e)
