#Oppgave 5.13
import sys
import numpy as np
import matplotlib.pyplot as plt

from math import cos, tan, sqrt

y0, theta, v0 = [float(arg) for arg in sys.argv[1:]]
g = 9.81

#a*x**2 + b*x + c
a = -1.0/(2*v0**2)*(g/cos(theta)**2)
b = tan(theta)
c = y0

x1 = (-b + sqrt(-b**2-4*a*c))/(2*a)
x2 = (-b - sqrt(-b**2-4*a*c))/(2*a)

x_max = max(x1, x2)

x = np.linspace(0, x_max, 101)
y = a*x**2 + b*x + c

plt.plot(x, y)
plt.show()
