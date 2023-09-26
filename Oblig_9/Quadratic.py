import numpy as np
from math import *
class Parabola():
    def __init__(self, c0, c1, c2):
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2

    def value(self, x):
        f = self.c2*x**2 + self.c1*x + self.c0
        return f

    def table(self, L, R, n):
        print("x    y")
        for t in np.linspace(L, R, n):
            print(f"{t: .3f}, {self.value(t): .3f}")
        return ""
    def roots(self):
        value1 = (-self.c1/2*self.c2)+(sqrt((-self.c1)**2-(4*self.c2*self.c0)))/(2*self.c2)
        value2 = (-self.c1/2*self.c2)-(sqrt((-self.c1)**2-(4*self.c2*self.c0)))/(2*self.c2)
        return value1, value2

Par = Parabola(2, 4, 2)
t = Par.table(0, 10, 11)

def test_parabola():
    x = 3
    expected = 32
    computed = Par.value(3)
    tol = 1e-15
    root1 = -4
    test_root = Par.roots()
    success = abs(expected - computed) < tol
    success2 = root1 == test_root
    assert success, success2
test_parabola()
