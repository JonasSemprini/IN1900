import numpy as np

#Opprett array
N = 20
x = np.zeros(N+1)

#Les fra bruker
x[0] = float(input("Innskudd: "))
p = float(input("Rente (prosent): "))

#Regn ut x1,....,xn
for i in range(1, N+1):
    x[i] = (1+ p/100) * x[i-1]

print("Aar  Verdi")
for i in range(N+1):
    print(f"{i}  {x[i]}")
