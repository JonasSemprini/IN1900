from math import *
#Class for evaluating the function (f(x: a,w) = e^-a*x * sin(w*x))
class F():
    #Constructor declaring the a and the w value
    def __init__(self, a, w):
        self.a = a
        self.w = w
    #Value method for calculating the values of the function at fixed points
    def value(self, x):
        f = exp(-self.a * x) * sin(self.w * x)
        return f
    #Special method printing the expression of the function
    def __str__(self):
        s = 'exp(self) * sin(w * x)'
        return s

f1 = F(1.0, 0.1) #calling on the function for a = 1 and w = 0.1
f2 = f1.value(x = pi) #calling on the function for x = pi
print(f2)
f1.a = 2 #changing a from 1 to the value of 2
f2 = f1.value(x = pi)
print(f2)
print(f1)

"""
Output: python3 F2.py
0.01335383513703555
0.0005770715401197441
exp(self) * sin(w * x)
"""
