def f(x)
  return x**3

n = 5 #number of points
dx = 1.0/(n-1)
xlist = [i*dx for i in range(n)]
ylist = [f(x) for x in xlist]

pairs = [[x, y] for x, y in zip(xlist, ylist)]

import numpy as np

x = np.array(xlist)
y = np.array(ylist)

x = np.linspace(0, 1, n) #n points in [0,1]
y = np.zeros(n) #n zeros (float data type)
for i in range(n)
  y[i] = f(x[i])

from math import sin

for i in range(len(x))
  y[i] = sin(x[i])

"""Mer effektiv og smartere måte å representere
en array av x og y-verdier for sinus"""
import numpy as np
y = np.sin(x)
