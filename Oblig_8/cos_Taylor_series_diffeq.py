#a.)
from math import *
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi*4, 100) #array with x-values ranging from 0 to 4*pi with a 1000 points
n = 2 #number of terms
def cos_difference(x,n): #main function for evaluating the difference equation of cos(x)
    a0 = 1 #first initial condition for aj
    s = a0 #first initial condition for sj
    for i in range(1, n+1):
        a1 = -(x**(2) / ((2*i)*(2*i-1)))*a0 #the a[j] sequence presented as a difference equation
        a0 = a1
        s = s + a1 #the s[j] sequence
    return s, a1

#print(f" n = {n}, approx = {cos_difference(x,n)[1]}")

def cos_taylor_sum(x, n): #function for calculating the taylor series of cos(x)
    sum = 0
    for i in range(n+1):
        sum = sum + ((-1)**i * x**(2*i)) / factorial(2*i) #the taylor expression for cos(x)
    return sum
#test function making sure the difference equation and the taylor expression give the same results
def test_cos_taylor():
    tol = 1e-16
    computed = cos_difference(1,2)[0]
    expected = cos_taylor_sum(1,2)
    success = abs(expected - computed) < tol
    assert success

test_cos_taylor()

plt.plot(x, np.cos(x)) #plotting the exact cos(x)

for n in range(1, 15):
    plt.plot(x,cos_difference(x,n)[0]) #plotting the difference equation

plt.ylim(-1,1) #setting a limit on the y-axis
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.savefig("cos_taylor.png")
plt.show()

"""
Output: python3 cos_Taylor_series_diffeq.py
The plot is shown in png cos_taylor.png
"""
