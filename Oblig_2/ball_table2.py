v0 = 5.00 #m/s
g = 9.81 #m/s^-2
n = 20
t = [] #time (s)
y = [] #height (m)

for i in range(0, n+1):
    f = (i*(2*v0/g))/(n+1) #seconds
    x = (v0*f - 0.5*g*f**2) #meters
    t.append(f)
    y.append(x)

for T, Y in zip(t, y):
    print(f" tid:{T: .1f} s posisjon:{Y: .1f} m")

"""
Output: python ball_table2.py
 tid: 0.0 s posisjon: 0.0 m
 tid: 0.0 s posisjon: 0.2 m
 tid: 0.1 s posisjon: 0.4 m
 tid: 0.1 s posisjon: 0.6 m
 tid: 0.2 s posisjon: 0.8 m
 tid: 0.2 s posisjon: 0.9 m
 tid: 0.3 s posisjon: 1.0 m
 tid: 0.3 s posisjon: 1.1 m
 tid: 0.4 s posisjon: 1.2 m
 tid: 0.4 s posisjon: 1.2 m
 tid: 0.5 s posisjon: 1.3 m
 tid: 0.5 s posisjon: 1.3 m
 tid: 0.6 s posisjon: 1.2 m
 tid: 0.6 s posisjon: 1.2 m
 tid: 0.7 s posisjon: 1.1 m
 tid: 0.7 s posisjon: 1.0 m
 tid: 0.8 s posisjon: 0.9 m
 tid: 0.8 s posisjon: 0.8 m
 tid: 0.9 s posisjon: 0.6 m
 tid: 0.9 s posisjon: 0.4 m
 tid: 1.0 s posisjon: 0.2 m
"""
