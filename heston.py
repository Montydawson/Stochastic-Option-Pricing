# given parameters, find call price using the heston model:

import numpy as np
import math

# following kahl and jackel:
# make f_1 and f_2:

def make_f_1(F, K, lamb, nu_bar, eta, tau, nu_0, rho):

    def f_1(u):
        v = u - 1j
        d = np.sqrt((rho*eta*v*1j - lamb)**2 + (eta**2)*(v*1j+v**2))
        c = (lamb - rho*eta*v*1j+d) / (lamb - rho*eta*v*1j-d) 
        t_c = np.angle(c)
        G_D = c - 1 
        m = math.floor((t_c + np.pi) / (2*np.pi))
        n  = math.floor((t_c + np.imag(d)*tau + np.pi) / (2*np.pi))
        emach = np.finfo(np.float64).eps

        if np.real(d)*tau > -np.log(emach):
            lnG = np.log(np.abs(c)) + np.real(d)*tau - np.log(np.abs(G_D)) + 1j*(np.angle(c) + np.imag(d)*tau - np.angle(G_D) - 2*np.pi*m)
            D = (lamb - rho*eta*v*1j + d) / ((eta**2)*(c))

        else:
            G_N = c*np.exp(d*tau) - 1
            lnG = np.log(np.abs(G_N) / np.abs(G_D)) + 1j*(np.angle(G_N) - np.angle(G_D) + 2*np.pi*(n - m))
            D = (lamb - rho*eta*v*1j + d)*(np.exp(d*tau) - 1) / ((eta**2)*(c*np.exp(d*tau) - 1))
        
        C = (lamb*nu_bar)*((lamb - rho*eta*v*1j+d)*tau - 2*lnG) / (eta**2)
        phi = np.exp(C + D*nu_0 + 1j*v*np.log(F))
        return np.real((np.exp(-1j*u*np.log(K))*phi) / (1j*u*F))
    
    return f_1



def make_f_2(F, K, lamb, nu_bar, eta, tau, nu_0, rho):

    def f_2(u):
        d = np.sqrt((rho*eta*u*1j - lamb)**2 + (eta**2)*(u*1j+u**2))
        c = (lamb - rho*eta*u*1j+d) / (lamb - rho*eta*u*1j-d) 
        t_c = np.angle(c)
        G_D = c - 1 
        m = math.floor((t_c + np.pi) / (2*np.pi))
        n  = math.floor((t_c + np.imag(d)*tau + np.pi) / (2*np.pi))
        emach = np.finfo(np.float64).eps

        if np.real(d)*tau > -np.log(emach):
            lnG = np.log(np.abs(c)) + np.real(d)*tau - np.log(np.abs(G_D)) + 1j*(np.angle(c) + np.imag(d)*tau - np.angle(G_D) - 2*np.pi*m)
            D = (lamb - rho*eta*u*1j + d) / ((eta**2)*(c))

        else:
            G_N = c*np.exp(d*tau) - 1
            lnG = np.log(np.abs(G_N) / np.abs(G_D)) + 1j*(np.angle(G_N) - np.angle(G_D) + 2*np.pi*(n - m))
            D = (lamb - rho*eta*u*1j + d)*(np.exp(d*tau) - 1) / ((eta**2)*(c*np.exp(d*tau) - 1))
        
        C = (lamb*nu_bar)*((lamb - rho*eta*u*1j+d)*tau - 2*lnG) / (eta**2)
        phi = np.exp(C + D*nu_0 + 1j*u*np.log(F))
        return np.real((np.exp(-1j*u*np.log(K))*phi) / (1j*u))
    
    return f_2

def make_y(F, K, lamb, nu_bar, eta, tau, nu_0, rho):

    def y(x):
        # integration endpoint limits:
        C_inf = ((np.sqrt(1 - (rho**2)))*(nu_0 + lamb*nu_bar*tau)) / eta
        a = (F - K) / 2


        imcdashm = 1
        imddashm = 1
        if lamb == rho*eta:
            imcdashm = (lamb*nu_bar*tau**2) / 4
            imddashm = tau / 2

        else:
            imcdashm = (np.exp((rho*eta - lamb)*tau)*lamb*nu_bar + lamb*nu_bar*((lamb - rho*eta)*tau - 1)) / (2*((lamb - rho*eta)**2))
            imddashm = (1 - np.exp(-(lamb - rho*eta)*tau)) / (2*(lamb - rho*eta))

        imcdashz = -( (np.exp(-lamb*tau)*lamb*nu_bar + lamb*nu_bar*(lamb*tau - 1)) / (2*(lamb**2)) )
        # Slight 'typo' in kahl and jackel disagreeing with derivation of limit, this is correct:
        imddashz = -(1 - np.exp(-lamb * tau)) / (2 * lamb)

        b =  (F - K) / 2  + (F*(np.log(F / K) + imcdashm + imddashm*nu_0) - K*(np.log(F / K) + imcdashz + imddashz*nu_0)) / (np.pi*C_inf)
        