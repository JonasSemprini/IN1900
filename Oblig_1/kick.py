from math import pi

massF = 0.43 #kg
g = 9.81 #m/s-2
G = massF*g #kgms^-2

density = 1.2 #kgm^-3
radA = 11*(10**-2) #meters
A = pi*(radA**2) #
dragC = 0.4

V1 = 120/3.6 #m/s
V2 = 30/3.6 #m/s

forceA = 0.5*(dragC*density*A*(V1**2)) #kgms^-2
forceB = 0.5*(dragC*density*A*(V2**2)) #kgms^-2

ratio1 = forceA / G
ratio2 = forceB / G


print(f"""
The air resistance utilizez an amount of {forceA: .1f}
Newtons or kgms^-2 from the harder kick""")

print(f"""
The gravitational force of the ball
is estimated to be {G: .1f} Newtons or kgms^-2""")

print(f"""
The ratio between the air resistance
and the gravitational force is {ratio1: .1f}
Newtons or kgms^-2""")

print(f"""
The air resistance utilizez an amount of
{forceB: .1f} Newtons or kgms^-2 from a less powerful
kick""")


print(f"""
The ratio between the air resistance and the
gravitational force is {ratio2: .1f}
Newtons or kgms^-2""")

"""
Output: python kick.py

The air resistance utilizez an amount of  10.1
Newtons or kgms^-2

The gravitational force of the ball
is estimated to be  4.2 Newtons or kgms^-2

The ratio between the air resistance
and the gravitational force is  2.4
Newtons or kgms^-2

The air resistance utilizez an amount of
0.6 Newtons or kgms^-2 from a less powerful
kick

The ratio between the air resistance and the
gravitational force is  0.2
Newtons or kgms^-2
 """
