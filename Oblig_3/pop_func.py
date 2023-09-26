from math import exp
B = 50000 # carrying capacity
k = 0.2 #growth constant
C = (B - 5000)/5000 #constant
t = 0 #time

def N(t, k, B, C): #main function for the calculation of the population
    N1 = (B/(1+C*exp(-k*t))) #population equation
    return N1


for t in range(0, 49, 4):
 print(f"Populasjon:{N(t, k, B, C): .1f}  Tid:{t}")

"""
Output: python pop_func.py
Populasjon: 9912.8  Tid:4
Populasjon: 17748.9  Tid:8
Populasjon: 27526.0  Tid:12
Populasjon: 36580.2  Tid:16
Populasjon: 42924.3  Tid:20
Populasjon: 46552.0  Tid:24
Populasjon: 48389.6  Tid:28
Populasjon: 49263.3  Tid:32
Populasjon: 49666.3  Tid:36
Populasjon: 49849.5  Tid:40
Populasjon: 49932.3  Tid:44
Populasjon: 49969.5  Tid:48
"""
