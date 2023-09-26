from math import exp
B = 50000 # carrying capacity
k = 0.2 #growth constant
C = (B - 5000)/5000
t = 0

def N(t, k, B, C):
    N1 = (B/(1+C*exp(-k*t)))
    return N1


for t in range(0, 49, 4):
 print(f"Populasjon:{N(t, k, B, C)} Tid:{t}")
