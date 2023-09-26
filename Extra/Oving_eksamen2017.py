"""
def heavy(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1
def test():
    x = [-1.0, 1.0]
    expected = [0, 1]
    computed = [heavy(x[0]), heavy(x[1])]
    tol = 1e-7
    for i in range(len(x)):
        success = abs(expected[i] - computed[i]) < tol
        if computed[0] == 0  and computed[1] == 1:
            return ""
        else:
            assert success
test()
"""
"""
import numpy as np

def is_prime(k):
    if k >= 1:
        for o in range(2, k):
            if (k % o) == 0:
                return False
        else:
            return True

j = [1,2,3,6,9,27]
for i in j:
    print(f"{i} {is_prime(i)}")
"""
class Heun(ForwardEuler):
    def adavance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        dt2 = dt/2
        us = u[k] + dt*f(u[k], t[k])
        u_new = u[k] + dt2*f(u[k], t[k]) + dt2*f(us, t[k+1])
        return u_new

metode = Heun(f, 1, 10, 100)
u, t = metode.solve()

def predator_prey(x0, y0, r, a, m, b, T, n):
    def f(u,t):
        x,y = u
        dx = r*x - a*x*y
        dy = -m*y + b*x*y
        return np.array([dx, dy])
    U0 = [1,1]
    metode = Heun(f,0, U0, T, n)
    u,t = metode.solve()
    dx, dy = u[:, 0], u[:, 1]
    return t, dx, dy
t, dx, dy = predator_prey(1, 1, 1, 0.3, 1, 0.2, 20, 100)
plt.plot(t, dx, t, dy)
plt.legend(['dx', 'dy'])
plt.show()
