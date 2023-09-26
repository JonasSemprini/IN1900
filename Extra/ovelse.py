from ODESolver import RungeKutta4 as RK4
import numpy as np
def SIR(sigma, mu, b, q, d, T):
    def f(u, t):
        S, I, R = u
        return [sigma(t)-b(t)*S*I +d*R - mu*S,
    b(t)*S*I - q*I-mu*I, q*I - d*R-mu*R]
    solver = RK4(f)
    solver.set_initial_condition([1000, 2, 0])
    time_points = np.linspace(0, T, 100*T+1)
    u, t = solver.solve(time_points)
    S, I, R = u[:,0], u[:,1], u[:,2]
    return t, S, I, R
t, S, I, R = SIR(sigma=lambda t: 10, mu = 0.01,b=lambda t: 0.001, q=1./7, d= 0.01, T = 40)
# Can also make sigma and b as ordinary Python functions
import matplotlib.pyplot as plt
plt.plot(t,S, t, I, t, R)
plt.legend(['S', 'I', 'R'])
plt.show()
