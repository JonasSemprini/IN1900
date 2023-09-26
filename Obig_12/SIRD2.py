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

class ProblemSIRD:
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

    def __init__(self,region, S0, I0, R0, D0, region_j phi, lamb):
        Region.__init__(self, region, I0, R0, D0)
        self.region_j = region_j
        self.phi = phi*(np.pi/180)
        self.lamb = lamb*(np.pi/180)

    def distance(self, other):
        phi = self.phi
        lamb = self.lamb
        dOmega = np.arccos((np.sin(phi_j) * np.sin(phi_i)) + (np.cos(phi_j)*np.cos(phi_i) * np.cos(abs(lamb_i - lamb_j))))
        dis = 65*(dOmgega)

        if dis > 1:
            return 1
        else:
            pass

class ProblemInteraction(ProblemSIRD):
    def __init__(self, region, alpha, beta, gamma, region_name):
        ProblemSIRD.__init__(self, region, alpha, beta, gamma)
        self.region_name = region_name

    def get_population(self):
        self.total_population = self.region + self.region_j

    def set_initial_condition(self):

    def __call__(self, u, t):
    n = len(self.region)
    # create a nested: SIRD_list[i] = [S_i, I_i, R_i, D_i]: SIRD_list = [u[i:i+4] for i in range(0, len(u), 4)]
    # crate a list containing all the I(t)-values:
    I_list = ...
    derivative = []
    for i in range(n):
        S, I, R, D = SIRD_list[i] dS = 0
        for j in range(n):
            I_other = I_list[j]
            dS += ...
            # calculate dI, dR and dD
            # put the values in the end of derivative
    return derivative

    def solution(self, u, t):
        n = len(t)
        n_reg = len(self.region) self.t = t
        self.S = np.zeros(n) self.I = ...
        SIRD_list = [u[:, i:i+4] for i in range(0, n_reg*4, 4)]
        for part, SIRD in zip(self.region, SIRD_list):
            part.set_SIRD_values(SIRD, t) self.S += ...
