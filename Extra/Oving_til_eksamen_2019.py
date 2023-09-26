"""
def piecewise(x):
    if x < 0:
        return -1
    else:
        return 1

def test_piece():
    x = [-0.5, 0.5]
    expected = [-1, 1]
    computed = [piecewise(x[0]), piecewise(x[1])]
    tol = 1e-6
    for i in range(len(x)):
        success = abs(computed[i] - expected[i]) < tol
        if computed[0] == -1 and computed[1] == 1:
            return ""
        else:
            assert success
test_piece()
"""
"""
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

n_values = np.linspace(0, 5, 100)
def exp_approx(x,n):
    s = 0
    for i in n_values:
        s+= (x**i) / factorial(i)
        return s

def plot_exp(n_values):
    x = np.linspace(0, 5, 100)
    for i in n_values:
        y = exp_approx(x, i)
        plt.plot(x,y)
    plt.plot(x, np.exp(x))
    plt.show()
plot_exp(n_values)
"""
"""
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

n_values = [0,1,5,10,15,20,30]
x = np.linspace(0,5,100)
def exp_approx(x,n):
    s = 0
    for k in range(n+1):
        s += x**(k)/ (factorial(k))
    return s

def plot_approx(n_values):
    x1 = np.linspace(0, 5, 100)
    for n in n_values:
       y = exp_approx(x, n)
       plt.plot(x1, y, 'ro')
    plt.plot(x1, np.exp(x1))
    plt.show()
plot_approx(n_values)
"""
"""

def read_file(filename):
    infile = open(filename, 'r')
    countries = {}
    for line in infile:
        words = line.split()
        countries[words[0]] = ''.join(words[1:])
    return countries
"""
dna_list = ['GCTCT', 'GGTAC', 'GATGC']
for dna in dna_list:
    for index in enumerate(dna):
        print(index)
