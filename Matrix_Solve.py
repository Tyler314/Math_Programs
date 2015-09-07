import numpy as np
from numpy.matrixlib.defmatrix import matrix

print '\n'
print 'What is the size of your Matrix'
a=int(input('Enter Dimension 1: '))
b=int(input('Enter Dimension 2: '))
# Create empty matrix with user defined inputs
m=np.empty([a,b],dtype=float)
m=matrix(m)

for i in range(a):
    for j in range(b):
        m[i,j]=float(input('Enter Matrix dim [{},{}]: '.format(i+1,j+1)))


print 'What would you like to do?'
print 'Enter the number corresponding to the choice you make.\n'
userInput=int(input('1.) Solve a system of equations.'))

if userInput==1:
    print "Enter the values for matrix 'b' of Ax=b. You already entered 'A'"
    bmatrix=np.empty([a,1])
    bmatrix=matrix(bmatrix)
    for i in range(a):
        bmatrix[i,0]=float(input('Enter b Matrix dim [{},{}]: '.format(i+1,1)))
    
solution = np.linalg.solve(m,bmatrix)
print solution