"""This file holds the three mathematical functions that will be integrated 
over numerically
Note: e is Euler's number, ~ 2.718281828459045"""

import numpy as np

# a(x) = e^(-x^2);
a = lambda x: np.e**(-(x**2))

# b(x) = 1/(2+cos(x))
b = lambda x: 1/(2+np.cos(x))

# c(x) = (e^x)*cos(4x)
c = lambda x: (np.e**x)*np.cos(4*x)