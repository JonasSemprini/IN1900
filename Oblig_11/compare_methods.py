import numpy as np
import matplotlib.pyplot as plt
from ODESolver import * #importing the methods from ODESOlver

#Class (Runge Kutta 2) inhereting information from ODESolver
class RungeKutta2(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k] #the change in time values
        dt2 = dt/2.0 #calculating the midvalue of every time value change
        K1 = dt*f(u[k], t[k]) #first increment based of the slope in the beggining of the intervall
        K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)# #second increment based of the slope in the midpoint of the intervall
        u_new = u[k] + K2 #The next calculated term in the sequence
        return u_new

#Class (Heun) inhereting information from ODESolver
class Heun(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k] #the change in time values
        dt2 = dt/2.0 #calculating the midvalue of every time value change
        us = u[k] + dt*f(u[k], t[k]) #Forward Euler
        u_new = u[k] + dt2*f(u[k], t[k]) + dt2*f(us, t[k+1]) #calculating the next term in the sequence with the use of forward Euler and the trapezodial rule
        return u_new

#Differential expression
def f(u,t):
    return (t*np.cos(t)) - np.sin(t)

#Initiating a subplot
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)

#The exact solution to the differential equation
def exact(t):
    return t * np.sin(t) + 2 * np.cos(t)

#number of time steps
n = [20,25,50, 150]

metode = RungeKutta2(f)

#Setting the inital condition
metode.set_initial_condition(-17)

for i in range(len(n)):
    #array with time values
    time_points = np.linspace(-17,17, n[i])
    u,t  = metode.solve(time_points)
    ax1.set_title('Runge Kutta 2')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    plt.tight_layout()
    ax1.plot(t, u)

metode2 = RungeKutta4(f)
metode2.set_initial_condition(-17)

for i in range(len(n)):
    time_points = np.linspace(-17,17, n[i])
    u1,t1  = metode2.solve(time_points)
    ax2.set_title('Runge Kutta 4')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    plt.tight_layout()
    ax2.plot(t1, u1)

metode3 = Heun(f)
metode3.set_initial_condition(-17)

for i in range(len(n)):
    time_points = np.linspace(-17,17, n[i])
    u2,t2  = metode2.solve(time_points)
    ax3.set_title('Heun')
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    plt.tight_layout()
    ax3.plot(t2, u2)

for i in range(len(n)):
    time_points = np.linspace(-17,17, 200)
    ax4.set_title('Exact')
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    plt.tight_layout()
    ax4.plot(time_points, exact(time_points))
plt.savefig('compare.png')
plt.show()

"""
Output: python3 compare_methods
The output is shown in the png compare.png where all the numercial estimations are shown in the same plot,
togheter with the exact solution
"""
