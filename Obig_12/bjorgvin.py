import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *

alpha = 6.5*(10**(-5))
beta = 0.1/4
gamma = 0.9/4

"""
def terminate(u,t, k):
    tol = 1e6
    if abs(u[step_no -1] + u[step_no][1] + u[step_no][2] + u[step_no][3] > 0 ):
        return True
    else:
        return false
"""
def SIRD(alpha, gamma, beta):
    def solver(u, t):
        S, I, R, D = u
        dS = (-alpha*S)*(I)
        dI = (alpha*S*I) - (beta*I) - (gamma*I)
        dR = beta*I
        dD = gamma*I
        return np.array([dS, dI, dR, dD])

    time_points = np.linspace(0, 63, 400)
    metode = RungeKutta4(solver)
    U0 = [7000, 30, 0, 0]
    metode.set_initial_condition(U0)
    u,t = metode.solve(time_points, )
    S, I, R, D = u[:,0], u[:,1], u[:,2], u[:,3]
    return time_points, S, I, R, D

t, S, I, R, D = SIRD(alpha, beta, gamma)
#plt.plot(t, S, t, I, t, R, t, D)
plt.legend(['S', 'I', 'D', 'R'])
#plt.show()
