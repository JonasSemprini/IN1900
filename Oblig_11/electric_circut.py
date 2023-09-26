from ODESolver import * #importing the methods from ODESOlver
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

L = 1 #Inductance measured in henrys
w = sqrt(3.5) #angular frequency measured in s^-2
C = 0.25 #Capacitance measured in farad
R = 0.2 #Resistance measured in Ohms

#The change in time with respect to the angular frequency
dt = (2*np.pi)/(60*w)

#Array with time values correspondig to the period of E(t)
time_points = np.linspace(0, (2*np.pi/w)*10, 600)

#Function statement for E(t)
def E(t,w):
    return 2*np.sin(w*t)
"""
Declaration of the class (Electric), which in this excercise
will provide the formal output
to the system of differential equations
"""
class Electric:
    #Constructor corresponding to Electric
    def __init__(self, w, C, R, L, E):
        self.w = w; self.C = C; self.R = R
        self.L = L; self.dt = dt; self.E = E
    #Sepcial method returning our vectorized representation
    #of the differential system
    def __call__(self, u, t):
        Q = u[1] #Declaring Q as the second element of the u array
        I = u[0] #Declaring I as the first element of the u array
        w = self.w; C = self.C; R = self.R
        L = self.L; dt = self.dt; E = self.E
        """
        Derivatives of both the current and the charge in and
        on the electic circuit with respect to the time
        """
        dIdt = (E(t,w) - R*I - (Q/C))/(L)
        dQdt = I

        return dIdt, dQdt

#calling on the class with the given statements
metode = Electric(w, C, R, L, E)
#Using the Forward Euluer approximation
method = ForwardEuler(metode)
#Setting the initial conditions for I(0) and Q(0)
method.set_initial_condition((1,1))

u,t = method.solve(time_points)

plt.xlabel('time (t/s)')
plt.ylabel('Current (ampere)')
plt.plot(t,u)
plt.legend(['I','Q'])
plt.savefig('electric.png')
plt.show()

"""
Output: python3 electric_circut

The output is shown in the png electric.png where both the charge and the current is shown
and how they change and correspond to each other
"""
