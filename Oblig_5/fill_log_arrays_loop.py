import numpy as np

n = 101 #number of points
N = 10 #last point in the intervall [1, 10]
x_array = np.zeros(n) #empty array with 101 points
y = np.zeros(n) #empty array with 101 points

for i in range(1, n):
    x_array[i] = (i*10)/n)
    y[i] = np.log(x_array[i])
    print(f"x-values:{x_array} y-values:{y}")
"""
Output: python fill_log_arrays_loop.py
x-values:
[ 1.0990099   1.1980198   1.2970297   1.3960396   1.4950495
1.59405941  1.69306931  1.79207921  1.89108911  1.99009901  2.08910891
....10]

y-values:
[0.09440968 0.18067003 0.26007681 0.33363937 0.40215932
0.46628385 0.52654304 0.58337651 0.63715291 0.68818439 0.7367...
2.29363426 2.3035747  2.3134173  2.32316397 2.33281655 2.342376852.3
5184662 2.36122755 2.3705213  2.37972947 2.38885362]
"""
