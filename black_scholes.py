# Calculate Black-Scholes call price given parameters
import numpy as np
from scipy.stats import Normal


def black_scholes(S, K, tau, r, sigma, q = 0):
    d1 = ((np.log(S / K)) + tau*(r - q + ((sigma**2) / 2))) / (sigma*np.sqrt(tau))
    d2 = d1 - sigma*np.sqrt(tau)
    V = S*np.exp(-q*tau)*Normal(d1) - K*np.exp(-r*tau)*Normal(d2)

    return V
