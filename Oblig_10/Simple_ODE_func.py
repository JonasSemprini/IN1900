import numpy as np
import matplotlib.pyplot as plt
#Hovedfunksjon for å kalkuere den numeriske tilnærmingen til funksjonen f
def ForwardEuler(f, U0, T, n):
    t = np.zeros(n+1)#tom array med t-verdier
    u = np.zeros(n+1)#tom array med u-verdier
    u[0] = 0.2 #u0
    t[0] = 0 #t0
    dt = T/float(n) #h = b-a/n
    #for løkke som kalkuler t[k] og u[k] sekvensen
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t
#den simulerte løsningsfunksjonen
def f(u,t):
    return u/10
#Den eksakte løsningen
def f2(T):
    return 0.2*np.exp(0.1*T)

T = np.linspace(0, 20, 5)
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(T, f2(T), label='Exact')
u, t = ForwardEuler(f, 0.2, 20, 5) #kaller på funksjonen med de gitte betingelsene
plt.plot(t, u, label='Forward Euler')
plt.legend()
plt.savefig('Simple_ODE_func')
plt.show()
