import matplotlib.pyplot as plt
import numpy as np

def inflation(): #main function
    N = 60 #years
    p = 1.05 #interest
    q = 3
    F = 10000 #fortune
    I = 3

    x = np.zeros(N+1) #empty array with N + 1 zeros
    x[0] = F #setting the first x-value to F
    c = np.zeros(N+1) #empty array with N +1 zeros
    c[0] = (p*q*F)/(10**4) #setting the

    #for loop calculating the cn sequence and the xn sequence

    for i in range(1, N+1):
        x[i] = x[i-1] + (p/100)*x[i-1] - c[i-1]
        c[i-1] = x[i-1] + (p/100)*x[i-1] - x[i] #calculating the c(n-1) sequence following the xn sequence
        c[i] = c[i-1] + c[i-1]*(I/100)
        plt.plot(i, x[i],  "ro") #plotting the xn sequence with i values along the x-axis and fortune along the y
    plt.xlabel("Years")
    plt.ylabel("Fortune")
    plt.savefig("fortune_and_inflation.png")
    plt.show()

inflation()

"""
Output: python3  fortune_and_inflation1.py
Graph shown in the png. The excercise does not ask to represent any fixed values,
but the solution is programmed of the same operating procedure.
"""
