#Oppgave 5.9
"""
Plot function
y = v0*t - 0.5*g*t**2
for t in [0, 2*v0/g]
"""

import numpy as np
import matplotlib.pyplot as plt
v0 = 10
g = 9.81

n = 200
t_stop = 2*v0/g
dt = t_stop/(n-1)
t = []
"""
for i in range(n):
    t.append(dt*i)

t = np.array(t)

print(t)
exit()
""


"""
t = np.linspace(0, t_stop, n)

y = v0*t - 0.5*g*t**2

plt.plot(t, y)
plt.xlabel('time(s)')
plt.ylabel('height (m)')
plt.show()
