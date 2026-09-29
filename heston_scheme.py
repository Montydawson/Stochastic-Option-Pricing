# Scheme
import numpy as np
import math

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
        m = math.floor((t_c + math.pi) / 2*math.pi)
        G_N = c*math.exp(d*tau) - 1
        n  = math.floor((t_c + np.imag(d)*tau + math.pi) / (2*math.pi))
        lnG = math.log(np.abs(G_N) / np.abs(G_D)) + 1j*(np.angle(G_N) - np.angle(G_D) + 2*math.pi*(n - m))
        D = (lamb - rho*eta*u*1j + d)*(math.exp(d*tau) - 1) / ((eta**2)*(c*math.exp(d*tau) - 1))
        C = (lamb*nu_bar)*((lamb - rho*eta*u*1j+d)*tau - 2*lnG)
        phi = math.exp(C + D*nu_0 + 1j*u*math.log(F))
        return np.real((math.exp(-1j*u*math.log(K))*phi) / (1j*u))
    return f_1



# f_2"
def make_f_2(S, F, r, nu_0, nu_bar, lamb, eta, rho, tau, K):

    def f_2(u):
        d = np.sqrt((rho*eta*u*1j - lamb)**2 + (eta**2)*(u*1j+u**2))
        c = (lamb - rho*eta*u*1j+d) / (lamb - rho*eta*u*1j-d) 
        t_c = np.anlge(c)
        G_D = c - 1 
        m = math.floor((t_c + np.pi) / 2*np.pi)
        emach = np.finfo(np.float64).eps
        #if np.real(d)*tau > -np.log(emach):

        G_N = c*math.exp(d*tau) - 1
        n  = math.floor((t_c + np.imag(d)*tau + np.pi) / (2*np.pi))
        lnG = np.log(np.abs(G_N) / np.abs(G_D)) + 1j*(np.angle(G_N) - np.angle(G_D) + 2*np.pi*(n - m))
        D = (lamb - rho*eta*u*1j + d)*(np.exp(d*tau) - 1) / ((eta**2)*(c*np.exp(d*tau) - 1))
        C = (lamb*nu_bar)*((lamb - rho*eta*u*1j+d)*tau - 2*lnG)
        phi = np.exp(C + D*nu_0 + 1j*u*np.log(F))
        return np.real((np.exp(-1j*u*np.log(K))*phi) / (1j*u))
    return f_2


