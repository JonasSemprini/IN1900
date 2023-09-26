#Oppgave 5.39
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

def animate_series(fk, M, N, xmin, xmax, ymin, ymax, n ,exact):
    #A) Fjern eksisterende bildefiler
    for file in glob.glob("*.png"):
        os.remove(file)

    #B) Sett opp Plot
    plt.axis([xmin, xmax, ymin, ymax])
    plt.xlabel("x")
    plt.ylabel("S(x;M,N)")

    #C) Definer grid av x-verdier og array s med mellomresultater
    x = np.linspace(xmin, xmax, n)
    s = np.zeros(n)

    #D) Plott punkter fir k=M,....N
    lines = plt.plot(x, fk(x,M))
    for k in range(M, N+1):
        # Legg til et ledd i Taylor-approksimasjonen
        s = s + fk(x,k)
        #Oppdatere plottet
        lines[0].set_ydata(s)
        #Eksakt løsning
        plt.plot(x, exact(x), "g")
        #Oppdatere grafen
        plt.draw()
        #Lagre til fil
        plt.savefig("tmp_%04d.png" %(k-M))
#Eksempel: sin(x)

exact = np.sin
fk = lambda x, k: 1.0 * (-1)**k * x**(2*k+1) / np.math.factorial(2*k*1)
M = 0
N = 40
xmin = 0
xmax = 13*np.pi
ymin = -2
ymax = 2
n = 200
animate_series(fk, M, N, xmin, xmax, ymin, ymax, n ,exact)
