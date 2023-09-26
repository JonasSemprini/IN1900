def C(F):
 c1 = (5/9)*(F-32)
 return c1

"""
for F in range(0, 80, 10):
    print(f"Farenheit:{F} Celsius:{C(F)}")
    """


def F(C):
    f1 = (9/5)*C + 32
    return f1
"""for C in range(0, 80, 10):
print(f"Celsius:{C} Farenheit:{F(C)}")
"""

def C_test():
    F1 = 50
    expected = F(-12.22222222222222222222)
    computed = C(50)
    tol = 1e-10
    success = abs(expected - computed) < tol
    msg = (f" (computed) = {computed} != {expected} (expected)")
    assert success, msg
C_test()
