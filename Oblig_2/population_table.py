from math import exp
B = 50000 # carrying capacity
n = 12
k = 0.2 #growth constant
C = (B - 5000)/5000
N1 = [] # population
t = [] #time

for i in range(0, 49, int(48/n)):
    N = (B/(1+C*exp(-k*i)))
    t.append(i)
    N1.append(N)

for T, N2 in zip(t, N1):
    print(f"tid:{T: g}, populasjon:{N2: g}")

"""
Output: python population_table.py

tid: 0, populasjon: 5000
tid: 4, populasjon: 9912.84
tid: 8, populasjon: 17748.9
tid: 12, populasjon: 27526
tid: 16, populasjon: 36580.2
tid: 20, populasjon: 42924.3
tid: 24, populasjon: 46552
tid: 28, populasjon: 48389.6
tid: 32, populasjon: 49263.3
tid: 36, populasjon: 49666.3
tid: 40, populasjon: 49849.5
tid: 44, populasjon: 49932.3
tid: 48, populasjon: 49969.5

"""
