"""
NB!:

Hele denn oppgaven er basert på programeringskode,
som finnes i boken tilhørende kurset. Vi blir i oppgaven,
spurt om å benytte oss av nettopp denne koden
"""

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
    #Konstruktør som lar oss kalle på funksjonen f vi ønsker å implementere
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

        for k in range(len(self.t)-1):
            self.k = k
            self.u[k+1] = self.advance()
        return self.t, self.u

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

class midpoint(ForwardEuler):
#solve metode som i ForwardEuler lager sekvernser av t[k] og u[k]
    def solve(self, time_points):
        self.t = np.asarray(time_points)
        self.u = np.zeros(len(time_points))
        self.u[0] = self.U0

        for k in range(len(self.t)-1):
            self.k = k
            self.u[k+1] = self.advance() #kaller på advance2 som svarer til midtpunktsmetoden
        return self.t, self.u

    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        """
        Deklarer her x[k+1/2], og bruker x[k+1/2](u_new_half)
        til å utrykke x[k+1](u_new)
        """
        u_new_half = u[k] + (dt/2) * f(t[k], u[k])
        u_new = u[k] + dt * f(u_new_half, t[k] + dt/2)
        return u_new
#Simulert versjon av differentsialligningen
def f(u,t):
    return np.cos(t) - t* np.sin(t)
#Eksakte løsningen
def f1(u):
    return u*np.cos(u) - 5*np.cos(-5)

T = np.linspace(-5, 5, 20) #array med verdier tilhørende den eksakte løsningen
plt.plot(T, f1(T), label='exact')#plotter den eksakte løsningen
metode = ForwardEuler(f) #kaller på klassen med funksjonen f
time_points = np.linspace(-5, 5, 20) #array med t-verdier
metode.set_initial_condition(-5*np.cos(-5)) #initialbetingelse U0
t1, u1 = metode.solve(time_points)
plt.plot(t1, u1, label='Forward Euler')

metode2 = midpoint(f) #kaller på midpoint klassen med funksjonen f
metode2.set_initial_condition(-5*np.cos(-5))
t2, u2 = metode2.solve(time_points)
plt.plot(t2, u2, label='Euler Midpoint')
plt.legend()
plt.savefig("Midpoint.png")
plt.show()

"""
Output: python3 Midpoint.py

"""
