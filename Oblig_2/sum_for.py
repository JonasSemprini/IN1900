s = 0
M = 4
k = 1
s1 = 0

for i in range(1,4):
    s += 1/(2*i)**2
print(f"Sum:{s: .1f}")



while k < M:
    s1 += 1/(2*k)**2
    k = k+1
print(f"Sum:{s1: .1f}")

"""
Output: sum_for.py
Sum: 0.3
Sum: 0.3

Comments:
The main errors to the faulty syntax:
1. The range was set to M which in the program was a variable with the value of 3,
and that doesn`t give a correct output considering the range of the sum was set to 1->3
2. The second error was the paranthesis in (2k)^2. In the syntax the program will interperet it as
0.5*(k^2)
3. k is not defined as a variable.
"""
