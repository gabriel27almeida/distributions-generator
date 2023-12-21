import numpy as np
from math import exp

def normal_distr(n, sigmas):
    """Returns symmetric normal distribution on n qubit register"""
    mu = 2**(n-1)-0.5
    sigma = 2**(n-1)/sigmas
    prob = np.array([exp(-0.5*((x-mu)/sigma)**2) for x in range(2**n)])
    prob /= np.sum(prob)
    return prob 

def maxwell_boltzmann(n, sigmas):
    #"""Returns symmetric normal distribution on n qubit register"""
    sigma = 2**(n-1)/sigmas
    prob = np.array([x*x*exp(-0.5*((x/sigma)**2)) for x in range(2**n)])
    prob /= np.sum(prob)
    return prob 

