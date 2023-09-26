"""
def f(x):
    if x < 0:
        return 0
    elif x >= 0 and x < 2:
        return x**2
    else:
        return 4

print(f(
"""

"""
from Parabola import *
class Line(Parabola):
    def __init__(self, c0, c1):
        Parabola.__init__(self, c0, c1, 0)
"""

def sum_file(filename, outputname):
    infile = open(filename, 'r')
    tall = []
    for line in infile:
        row = [float(word) for word in line.split()]
        row.append(sum(row))
        tall.append(row)

    with open(outputname,'w') as outfile:
        for j in tall:
            line = ''
            for i in j:
                line += f'{i: 7.2f}'
            outfile.write(f'{line} \n')
sum_file('tall.txt', 'tall2.txt')

"""
def sum_file(inputname,outputname):
    numbers = []
    with open(inputname,'r') as infile:
        for line in infile:
            row = [float(word) for word in line.split()]
            row.append(sum(row))
            numbers.append(row)
outfile.write(f'{i :14.2f}''\n')
    with open(outputname,'w') as outfile:
        for row in numbers:
            line = ''
            for number in row:
                line += '%7.2f' %number
            line += '\n'
            outfile.write(line)
sum_file('tall.txt', 'tall2.txt')
"""
"""
def _exp_diffeq(x, n):
    x = float(x)
    e0 = 0
    a0 = 1
    for i in range (0, n+1):
        e = e + a
        a = x/n * a
    return e
"""
"""
def test_midpoint():
    f = lambda u,t: 5
    expected = lambda t: 5*t + 1
    computed = midpoint(f)
    computed.set_initial_condition(1)
    tol = 1e-7
    u,t = computed.solve([0,1,2,3])

    for u1, t1 in zip(u,t):
        success = abs(expected(t1) - u1) < tol
        assert success
"""
