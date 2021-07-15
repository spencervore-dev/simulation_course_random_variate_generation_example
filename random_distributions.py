# A basic library of random distribution generation functions

# More info about what is already built into the basic python 
# random library that comes with base python

from random import random
import numpy as np
from datetime import datetime


class lcg_class:
    """
    The L'Ecuyer linear congruential generator to potentially be used in the following random
    variate generators
    """

    # Note that default seed take system date and time down to the milliseconds 
    # and converts it into an integer. This way each distribution can be different.
    def __init__(self, a=16807, c=0, mod=(2**31-1), seed=int(datetime.now().strftime("%Y%m%d%H%M%S%f"))):
        """
        Initialize lcg generator with appropriate constants
        """
        self.a = a
        self.c = c
        self.mod = mod
        self.x_prev = seed

    def rand(self):
        """
        Get Random number from LCG
        """
        a = self.a
        x_prev = self.x_prev
        c = self.c
        mod = self.mod

        x = (a*x_prev + c) % mod

        # Update previous x with new x - saved as variable in the class
        self.x_prev = x
        return float(x)/float(mod)

# Now create (i.e. instantiate) the lcg object
lcg = lcg_class()

def unif(a=0, b=1):
    """
    Generate a uniform distribution between a and b
    """

    U = lcg.rand()
    return (U+ a/(b-a))*(b-a)

def bern(p):
    """
    Generate a bernoulli random variate from a standard uniform distribution
    """

    U = lcg.rand()
    return int(U <= p)

def binom(n, p):
    """
    Generate a binomial random variate that returns the number of successes in n trials,
    with p probability of success, from a standard uniform distribution.
    """
    trials = []
    for _ in range(n):
        U = lcg.rand()
        trials.append(int(U <= p))
    return np.sum(trials)

def norm(mu, sigma, trig="cos"):
    """
    Generate a normal random variates with mean, mu, and standard deviation, sigma,
    using the Box-Muller transformation from a standard uniform distribution
    """
    U1 = lcg.rand()
    U2 = lcg.rand()

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
    U = lcg.rand()

    if U < 0.5:
        return np.sqrt(U*(c - a)*(b - a)) + a
    else:
        return c - np.sqrt((1 - U)*(c - a)*(c - b))

def expo(lamb):
    """
    Generate an exponential random variate with l = lambda, using U from a standard uniform
    distribution.
    """
    U = lcg.rand()

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
    U = lcg.rand()

    return (1/lamb)*(-np.log(U))**(1/beta)
