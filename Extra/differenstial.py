import numpy as np
import matplotlib.pyplot as plt
"""dt = 0.01
T = 5

n = int(T/dt) + 1

t = np.linspace(0, T, n)
u = np.zeros(n)

u[0] = 0.5

for i in range(1, n):
    u[i] = u[i-1] + dt  * u[i-1] * (1 - u[i])


plt.plot(t, u, 'ko')
plt.plot(t, np.exp(t), 'b-')
plt.show()
"""

def Forward(f, U0, T, n):
    t = np.zeros(n+1)
    u = np.zeros(n+1)
    u[0] = U0
    dt = T/n
    for i in range(0, n-1):
        t[i+1] = t[i] + dt
        u[i+1] = u[i] + dt*f(u[i], t[i])
    return u, t

def f(u, t):
    return u * (1-u)

u, t = Forward(f, 1, 4, 20)

plt.plot(t, u)
plt.show()


class ForwardEuler:
    def __init__(self, f):
        self.f = f

    def initial_condition(self, U0):
        self.U0 = U0

    def solve(self, time_points):
        n = time_points.size
        self.t = time_points
        self.u = np.zeros(n)
        self.u[0] = self.U0
        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
        return self.u, self.t

    def advance(self):
        u = self.u; t = self.t; f = self.f; k = self.k
        dt = t[k+1]-t[k]
        return u[k] + dt * f(u[k], t[k])

f = lambda u,t: u**2 * (1-u)

F = ForwardEuler(f)

F.initial_condition(0.5)

t = np.linspace(0, 5, 100)
u,t = F.solve(t)

plt.plot(t, u)
plt.show()
