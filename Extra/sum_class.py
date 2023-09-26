#Oppgave 7.12
class Sum:
    def __init__(self, term, M, N):
        self.term = term
        self.M = M
        self.N = N

    def __call__(self, x):
        S = 0
        for i in range(self.M, self.N+1):
            S += self.term(k,x)
        return S

#a)
#following code should work

def term(k, x):
    return (-x)**k

S = Sum(term, M = 0, N = 3)

x = 0.5

print(S(x))
print(S.term(k = 4, x = x)) #-0.5**4
#exit()

#b.)
def test_sum():
    def f(k,x):
        return (-x)**k
    S = Sum(term = f, M = 0, N = 3)

    x = 0.5
    expected = 1 - x + x**2 - x**3
    computed = S(x)
    tol = 1e-10
    assert abs(computed - expected) < tol
test_Sum()
#exit()

#c.)
from math import *

def taylor_sin(k, x):
    return (-1)**k * (x**(2*k+1)) / factorial(2*k+1)

S = Sum(taylor_sin, 0, 5)
x1 = pi
x2 = pi/2

print(S(x1), S(x2))
