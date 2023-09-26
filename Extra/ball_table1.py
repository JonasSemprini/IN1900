v0 = 5.00
g = 9.81
n = 10
print("   t", "   y")
"""
for i in range(0, n+1):
    t = (i*(2*v0/g))/(n+1)
    y = (v0*t - 0.5*g*t**2)
    print(f" {t:.2f} {y:.2f}")
"""
i = 0
while i < n+1:
    t = (i*(2*v0/g))/n+1
    y = (v0*t - 0.5*g*t**2)
    print(f" {t:.2f} {y:.2f}")
    i = i+1
