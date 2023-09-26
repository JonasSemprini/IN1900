
from math import sqrt

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

value = (-b/2*a)+(sqrt((-b)**2-(4*a*c)))/(2*a)
value2 = (-b/2*a)-(sqrt((-b)**2-(4*a*c)))/(2*a)

print(f"x1 = {value: .1f}, x2 = {value2: .1f}")

"""
Output: python quadratic_roots_input.py
a: input(1)
b: input(2)
c: input(3)
x1 = value, x2 = value2
"""
