import numpy as np
import matplotlib.pyplot as plt
#a.)

n = 101 #number of points
y_array = np.zeros(n) #empty array
t_array = np.zeros(n) #empty array
k = 4 #kg s^-2
gamma = 0.15 #s^-1
m = 9 #kg
A = 0.3 #m
L = 25

for i in range(0, n):
    tid = (L*i)/n #time values with point 101 points from 0 to 25
    formula = (A * np.exp(-gamma*tid) * np.cos(np.sqrt(k/m)*tid)) #meters
    y_array[i] = formula #adding y-values to the y(t) array
    t_array[i] = tid #adding the t-values to the time array

print(f" Time: {t_array} height: {y_array}")

#b.)

n = 101 #number of points
k = 4
gamma = 0.15 #s^-1
m = 9
A = 0.3
t_array = np.linspace(0, 25, n)

def y(k, gamma, m, A):
    formula = (A * np.exp(-gamma*t_array) * np.cos(np.sqrt(k/m)*t_array))
    return formula
y2 = y(k, gamma, m, A)

plt.plot(t_array, y2)
plt.xlabel("Time(s)")
plt.ylabel("Height(m)")
plt.show()

"""
Output: python oscillating_spring.py
a.)
Time:

[ 0. 0.24752475  0.4950495  0.74257426  0.99009901  1.23762376
1.48514851  1.73267327...25]
Height:

[ 0.3  0.28513886  0.263498 0.23615791 0.20427849 0.16906153
 0.13171459 0.09341741...-0.00841884 -0.00782267 -0.00705399
 -0.00614629 -0.00513449]
b.)
Visualized graph when the program is ran
"""
