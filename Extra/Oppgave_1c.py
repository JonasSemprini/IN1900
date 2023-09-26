import numpy as np
from math import sqrt

N = 100
x = np.zeros(N+3) #creating an array of zeros with 103 spaces
x0 = 1 #initial condition 1
x1 = 1 - sqrt(3) #initial condition 2
x[0] = x0
x[1] = x1

#Simulert løsning
for N in range(0, N+1):
    x[N+2] = 2*x[N+1] + 2*x[N] #formula for representing the n'th term in range of a stated N
    print(f"{x[N]: g}  n: {N}")

#Analytisk løsning

for N in range(0, N+1):
  sum = (1 - sqrt(3))**N
  print(f"{sum: g}  n:{N}")


"""
Output: python Oppgave_1c.py

Simulert løsning:
 1         n: 0
-0.732051  n: 1
 0.535898  n: 2
-0.392305  n: 3
 0.287187  n: 4
 .
 .
 .
 2.31661e+25  n: 96
 6.32909e+25  n: 97
 1.72914e+26  n: 98
 4.7241e+26   n: 99
 1.29065e+27  n: 100

 Analytisk løsning: 
 1         n:0
-0.732051  n:1
 0.535898  n:2
-0.392305  n:3
 0.287187  n:4
 .
 .
 .
 9.90735e-14  n:96
-7.25268e-14  n:97
 5.30933e-14  n:98
-3.8867e-14   n:99
 2.84526e-14  n:100
"""
