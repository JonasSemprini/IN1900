import sys
import numpy as np
import matplotlib.pyplot as plt

#Les fra kommandolinjen
x0 = float(sys.argv[1]) #Startpopulasjon
M = float(sys.argv[2]) #Bærekapasitet
a = float(sys.argv[3]) #Vekstrate

#Opprett array
N = 200
x = np.zeros(N+1)
x[0] = x0

# Regn ut x1,x2....,xN
for i in range(1, N+1):
    x[i] = x[i-1] + a * x[i-1] * (1-x[i-1]/M)

#Plott nx mot n
plt.plot(range(N+1), x, "r-")
plt.xlabel("År")
plt.ylabel("Logistisk vekstmodell")
plt.show()
