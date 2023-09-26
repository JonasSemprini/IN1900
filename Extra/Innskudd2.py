import numpy as np

#Les fra bruker
innskudd = float(input("Innskudd: "))
p = float(input("Rente (prosent): "))
N = int(input("Antall dager: "))

#Opprett array
x = np.zeros(N+1)
x[0] = innskudd

r = p/360

#Regn ut x1,....,xn
for k in range(1, N+1):
    x[k] = (1 + r/100) * x[k-1]

print("Aar    Verdi")
for i in range(N+1):
    print(f"{i: 5.2f}  {x[i]: 5.2f}")
