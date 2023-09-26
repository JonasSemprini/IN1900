import numpy as np
import matplotlib.pyplot as plt
from math import exp, sin, pi
n = 1000
t = 0 #fixed t-value
x = np.linspace(-4, 4, n) #array for x-values from -4 to 4 with 1000 points

def f(x, t): #main function
    formula = np.exp(-(-x-3*t)**2) * np.sin(3*np.pi*(x-t))
    return formula

plt.plot(x, f(x, t), '-g') #plotting the function
plt.xlabel("Time") #x-axis representing time units
plt.ylabel("Height") #y-axis representing the oscillation
plt.show()

"""
Output: python3 plot_wavepacket.py
Visualized graph when program is ran in the terminal.
"""
