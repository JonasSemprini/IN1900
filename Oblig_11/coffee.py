import matplotlib.pyplot as plt
import numpy as np
from ODESolver import * #importing the methods from ODESOlver
#Class implemented to solve the differential expression
class Problem:
    #Constructor corresponding to the class, delegating information about,
    #The declared varibles
    def __init__(self, h, Ts):
        self.h = h
        self.Ts = Ts
    #Special method returning the expression of the differential equation
    #T' = -h(T- Ts)
    def __call__(self, T, t):
        y = -self.h*(T - self.Ts)
        return y
    #Terminate method to implement an asymptote to the corresponding differential expression
    def terminate(self, u, t, step_no):
        tol = 1e-7 #tolerance
        return abs((u[step_no] - u[step_no - 1])) < tol #testing the expression for its asymptotic value
#Function to make an estimate of the h-constant
def estimate_h(t1, Ts, T0, T1):
    h = (T1 - T0) / (t1*(Ts - T0))
    return h

t1 = 15 #Second time measurment
Ts1 = 20 #First testing value of the room temperature
Ts2 = 25 #Second testing value of the room temperature
T0 = 95 #First calculated term of the temperatur of the coffee
T1 = 92 #Second measurment

#Array of time values from 0 to 1400 with 10000 points
time_points = np.linspace(0, 1400, 10000)

h = estimate_h(t1, Ts1, T0, T1)
h2 = estimate_h(t1, Ts2, T0, T1)
#Calling on the class with the given arguments
instance = Problem(h, Ts1)
instance2 = Problem(h2, Ts2)
metode = RungeKutta4(instance)
metode2 = RungeKutta4(instance2)
#Setting the initial condition
metode.set_initial_condition(95)
metode2.set_initial_condition(95)
u,t = metode.solve(time_points, instance.terminate)
u2, t2 = metode2.solve(time_points, instance2.terminate)

#Exact solution to the differential equation with C = 75
def exact(t):
    return 75*np.exp(-h*t) + Ts1

#Test function implemented to check if the class gives a correct corresponding output
def test_problem():
    time_points2 = np.linspace(0, 15, 16) #new linspace with t-values
    expected = exact(time_points[5]) #exact solution with t = 5
    computed = u[5] #computed solution testing the expression with the fifth term of u
    tol = 1e-7 #tolerance
    success = abs(expected - computed) < tol
    msg = f'expected :{expected}, but got {computed}'
    assert success, msg
test_problem()

plt.plot(t,u, label = 'f(Ts1)')
plt.plot(t2, u2, label='f(Ts2)')
plt.xlabel('time (t/s)')
plt.ylabel('temperatur (Celsius)')
plt.legend()
plt.savefig('coffee.png')
plt.show()

"""
Output: python3 coffee.py
The output is shown in the png coffee.png where both the solutions are shown with different labels
"""
