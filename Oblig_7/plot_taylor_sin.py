from math import factorial
import numpy as np
import matplotlib.pyplot as plt

n = 14 #number for terms (3, 6, 12)
x = np.linspace(0, 4*np.pi, 100) #numpy array with a points from 0 to four pi
                                                                              
def S(x, n): #function for estimating sin(x)
    sum = 0
    #for loop calcuting the sum for n-terms
    for i in range(0, n+1):
        sum = sum + ((-1)**i)*(x**(2*i + 1))/(factorial(2*i + 1))
    return sum
#setting a limit for the y-axis
plt.ylim(-1, 1)

plt.xlabel("x-values")
plt.ylabel("Magnitude")

plt.plot(x, S(x, n), "-r")

plt.plot(x, np.sin(x), "-g")
plt.savefig("plot_taylor.png")
plt.show()

"""
Output: python3 plot_taylor_sin.py
Graph shown in the png picture where the red-line represents the approximated sum,
and the green representing the actual sin(x) function.
"""
