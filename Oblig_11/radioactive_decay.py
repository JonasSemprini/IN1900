import numpy as np
import matplotlib.pyplot as plt
from ODESolver import * #importing the methods from ODESOlver
#Implemented class to solve the numerical approximation
class Decay:
#Constructor corresponding to decay and delegating information about declared variabels
    def __init__(self, a):
        self.a = -a
#Special method returning the differential expression
    def __call__(self, u, t):
        return self.a*u

#Exact solution
def func(a, t):
    return np.exp(-a*t)

#Inverse of the mean lifetime of the substance
a = np.log(2)/5600
#Calling on the class with the given parameters
metode = Decay(a)
#Using the Runge - Kutta 4 method
method = RungeKutta4(metode)
#Setting the initial condition u(0) = 1
method.set_initial_condition(1)
#Array with time values
time_points = np.linspace(0, 20000, 500)
u,t = method.solve(time_points)
plt.xlabel('time (y/years)')
plt.ylabel('Remaining fractions')
plt.plot(t, u, label='Runge - Kutta 4')
plt.plot(time_points, func(a, time_points), label='Exact')
plt.legend()
plt.savefig('radioactive.png')
plt.show()

"""
Output: python3 radioactive_decay.py
The output is shown in the png 'radioactive.png' where both the exact and the approximated solution is shown.
Also notice that the both the solutions seem fully alike.
"""
