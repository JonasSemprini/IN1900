import sys

v0 = float(sys.argv[1]) #system argument 1
g = 9.81
t = float(sys.argv[2]) #system argument 2
y = v0*t - 0.5*g*t**2

print(f"""After a time {t} s the distance
the ball has traveled is
{y: .3f} m """)

"""
Output: python ball_cml.py

After a time sys.argv[2] s the distance
the ball has traveled is
sys.argv[1] m

"""
