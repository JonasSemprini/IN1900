from math import exp, pi
import numpy as np
from time import time
import matplotlib.pyplot as plt

def f(x, mu=0, sigma=1):
    return exp(-(x-mu)**2/(2*sigma**2))/((2*pi*sigma**2)**(1/2))

def midpoint(x, h):
    return f(x+ h/2)*((h/2)-x)

def integral(xmin, xmax, n):
    t0 = time()
    print()
    print("n = ", n)
    xs = np.linspace(xmin, xmax, n)
    h = (xmax - xmin)/(n - 1)
    print("h = ", h)
    sum = 0.0
    for x in xs[:-1]:
        sum += midpoint(x, h)
    t1 = time()
    t = t1 - t0
    return sum, t

"""
numcalc, t = integral(-10, 10, n)
print("Numerical calculation:", numcalc)
print("Time (seconds):", round(t, 4))
"""
for n in range(2, 20000, 50):
    numcalc, t = integral(-1000, 1000, n)
    error = abs(numcalc - 1)/ numcalc
    plt.semilogy(np.log(n), error, 'ro')
plt.show()
