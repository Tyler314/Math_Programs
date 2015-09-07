nvwqbvhiqrhv[from numpy import pi
from sys import argv
sum=0.0
try:
 s = int(argv[1])
except:
 s = 2
for n in range(1, 100):
 sum += 1/(n**s)

print sum
