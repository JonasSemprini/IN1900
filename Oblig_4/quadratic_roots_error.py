import sys
from math import sqrt

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    value = (-b/2*a)+(sqrt((-b)**2-(4*a*c)))/(2*a)
    value2 = (-b/2*a)-(sqrt((-b)**2-(4*a*c)))/(2*a)
    print(f"x1 = {value: .1f} x2 = {value2: .1f}")

except IndexError:
    print('No command-line argument for a, b and c!')
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    value = (-b/2*a)+(sqrt((-b)**2-(4*a*c)))/(2*a)
    value2 = (-b/2*a)-(sqrt((-b)**2-(4*a*c)))/(2*a)
    print(f"x1 = {value: .1f} x2 = {value2: .1f}")

"""
Ouput: python quadratic_roots_error.py
For given system arguments in the terminal the program will run as usual.
If not given the program will continue to the except-block for IndexError,
and run input statements instead. The result will be formated the same, regardless of
which method is used. 
"""
