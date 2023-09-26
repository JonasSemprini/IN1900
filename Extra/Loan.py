#Oppgave A.4
import numpy as np

def verdi(L, p, N):
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    x[0] = L
    for n in range(1, N+1):
        y[n] = p / (12*100) * x[n-1] + L/N
        x[n] = x[n-1] + p/(12*100) * x[n-1] - y[n]
    return x, y

#Lån på 1000kr, årlig rente 10 prosent, 12mnd
#tilbakebetalingstid

x, y = verdi(1000, 10 , 12)
print("Måned  Betalin Lån etter måneden")
for k in range(len(x)):
    print(f"{k:5.1f} {y[k]:5.1f} {x[k]:8.1f}")
