#Oppgave 1b.) Obligatorisk oppgave MAT-INF 1100
import numpy as np
from math import sqrt

N = 100
x = np.zeros(N+3) #creating an array of zeros with 103 spaces
x0 = 1 #initial condition 1
x1 = 1 - sqrt(3) #initial condition 2
x[0] = x0
x[1] = x1

for N in range(0, N+1):
    x[N+2] = 2*x[N+1] + 2*x[N] #formula for representing the n'th term in range of a stated N
    print(f"{x[N]: g}  n: {N}")

"""
Output: python Oppgave_1b.py
 1         n: 0
-0.732051  n: 1
 0.535898  n: 2
-0.392305  n: 3
 0.287187  n: 4
 .
 .
 .
 .
 8.47937e+24  n: 95
 2.31661e+25  n: 96
 6.32909e+25  n: 97
 1.72914e+26  n: 98
 4.7241e+26   n: 99
 1.29065e+27  n: 100
"""
