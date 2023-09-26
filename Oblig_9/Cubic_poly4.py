class Parabola(): #Parabola (2nd degree polynomial) class

    #Constructor declaring all the constanst which are being used in the program for a 2nd degree polynomial
    def __init__(self, c0, c1, c2):
        self.c0 = c0 #constant c
        self.c1 = c1 #constant b
        self.c2 = c2 #constant a

#speical method for printing the values of the parabola when the class is called
    def __call__(self, x):
        print("This is a parabola")
        return self.c2*x**2 + self.c1*x + self.c0 #returnin a*x^2 + b*x + c
#method for printing out the y values in a intervall from L to R with n partitions
    def table(self, L, R, n):
        s = ''
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s

#Class for a Cubic polynomial (3rd degree) inhereting information from Parabola
class Cubic(Parabola):
    #Constructor for declaring all the constants in a cubic polynomial where it inherits the values from parabola
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2) #inhereting information from the superclass parabola
        self.c3 = c3
    #Special method inhereting information from Parabola and returning the values for the cubic polynomial
    def __call__(self, x):
        print("This is a cubic function")
        return Parabola.__call__(self, x) + self.c3*x**3

#Class for 4th degree polynomials (inhereting information from the superclass Cubic)
class Poly4(Cubic):
    #Constructor declaring all constants for a 4th degree polynomial with inhereted information from Cubic
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4
    #Special method for returning the values of a 4th degree polynomial
    def __call__(self, x):
        print("This is a polynomial of 4-th degree")
        return Cubic.__call__(self, x) + self.c4*x**4

P = Poly4(1,2,3,4,5)
p1 = P(x=2)
print(p1)
