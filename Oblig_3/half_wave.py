from math import sin #importing the sine function
def f(x): #main function
    sinus = sin(x)
    if sinus <= 0:
        return 0
    else:
        return sinus

def rect_test(): #test function for def f()
    x = 3
    expected = sin(3) #expected output for sin(3)
    computed = f(3) #estimated output for the main fuction with an argument of x = 3
    tol = 1e-4 #tolerance of a small quantity to narrow down possible round off errors
    success = abs(expected - computed) < tol
    msg = (f" (computed) = {computed} != {expected} (expected)")
    assert success, msg
rect_test()

"""
Output: python half_wave.py

Note:
The output is blank for given arguments that fulfil
the success statement in the test function. Otherwise there will be an assertion mistake.
"""
