# A basic library of random distribution generation functions

# More info about what is already built into the basic python 
# random library that comes with base python

from random import random
import numpy as np

def lcg(a=16807, c=0, mod=(2**31)-1, seed=12567):
    """
    The L'Ecuyer linear congruential generator to potentially be used in the following random 
    variate generators
    """
    x = (a*seed + c) % mod
    return x/mod

def unif(a, b):
    """
    Generate a uniform distribution between a and b
    """
    # ^^ The above comment is called a docstring. If it's
    # immediately below the function definition, it can
    # show up in python help and you can write comments
    # that describe what the function does.

    U = random()
    return (U+ a/(b-a))*(b-a)

def bern(p):
    """
    Generate a bernoulli random variate from a standard uniform distribution
    """
    
    U = unif(0, 1)
    return int(U <= p)

def binom(n, p):
    """
    Generate a binomial random variate that returns the number of successes in n trials, 
    with p probability of success, from a standard uniform distribution.
    """
    trials = []
    for _ in range(n):
        U = unif(0, 1)
        trials.append(int(U <= p))
    return np.sum(trials)
    
def norm(mu, sigma, trig="cos"):
    """
    Generate a normal random variates with mean, mu, and standard deviation, sigma, 
    using the Box-Muller transformation from a standard uniform distribution
    """
    U1 = unif(0, 1)
    U2 = unif(0, 1)
    
    if trig == "sin":
        z = np.sqrt(-2*np.log(U1))*np.sin(2*np.pi*U2)
    else:
        z = np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2)
    
    return mu + sigma*z

def tria(a, c):
    """
    Generate a triangualar random variate with min=a, max=c, and most likely, b, being halfway
    between a and c. The random variate is found using a standard uniform distribution.
    """
    b = (a+c) / 2
    U = lcg()
    
    if U < 0.5:
        return np.sqrt(U*(c - a)*(b - a)) + a
    else:
        return c - np.sqrt((1 - U)*(c - a)*(c - b))
    
def expo(lamb):
    """
    Generate an exponential random variate with l = lambda, using U from a standard uniform
    distribution.
    """
    U = unif(0,1)
    
    return -(1/lamb)*np.log(U)
    
def poisson(lamb):
    """
    Generate a poisson random variate with l = lambda, using U from a standard uniform distribution
    and the exponential distribution as the interarrival times. n is the  number before thesum of 
    exponential random variates is greater than 1.
    """
    sum_expo = 0
    n = -1
    
    while (sum_expo < 1):
        e = expo(lamb)
        sum_expo += e
        n += 1
    return n
    
def weibull(lamb, beta):
    """
    Generate a weibull random variate with lambda = lamb and beta, using a standard uniform
    distribution.
    """
    U = unif(0,1)
    
    return (1/lamb)*(-np.log(U))^(1/beta)
