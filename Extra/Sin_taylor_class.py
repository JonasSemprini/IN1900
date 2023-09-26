#7.13
from math import *
class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def __call__(self, x):
        return exp(-self.a*x)*sin(self.w*x)

    def __str__(self):
        return 'exp(-a*x) * sin()w*x'


f = F(a = 1.0, w = 0.1)
print(f(pi))
print(f)
