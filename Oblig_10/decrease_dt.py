import numpy as np
import matplotlib.pyplot as plt

class ForwardEuler:
    """
    Class attributes:
    t: array med tidsverdier
    u: array med løsningsverdier (ved n time_points)
    k: tallsteget til den nyeste løsningen
    f: kallbart objekt f(u,t)
    dt: tidssteg (antatt konstant)
    """
    #Konstruktør som lar oss kalle på klassen med funksjonen f
    def __init__(self, f):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))
        self.f = f

        #Initialverdien U[0]
    def set_initial_condition(self, U0):
        self.U0 = float(U0)

        #Metode for å løse sekvensen u[k] og t[k]
    def solve(self, time_points):
        """Kalkulerer u og t-verdier ved hjelp av time_points."""
        self.t = np.asarray(time_points)
        self.u = np.zeros(len(time_points))
        # Anta at self.t[0] svarer til self.U0
        self.u[0] = self.U0
        #For-løkke som kalkulerer s[k+1]
        for k in range(len(self.t)-1):
            self.k = k
            self.u[k+1] = self.advance()
        return self.t, self.u

    #Metode som simulerer differentsialligningen
    def advance(self):
        """
        Viderfører løsning med neste tidssteg.
        Prøver ved hjelp av denne metoden og simulere en løsning som er,
        så lik som mulig den eksakte løsningen
        """
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new
#Utrykket for differentsialligningen vi ønsker å simulere
def f(u,t):
    return np.cos(6*t)/(1+t+u)

#Kaller på klassen ForwardEuler
metode = ForwardEuler(f)
metode.set_initial_condition(U0 = 0) #initialbetingelse
n = [20,30,35,40,50,100,1000,10000] #tidssteg
#for-løkke som plotter simuleringen ved de n-tidsstegene
for i in range(len(n)):
    time_points = np.linspace(0, 10, n[i])
    u,t  = metode.solve(time_points)
    plt.plot(u,t, label=n[i])
    plt.legend()
plt.savefig('decrease.png')
plt.show()

"""
Output: python3 decrease_dt.py
Outputet i denne oppgaven er vist i bildet decrease png,
hvor alle plottene svarer til de forskjellige tidsstegene vist med fargekoder
"""
