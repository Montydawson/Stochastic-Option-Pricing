# Calculate Black-Scholes call price given parameters
import numpy as np
from scipy.stats import norm


def black_scholes_price(S, K, tau, r, sigma, q = 0):
    d1 = ((np.log(S / K)) + tau*(r - q + ((sigma**2) / 2))) / (sigma*np.sqrt(tau))
    d2 = d1 - sigma*np.sqrt(tau)
    V = S*np.exp(-q*tau)*norm.cdf(d1) - K*np.exp(-r*tau)*norm.cdf(d2)

    return V
