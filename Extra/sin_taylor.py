import numpy as np
import matplotlib.pyplot as plt

def sin_taylor(x, n):
  a = x
  s = 0

  for i in range(1, n+2):
    s = s+a
    a = -(x**2/((2*i+1)*2*i)) * a

    return s, abs(a)

x = np.pi/2
for n in [1,2, 5]:
    print(f"n= {n}, approx = {sin_taylor(x,n)[0]}")

def test_sin_taylor():
    from math import factorial
    print("Calling test function")
    x = 0.5
    tol = 1e-10
    expected = x - (x**3)/factorial(3) + (x**5)/factorial(5)
    computed = sin_taylor(x,2)[0]
    success = abs(expected - computed) < tol
    assert success
test_sin_taylor()

x_max = 4*np.pi
x = np.linspace(0, 4*np.pi, 1001)

for n in range(10):
    y = sin_taylor(x,n)[0]
    plt.plot(x,y,label=f"n={n}")

plt.plot(x, np.sin(x), label = 'exact')
plt.axis([0, x_max,-2,2])
plt.legend()
plt.show()
