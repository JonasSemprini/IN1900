#Oppgave 1a Obligatorisk oppgave MAT-INF 1100
import numpy as np
from math import sqrt
N = 100
x = np.zeros(N+3) #creating an array of zeros with 103 spaces
x0 = 1 #initial condition 1
x1 = 2 #initial condition 2
x[0] = x0
x[1] = x1

for N in range(0, N+1):
    x[N+2] = 2*x[N+1] + 2*x[N] #formula for representing the n'th term in range of a stated N
    print(f"{x[N]: g}  n: {N}")
"""
Output: python3 Oppgave_1.py
1  n: 0
2  n: 1
6  n: 2
16 n: 3
.
.
.
.
6.30696e+41  n: 96
1.72309e+42  n: 97
4.70758e+42  n: 98
1.28613e+43  n: 99
3.51379e+43  n: 100
"""
