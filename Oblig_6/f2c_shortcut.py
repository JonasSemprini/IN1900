import numpy as np
import matplotlib.pyplot as plt

F = np.linspace(-20, 120, 1000) #Array for farenheint values ranging from -20 to 120 with a 1000 points
C1 = (F-30)/2 #Shortcut formula
C2 = (F-32)*(5/9) #Main formula

plt.plot(F, C1, '-r') #plottong the shortcut celsius convertion
plt.plot(F, C2, '-b') #plotting the main celsius covertion
plt.xlabel("Farenheit")
plt.ylabel("Celsius")
plt.show()

"""
Output: python3 f2c_shortcut.py

Visualized graph
"""
