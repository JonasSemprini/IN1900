"""
def f(x):
    if x <= 0:
        return -x
    else:
        return x

def test():
    x = [-3, 1]
    excpected = [-x[0], x[1]]
    computed = [f(x[0]), f(x[1])]
    tol = 1e-9
    for i in range(len(x)):
        success = abs(computed[i] - excpected[i]) < tol
        msg = f'Got {computed}, but wanted {excpected}'
        assert success, msg
test()

from math import factorial
def exp(x):
    s = 0
    for k in range(0, x+1):
        s += (1**k/factorial(k))
    return s

def test_exp():
    N = 3
    x = 1
    tol = 1e-7
    expected = 1 + x + x**2/2 + x**3/6
    computed = exp(N)
    success = abs(expected - computed) < tol
    assert success
test_exp()
"""
"""
class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients
    def __call__(self, x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s

    def __add__(self, other):
            # Start with the longest list and add in the other
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:] # copy!
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]

        else:
            result_coeff = other.coeff[:] # copy!
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]

        return Polynomial(result_coeff)


    def diff(self):
        difference = []
        for i in range(1, len(self.coeff)):
            difference.append(i*self.coeff[i])
        return Polynomial(difference)

def test_diff():
    tol = 1e-7
    x = 2
    expected = 1 + 4*x + 9*x**2
    p = Polynomial([0, 1, 2, 3])
    computed = p.diff()(x)
    success = abs(expected - computed) < tol
    msg = f' got {computed} but wanted {expected}'
    assert success, msg

test_diff()
"""
"""
from ODESolver0 import *

class RungeKutta3(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)
        K3 = dt*f(u[k] - K1 + 2*K2, t[k] + dt)
        u_new = u[k] + 1/6(K1 + 4*K2 + K3)
        return u_new

def test_RK3():
    f = lambda u,t: 2
    expected = lambda t: 2*t +1
    computed = RungeKutta3(f)
    computed.set_initial_condition(1)
    time = [0,1,2,3,4]
    u,t = computed.solve(time)
    tol = 1e-15
    for i, j in zip(u,t):
        success = abs(i - expected(j)) < tol
        assert success
test_RK3()
"""
"""
from ODESolver0 import *
import numpy as np
import matplotlib.pyplot as plt

def SIR(S0, I0, sigma, mu, b, q, d, T):
    def f(u,t):
        S, I, R = u
        dS = sigma(t) - b(t)*S*I + d*R - mu*S
        dI = b(t)*S*I - q*I - mu*I
        dR = q*I - d*R - mu*R
        return dS, dI, dR

    metode = RungeKutta4(f)
    U0 = [1000, 2, 0]
    metode.set_initial_condition(U0)
    time = np.linspace(0, T, 100*T+1)
    u,t = metode.solve(time)
    S,I,R = u[:,0], u[:,1], u[:,2]
    return t, S, I, R

sigma = lambda t: 10
b = lambda t: 0.001

t, S, I, R = SIR(1000, 2, sigma, 0.01, b, 1/7, 0.01, 40)
plt.plot(t, S, t, I, t, R)
plt.show()
"""
