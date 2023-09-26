"""
NB!
I denne oppgaven tar vi utgangspunkt i en kode oppgitt i oppgaven fra boken,
tilhørende dette kurset (ODESolver)
"""
import numpy as np
import matplotlib.pyplot as plt
#Hovedklassen som skal arves fra når andre klasser lagees
class ODESolver(object):
    def __init__(self, f):
        self.f = lambda u, t: np.asarray(f(u, t), float)

    def advance(self):
        """Viderefør løsningen et tidssteg."""
        raise NotImplementedError

    #Setter initialbetingelse tilsvarende løsningsutrykket
    def set_initial_condition(self, U0):
        if isinstance(U0, (float,int)): # skalar ODE
            self.neq = 1
            U0 = float(U0)
        else:
            U0 = np.asarray(U0)
            self.neq = U0.size
        self.U0 = U0
    #Løsnings-metode som lager u[k] og t[k] sekvensen
    def solve(self, time_points, terminate=None):
        if terminate is None:
            terminate = lambda u, t, step_no: False

        self.t = np.asarray(time_points)
        n = self.t.size

        if self.neq == 1: # scalar ODEs
            self.u = np.zeros(n)
        else:
            self.u = np.zeros((n,self.neq))

        self.u[0] = self.U0

        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
            if terminate(self.u, self.t, self.k+1):
                break
        return self.u[:k+2], self.t[:k+2]
#sub-class som arver informasjon fra ODESolver slik at vi kan kalkulere funksjonen f
class ForwardEuler(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new

#Funksjonsutrykket vi ønsker å kalkulere.
def test(u,t):
    return u/10
#Eksakt løsning
def func(time_points):
    return 0.2*np.exp(0.1*time_points)

time_points = np.linspace(0, 20, 5) #array for t-verdier

metode = ForwardEuler(test) #kaller på klassen med funksjonen test

metode.set_initial_condition(U0=0.2)

u1,t1 = metode.solve(time_points)

plt.xlabel('X')

plt.ylabel('Y')
plt.plot(t1, u1, label='Forward Euler')
plt.plot(time_points, func(time_points), label='Exact')
plt.legend()
plt.savefig("class_hier.png")
plt.show()

"""
Output: python3 simple_ODE_class_ODESolver.py
Outputet i oppgaven vises på bildet class_hier.png hvor både den numeriske og den eksakte løsningen er plottet sammen
"""
