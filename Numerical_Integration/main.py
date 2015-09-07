"""The three mathematical functions being integrated over are defined in the 
mathFunctions.py file using the lambda operation. This is done so that the  
mathematical functions are able to be passed as arguments to Simpson's method 
and the Trapezoidal method."""

#Import the mathematical functions from mathFunctions.py, and the numerical 
#integration techniques from integrationMethods.py
from mathFunctions import *
from integrationMethods import *

print "\nThe following definite integrals are calculated using both the Trapezoidal Method, and with Simpson's Rule."
print "With n = 2,4,8,16,32,64,128,256,512\n"

#Calculate integrals using Trapezoidal Method
i=2
print "Trapezoidal Method"
print "   f(x) = e^(-x^2), integrated from 0 to 1"
while(i<=512):
    print "      n = " + str(i)
    print "         Integration = " + str(trapezoidal(a,i,0,1))
    #Increase i by a factor of 2
    i*=2

i=2
print "\n   f(x) = 1/(2+cos(x)), integrated from 0 to 2*pi"
while(i<=512):
    print "      n = " + str(i)
    print "         Integration = " + str(trapezoidal(b,i,0,2*np.pi))
    #Increase i by a factor of 2
    i*=2
    
i=2
print "\n   f(x) = (e^x)*cos(4x), integrated from 0 to pi"
while(i<=512):
    print "      n = " + str(i)
    print "         Integration = " + str(trapezoidal(c,i,0,np.pi))
    #Increase i by a factor of 2
    i*=2

#Calculate integrals using Simpson's Method
i=2
print "\nSimpson's Method"
print "   f(x) = e^(-x^2), integrated from 0 to 1"
while(i<=512):
    print "      n = " + str(i)
    print "         Integration = " + str(simpsons(a,i,0,1))
    #Increase i by a factor of 2
    i*=2

i=2
print "\n   f(x) = 1/(2+cos(x)), integrated from 0 to 2*pi"
while(i<=512):
    print "      n = " + str(i)
    print "         Integration = " + str(simpsons(b,i,0,2*np.pi))
    #Increase i by a factor of 2
    i*=2
    
i=2
print "\n   f(x) = (e^x)*cos(4x), integrated from 0 to pi"
while(i<=512):
    print "      n = " + str(i)
    print "         Integration = " + str(simpsons(c,i,0,np.pi))
    #Increase i by a factor of 2
    i*=2