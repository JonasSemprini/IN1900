#Oppgave 5.11
"""
Plot function
y = v0*t - 0.5*g*t**2
for t in [0, 2*v0/g]
"""
import numpy as np
import matplotlib.pyplot as plt
import sys

n = 101
g = 9.81

max_t = 0
max_y = 0

for v0 in sys.argv[1:]:
    v0 = float(v0)
    t_stop = 2*v0/g
    t = np.linspace(0, t_stop, n)
    y = v0*t - 0.5*g*t**2
    if max(t) > max_t:
        max_t = max(t)
    if max(y) > max_y:
        max_y = max(y)

    plt.plot(t, y)

plt.axis([0, max_t, 0, max_y*1.05])
plt.xlabel('time(s)')
plt.ylabel('height (m)')
plt.show()
