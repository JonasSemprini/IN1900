import numpy as np

def f(x): #function for returning ln(x)
    return np.log(x)

x = np.linspace(1, 10, 101) #array from 1 to 10 with 101 points

y = f(x)

print(f"""x-values for ln(x)
{x}  y-values for ln(x) {y}""")

"""
Output: python fill_log_arrays_vectorized.py
x-values for ln(x)
[ 1.    1.09  1.18  1.27  1.36  1.45  1.54  1.63
1.72  1.81  1.9   1.99...9.46  9.55
9.64  9.73  9.82  9.91 10.]

y-values for ln(x)
[0. 0.0861777  0.16551444 0.2390169  0.3074847  0.37156356
0.43178242 0.48858001 0.54232429 0.59332685 0.64185389 0.6881...
2.20827441 2.21811594 2.22786155 2.2375131  2.24707238 2.25654115
2.26592111 2.2752139  2.28442112 2.29354435 2.30258509]
"""
