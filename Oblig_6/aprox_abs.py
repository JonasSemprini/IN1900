import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100) # An array for the x-values from -pi to pi with hundred points
N = 4 #number of terms in the sum
def f(x): #main function for the sum
    sum = 0
    for i in range(1, N+1):
        sum += np.cos((2*i-1)*x) /((2*i-1)**2)
    result = np.pi/2 - 4/np.pi*sum
    return result
plt.plot(x, f(x), "-r") #plotting the sum function
plt.plot(x, abs(x), "-b") #plotting the absolute value of x
plt.show()

"""
Output: python3 aprox_abs.py
Visualized graphs where the blue function is the |x|,
and the red is the approximated sum.
"""
