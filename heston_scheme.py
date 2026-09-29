# Scheme
import numpy as np
from math import *

# Parameters:

S = 1
F = 1
r = 0
nu_0 = 0.16
nu_bar = 0.16
lamb = 1
eta = 2
rho = -0.8
tau = 10
K = 2

# Evaluate f_1:

def make_f_1(S, F, r, nu_0, nu_bar, lamb, eta, rho, tau, K):

    def f_1(u):
        d = np.sqrt((rho*eta*u*1j - lamb)**2 + (eta**2)*(u*1j+u**2))
        c = (lamb - rho*eta*u*1j+d) / (lamb - rho*eta*u*1j-d) 
        t_c = np.anlge(c)
        G_D = c - 1
        


