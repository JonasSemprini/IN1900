#Oppgave 5.29
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 500)
y = np.cos(18 * np.pi * x)

plt.plot(x,y)
plt.show()
