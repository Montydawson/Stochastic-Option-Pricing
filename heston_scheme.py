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

# f_1:
def make_f_1(S, F, r, nu_0, nu_bar, lamb, eta, rho, tau, K):

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


# f_2:
def make_f_2(S, F, r, nu_0, nu_bar, lamb, eta, rho, tau, K):

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

# integration endpoint limits:
C_inf = ((np.sqrt(1 - (rho**2)))*(nu_0 + lamb*nu_bar*tau)) / eta
a = (F - K) / 2

if lamb == rho*eta:
    imcdashm = (lamb*nu_bar*tau**2) / 4
    imddashm = tau / 2

else:
    imcdashm = (np.exp((rho*eta - lamb)*tau)*lamb*nu_bar + lamb*nu_bar*((lamb - rho*eta)*tau - 1)) / (2*((lamb - rho*eta)**2))
    imddashm = (1 - np.exp(-(lamb - rho*eta)*tau)) / (2*(lamb - rho*eta))

imcdashz = -( (np.exp(-lamb*tau)*lamb*nu_bar + lamb*nu_bar*(lamb*tau - 1)) / (2*(lamb**2)) )
imddashz = -( (1 - np.exp(-((lamb*tau) / 2))) / (2*lamb) )

# Slight 'typo' in kahl and jackel disagreeing with derivation of limit, this is correct:
imddashz = -(1 - np.exp(-lamb * tau)) / (2 * lamb)


b =  (F - K) / 2  + (F*(np.log(F / K) + imcdashm + imddashm*nu_0) - K*(np.log(F / K) + imcdashz + imddashz*nu_0)) / (np.pi*C_inf)

# quadrature


from scipy.special import roots_jacobi, eval_legendre

def gauss_lobatto(N):
    interior, _ = roots_jacobi(N - 1, 1, 1)
    nodes = np.concatenate(([-1.0], interior, [1.0]))

    weights = np.empty(N + 1)
    weights[0] = weights[-1] = 2 / (N * (N + 1))

    for i in range(1, N):
        weights[i] = 2 / (N * (N + 1) * eval_legendre(N, nodes[i])**2)

    return nodes, weights

# integr

f_1 = make_f_1(S, F, r, nu_0, nu_bar, lamb, eta, rho, tau, K)
f_2 = make_f_2(S, F, r, nu_0, nu_bar, lamb, eta, rho, tau, K)

def y(x):
    if x == 0:
        return a
    elif x == 1:
        return b
    else:
        u = -np.log(x) / C_inf
        return (F - K) / 2 + (F * f_1(u) - K * f_2(u)) / (x * np.pi * C_inf)


# Gauss-Lobatto evaluationd

def heston_price(N):
    nodes, weights = gauss_lobatto(N)

    x = (nodes + 1) / 2
    x[0] = 0.0
    x[-1] = 1.0

    y_values = np.array([y(x_i) for x_i in x])
    integral = 0.5 * np.sum(weights * y_values)

    return np.exp(-r * tau) * integral
