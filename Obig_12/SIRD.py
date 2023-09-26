import numpy as np
import matplotlib as plt
from ODESolver import *
from bjorgvin import *

S0 = 7000
I0 = 30
R0 = 0
D0 = 0
alpha = 6.5*(10**(-5))
beta = 0.1/4
gamma = 0.9/4

class Region:
    def __init__(self, region, S0, I0, R0, D0):
        self.region = region
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0
        self.D0 = D0
        self.population = self.S0 + self.I0 + self.R0 + self.D0

    def set_SIRD_values(self, u, t):
        self.S = u[:,0]
        self.I = u[:,1]
        self.R = u[:,2]
        self.D = u[:,3]
        self.t = t
        Vlues = self.S, self.I, self.R, self.D
        return Vlues

    def plot(self, x_label):
        plt.ylabel = 'Population'
        x = x_label
        plt.plot(self.t, self.S, label='Susceptible', color='Blue')
        plt.plot(self.t, self.I, label='Infected', color='purple')
        plt.plot(self.t, self.R, label='Recovered', color='red')
        plt.plot(self.t, self.D, label='Deceased', color='green')
Bjorgvin = Region('Vestlandet', S0, I0, R0, D0)

class Problem:
    def __init__(self, region, alpha, beta, gamma):
        self.region = region
        self.beta = beta
        self.gamma = gamma
        if isinstance(alpha, (float, int)): # number?
            self.alpha = lambda t: alpha
        elif callable(alpha):
            self.alpha = alpha
        self.set_initial_condition()

    def set_initial_condition(self):
        self.set_initial_condition = [self.region.S0, self.region.I0, self.region.R0, self.region.D0 ]

    def get_population(self):
        return self.region(self.population)

    def solution(self, u, t):
        self.region.set_SIRD_values(u,t)

    def __call__(self, u, t):
        alpha = self.alpha(t)
        S, I, R, D = u[0], u[1], u[2], u[3]
        dS = (-alpha*S)*(I)
        dI = (alpha*S*I) - (beta*I) - (gamma*I)
        dR = beta*I
        dD = gamma*I
        return np.array([dS, dI, dR, dD])

problem = Problem(Bjorgvin, alpha, beta, gamma)

class SolverSIRD:
    def __init__(self, problem):
        self.problem = problem
        self.total_population = self.problem.get_population

    def Terminate(self,u,t,step_no):
        tol = 1
        co = u[0][0] + u[0][1] + u[0][3] + u[0][3]
        step = u[step_no][0] + u[step_no][1] + u[step_no][2] + u[step_no][3]
        return abs(co - step) > tol

    def solve(self, method=RungeKutta4):
        solver= method(self.problem)
        solver.set_initial_condition(self.problem.set_initial_condition)
        time = np.linspace(0, 63, 10000)
        u,t = solver.solve(time, self.Terminate)

        self.problem.solution(u,t)

class RegionInteraction(Region):
    def __init__(self, latitude, longitude):

solver = SolverSIRD(problem)
solver.solve()
Bjorgvin.plot('Endelig')
plt.legend()
plt.show()
