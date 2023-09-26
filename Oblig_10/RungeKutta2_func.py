import numpy as np
import matplotlib.pyplot as plt

#Hovedfunksjonen som skal kalkulere differentsialligningen
def runge_2(f, U0, T, n):
    u = np.zeros(n+1) #tom array for u-verdier
    t = np.zeros(n+1) #tom array for u-verdier
    t[0] = 0 #t0
    u[0] = U0 #u0
    dt = T/float(n) #h = b-a/n
    #For-loop som legger til t-verdier i listen og regner u[k]-sekvensen
    for k in range(n):
        t[k+1] = t[k] + dt
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)
        u[k+1] = u[k] + K2
    return u, t

T = np.linspace(0,20,40)
#simulert løsning
def f(u,t):
    return u/10
#Eksakt løsning
def func(T):
    return 0.2*np.exp(0.1*T)

u, t = runge_2(f, 0.2, 20, 5) #plot 1
u1, t1 = runge_2(f, 0.2, 20, 10) #plot 2
u2, t2 = runge_2(f, 0.2, 20, 35) #plot 3
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(t, u, label='5-steps')
plt.plot(t1, u1, label='20-steps')
plt.plot(t2, u2, label='40-steps')
plt.plot(T, func(T), label='Exact')
plt.legend()
plt.savefig('runge_kutta_2.png')
plt.show()

"""
Output: python3 RungeKutta2_func.py

"""
