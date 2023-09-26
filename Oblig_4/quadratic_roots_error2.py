from math import sqrt
import sys

try: #try-block for given system arguments
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    value = (-b/2*a)+(sqrt((-b)**2-(4*a*c)))/(2*a)
    value2 = (-b/2*a)-(sqrt((-b)**2-(4*a*c)))/(2*a)
    print(f"x1 = {value: .1f} x2 = {value2: .1f}")

except ValueError: #except-block for given arguments that does not fulfill the requirement of real roots
    print('With the values of a,b and c the roots are not real!')

"""
Output: python quadratic_roots_2.py

Note:
For system arguments not giving real roots the terminal will print the
except-block ValueError statement. Else it will run as usual giving the results in float numbers.
"""
