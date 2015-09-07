def simpsons(f, n, low, up):
    """Calculates an integral by using Simpson's
    rule, a technique used for approximating definite integrals by 
    approximating the functions with n number of polynomials.
    
    The function takes in four input arguments:
    f - The function f(x) being integrated over using this numerical integration technique.
        Defined using a lambda operator.
    n - The number of subdivisions the bounds of integration are divided into.
    low - The lower bound of integration.
    up - The upper bound of integration."""
    
    #Calculate Length of Subdivisions
    h = (up-low)/(n+0.0)
    #Calculate first edge case
    result = f(low)
    #Calculate all the intermediate values with alternating 2's and 4's
    #__________________________________________________________________
    #Initialize a counter to keep track of which value is being calculated
    #in the while loop. That is, use the counter to determine whether to
    #multiply by a 2 or a 4
    counter = 0
    #i corresponds to x_i of the Simpson's Composite Rule
    #(i.e. the current subinterval within the bounds on integration)
    i = low+h
    
    #While the current subinterval is less than the upperbound
    while(i < up):
        #Add the function evaluated at point i to result, multiplied by the
        #appropriate scalar
    
        #If counter is EVEN
        if((counter % 2)==0):
            result += 4*f(i)
        #If counter is ODD
        else:
            result += 2*f(i)
        #Increment counter
        #Increase i by the interval length h
        counter += 1
        i += h
    #Calculate the last edge case of the integral, and add to result
    result += f(up)
    #Multiply entire sum by h/3, according to Simposon's Rule
    result *= (h/3)
    return result

def trapezoidal(f,n,low,up):
    """Calculates an integral by using the trapezoidal
    rule, a technique used for approximating definite integrals using n number
    of trapezoids divided amongst the region of integrations.
    
    The function takes in four input arguments:
    f - The function f(x) being integrated over using this numerical integration technique.
        Defined using a lambda operator.
    n - The number of subdivisions the bounds of integration are divided into.
    lowerBound - The lower bound of integration.
    upperBound - The upper bound of integration."""
    #Calculate the size of the subdivisions
    #Calculate integral
    #_______________________________________________________
    #Calculate Length of Subdivisions
    h = (up-low)/(n+0.0)
    #Find first edge case of integral
    result = 0.5*f(low)
    #Calculate all the intermediate parts of the integral
    #_______________________________________________________
    #The for loop starts at the first subdivision, increments by the 
    #length of one subdivision, up to one subdivision before the
    #upper bound b
    
    #i corresponds to each specific subdivion being incremented through with
    #the while loop
    i = low+h
    
    while(i < up):
        #Add the function evaluated at point i to result
        result += f(i)
        #Increment i to the next subdivision
        i += h
    
    #Calculate the last edge case of the integral
    result += 0.5*f(up)
    #Multiply the result by h, according to the Trapezoidal Rule
    result *= h
    return result