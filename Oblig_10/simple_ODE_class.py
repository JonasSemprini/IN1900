import numpy as np
import matplotlib.pyplot as plt
#Hovedklassen til den numeriske tilnærmingen
class ForwardEuler(object):
    #Konstruktør som deklarer alt av variabler som skal benyttes
    def __init__(self, f, U0, T, n):
        self.f, self.U0, self.T, self.n = f, U0, T, n
        self.dt = T/float(n)
        self.u = np.zeros(n+1) #tom array for u-verdier
        self.t = np.zeros(n+1) #tom-array for t-verdier
    #Løsningsmetode
    def solve(self, T):
        self.u[0] = float(self.U0)
        self.t[0] = float(0)
        for k in range(self.n):
            self.k = k
            self.t[k+1] = self.t[k] + self.dt
            self.u[k+1] = self.advance()
        return self.u, self.t

    def advance(self):
        """Viderefører løsningen et tidssteg."""
        u, dt, f, k, t = \
        self.u, self.dt, self.f, self.k, self.t
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new
#Ny klasse hvor vi implementerer funksjonsutrykket
class Function():
    #Konstruktør som deklarer initialbetingelsen
    def __init__(self,U0):
        self.U0 = U0
    def __call__(self,u,t):
        return u/10
#Eksakt løsning
def func(T):
    return 0.2*np.exp(0.1*T)

T = np.linspace(0,20,5)

metode = Function(0.2) #kaller på klassen med U0
method = ForwardEuler(metode, metode.U0, 20, 5)#kaller på ForwardEuler klassen med funksjonsklassen og de andre betingelsene
u, t = method.solve(20) #T = 20
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(t, u, label='Forward Euler')
plt.plot(T, func(T), label='Exact')
plt.legend()
plt.savefig('class_ODE.png')
plt.show()
"""
Output: python3

"""
