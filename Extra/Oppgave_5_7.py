#Oppgave 5.7

import numpy as np
dx = 0.1
n = round(3.0/dx) + 1

w = np.linspace(0, 3, n)
"""
w[start:stop:step]
"""
print(w[:])
print(w[:-2])
print(w[::5])
print(w[2:-2:6])
