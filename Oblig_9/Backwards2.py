import numpy as np
from math import exp
class Diff: # Class for initializing the method of differentiating
    #Constructor which declares the function f(x) = e^-t and the constant h
    def __init__(self, f, h):
        self.f = f
        self.h = float(h)
#Class for utilizing a method of differentiating a given function
class Backwards1(Diff):
#Special method returning the backwards method of differentiating a function
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x) - f(x-h)) / (h) #the main technique
#A second class for utilizing a different method of differentiating a given function
class Backwards(Diff):
    #Special method for returning the second technique of differentiating
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x - 2*h) - 4*f(x-h) + 3*f(x)) / (2*h) #main technique 2
k = 14
t = 0
#for-loop calculating the presicion of the differentiastion in an intervall [0,14]
for x in range(0, k+1):
    h = 2**-x #h-value
    Back = Backwards(lambda t:exp(-t), h) #calling on backwards 2
    Back1 = Backwards1(lambda t:exp(-t), h) #calling on backwards 1
    print(f"Number: {x}", "Back 2", Back(t), "Back 1", Back1(t))
"""
Output: python3 Backwards2.py
Number: 0 Back 2 -0.24203560745276498 Back 1 -1.718281828459045
Number: 1 Back 2 -0.8766032543414677 Back 1 -1.2974425414002564
Number: 2 Back 2 -0.9747607921016748 Back 1 -1.1361016667509656
Number: 3 Back 2 -0.9942735823182556 Back 1 -1.0651876245346106
Number: 4 Back 2 -0.9986350608368895 Back 1 -1.0319113426857491
Number: 5 Back 2 -0.9996667372568311 Back 1 -1.0157890399712883
Number: 6 Back 2 -0.9999176591244918 Back 1 -1.0078533495478865
Number: 7 Back 2 -0.9999795353028276 Back 1 -1.00391644242535
Number: 8 Back 2 -0.9999948988085521 Back 1 -1.001955670616951
Number: 9 Back 2 -0.9999987265698564 Back 1 -1.0009771985934321
Number: 10 Back 2 -0.999999681875579 Back 1 -1.0004884402344487
Number: 11 Back 2 -0.9999999204983396 Back 1 -1.0002441803662805
Number: 12 Back 2 -0.9999999801275408 Back 1 -1.0001220802469106
Number: 13 Back 2 -0.999999995030521 Back 1 -1.0000610376391705
Number: 14 Back 2 -0.9999999987630872 Back 1 -1.0000305182002194
"""
