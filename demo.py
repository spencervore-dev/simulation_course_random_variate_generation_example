# This script is a demostration / test of all the different
# random distribution generation functions in our library.

from random import weibullvariate
from numpy import random
from scipy.stats import kruskal
from scipy.stats import ks_2samp # Kolmogorov-Smirnov test
import numpy as np


# Import the other script where we define all the functions
import random_distributions as rds

obs = 100_000
alpha = 0.001 #Use low alpha as sample size is large


# Demo each distribution
def stat_conclusion(p, alpha):
    '''Returns conlcusion of statistical test based on test stat and alpha'''
    if p > alpha:
        return 'ACCEPT'
    else:
        return 'REJECT'


# Perform Kruskal Wallis test - this is a nonparametric test
# that will check if the two sample sets come from the same
# distribution. The goal is to see if our custom random
# number library has the same statistical properties
# as an "off the shelf" library.

# More info about the Kruskal Wallis test we are using is here:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html

# More info about the Kolmogorov-Smirnov test we are using is here
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_2samp.html

# More info about the various numpy random distribution that we are 
# testing against is available here:
# https://numpy.org/doc/1.16/reference/routines.random.html

# Good resource about which non-parametric tests to use in what situation
# https://www.mit.edu/~6.s085/notes/lecture5.pdf


# Info
print("\nThis script will print the results from a series of non-parametric tests, mostly ")
print("to compare our library of random distributions from scratch to the numpy distribution ")
print("library to demonstrate that the random number we are producing are correct.")
print(f"Each distribution will have {obs} samples by default and will be tested ")
print(f"at the alpha={alpha} level.\n\n")
print("---------------------------------------------\n\n")

# Lets see what happens if we pass in different distributions
# Demo how the Kruskal Wallis test works to make sure we are using it right
a = 3
b = 6
b2 = 9

np_unifs = random.uniform(a, b, obs)
np_unifs2 = random.uniform(a, b2, obs)
H, p_val = kruskal(np_unifs, np_unifs2)

print("DEMO of Kruskal-Wallis test with different distributions - This should REJECT.")
print(f"KW test results on two different unif distributions, unif({a}, {b}) and unif({a}, {b2}) from numpy.")
print(f"H test statistic is: {H}")
print(f"p-value is: {p_val}")
conclusion = stat_conclusion(p_val, alpha)
print(f"{conclusion} the null hypothesis that these distributions have the same median.")
print()

test_stat, p_val2 = ks_2samp(np_unifs, np_unifs2)
print("DEMO of Kolmogorov-Smirnov test with different distributions - This should REJECT.")
print(f"KS test results on two different unif distributions, unif({a}, {b}) and unif({a}, {b2}) from numpy.")
print(f"Test statistic is: {test_stat}")
print(f"p-value is: {p_val2}")
conclusion = stat_conclusion(p_val2, alpha)
print(f"{conclusion} the null hypothesis that the distributions are the same.")
print()
print("---------------------------------------------\n\n")

# Lets see what happens if we use two completely different distributions
# with the same median. This breaks the KW test and shows why we need KS 

mu = 0
sig = 1
a = -10
b = 10
np_norm = random.normal(loc=mu, scale=sig, size=obs)
np_unifs3 = random.uniform(a, b, obs)

H, p_val = kruskal(np_norm, np_unifs3)
print("DEMO of Kruskal-Wallis test with different distributions - "
"\n\tThis should ACCEPT because these distributions have the same median.")
print(f"KW test result comparing a norm({mu}, {sig}) with a unif({a}, {b}) "
f"\n\tfrom numpy:")
print(f"H test statistic is: {H}")
print(f"p-value is: {p_val}")
print(f"median of norm({mu}, {sig}) is {np.median(np_norm)}")
print(f"median of unif({a}, {b}) is {np.median(np_unifs3)}")
conclusion = stat_conclusion(p_val, alpha)
print(f"{conclusion} the null hypothesis that these distributions have the same median.")
print()

test_stat, pval2 = ks_2samp(np_norm, np_unifs3)
print("DEMO of Kolmogorov-Smirnov test with different distributions - "
"\n\tThis should REJECT even though these distributions have the same median.")
print(f"KS test result comparing a norm({mu}, {sig}) with a unif({a}, {b}) "
"\n\tfrom numpy:")
print(f"Test statistic is: {test_stat}")
print(f"p-value is: {p_val2}")
conclusion = stat_conclusion(p_val2, alpha)
print(f"{conclusion} the null hypothesis that the distributions are the same.")
print()

print("After testing, we will only use the KS test going forward to test these "
"\n\tdistrubtions since it's more general and doesn't have this median limitation.")
print("---------------------------------------------\n\n")


# Now let's start testing our actual functions

# Uniform
a = 3
b = 6

our_unifs = [rds.unif(a, b) for _ in range(obs)]
np_unifs = random.uniform(a, b, obs)
test_stat, p_val = ks_2samp(our_unifs, np_unifs)

print("UNIFORM DISTRIBUTION")
print(f"Kolmogorov-Smirnov test result comparing our unif({a}, {b}) distribution to numpy's:")
print(f"Test statistic is: {test_stat}")
print(f"p-value is: {p_val}")
conclusion = stat_conclusion(p_val, alpha)
print(f"{conclusion} the null hypothesis that the distributions are the same.")
print()

# Bernouilli - Since this is only 0 or 1, not sure if KS test will work well. 
# This distribution also doesn't exist in numpy random. However, since this 
# function is used to generate the binomeal distribution shown next, if that's
# working we can probably safely assume the bernoulli function is working as 
# well.


# Binomial
n = 10
p = 0.3

our_binoms = [rds.binom(n, p) for _ in range(obs)]
np_binoms = random.binomial(n, p, obs)
test_stat, p_val = ks_2samp(our_binoms, np_binoms)

print("BINOMIAL DISTRIBUTION")
print(f"Kolmogorov-Smirnov test result comparing our binom({n}, {p}) distribution to numpy's:")
print(f"Test statistic is: {test_stat}")
print(f"p-value is: {p_val}")
conclusion = stat_conclusion(p_val, alpha)
print(f"{conclusion} the null hypothesis that the distributions are the same.")
print()


# Normal
mu = 48
sig = 80

our_norms = [rds.norm(mu, sig) for _ in range(obs)]
np_norms = random.normal(mu, sig, obs)
test_stat, p_val = ks_2samp(our_norms, np_norms)

print("NORMAL DISTRIBUTION")
print(f"Kolmogorov-Smirnov test result comparing our norm({mu}, {sig}) distribution to numpy's:")
print(f"Test statistic is: {test_stat}")
print(f"p-value is: {p_val}")
conclusion = stat_conclusion(p_val, alpha)
print(f"{conclusion} the null hypothesis that the distributions are the same.")
print()


# Triangular
a = 3
c = 7

our_trigs = [rds.tria(a, c) for _ in range(obs)]
np_trigs = random.triangular(a, (a+c)/2, c, size=obs)
test_stat, p_val = ks_2samp(our_trigs, np_trigs)

print("TRIANGULAR DISTRIBUTION")
print(f"Kolmogorov-Smirnov test result comparing our tria({a}, {b}) distribution to numpy's:")
print(f"Test statistic is: {test_stat}")
print(f"p-value is: {p_val}")
conclusion = stat_conclusion(p_val, alpha)
print(f"{conclusion} the null hypothesis that the distributions are the same.")
print()


# Exponential
lamb = 0.001

our_expos = [rds.expo(lamb) for _ in range(obs)]
np_expos = random.exponential(1/lamb, obs)
test_stat, p_val = ks_2samp(our_expos, np_expos)

print("EXPONENTIAL DISTRIBUTION")
print(f"Kolmogorov-Smirnov test result comparing our expo({lamb}) distribution to numpy's:")
print(f"Test statistic is: {test_stat}")
print(f"p-value is: {p_val}")
conclusion = stat_conclusion(p_val, alpha)
print(f"{conclusion} the null hypothesis that the distributions are the same.")
print()


# Poisson
lamb = 5

our_fishies = [rds.poisson(lamb) for _ in range(obs)]
np_fishies = random.poisson(lamb, obs)
test_stat, p_val = ks_2samp(our_fishies, np_fishies)

print("POISSON DISTRIBUTION")
print(f"Kolmogorov-Smirnov test result comparing our poisson({lamb}) distribution to numpy's:")
print(f"Test statistic is: {test_stat}")
print(f"p-value is: {p_val}")
conclusion = stat_conclusion(p_val, alpha)
print(f"{conclusion} the null hypothesis that the distributions are the same.")
print()


# Weibull
lamb = 2
beta = 70

our_weibull = [rds.weibull(lamb, beta) for _ in range(obs)]
# For some reason the numpy library doesn't have lambda and beta inputs
# so we will use a different library for this one so it matches our format
py_weibull = [weibullvariate(1/lamb, beta) for _ in range(obs)]
test_stat, p_val = ks_2samp(our_weibull, py_weibull)

print("WEIBULL DISTRIBUTION")
print(f"Kolmogorov-Smirnov test result comparing our weibull({lamb}, {beta}) distribution to pythons base random lib's:")
print(f"Test statistic is: {test_stat}")
print(f"p-value is: {p_val}")
conclusion = stat_conclusion(p_val, alpha)
print(f"{conclusion} the null hypothesis that the distributions are the same.")
print()


# Geometric
p = 0.4

our_geom = [rds.geom(p) for _ in range(obs)]
np_geom = random.geometric(p, obs)
test_stat, p_val = ks_2samp(our_geom, np_geom)

print("GEOMETRIC DISTRIBUTION")
print(f"Kolmogorov-Smirnov test result comparing our geom({p}) distribution to numpy's:")
print(f"Test statistic is: {test_stat}")
print(f"p-value is: {p_val}")
conclusion = stat_conclusion(p_val, alpha)
print(f"{conclusion} the null hypothesis that the distributions are the same.")
print()

# NegBin
n = 5
p = 0.5

our_negbin = [rds.negbin(n,p) for _ in range(obs)]
np_negbin = random.negative_binomial(n, p, obs)
test_stat, p_val = ks_2samp(our_negbin, np_negbin)

print("NEGATIVE BINOMIAL DISTRIBUTION")
print(f"Kolmogorov-Smirnov test result comparing our negbin({n}, {p}) distribution to numpy's:")
print(f"Test statistic is: {test_stat}")
print(f"p-value is: {p_val}")
conclusion = stat_conclusion(p_val, alpha)
print(f"{conclusion} the null hypothesis that the distributions are the same.")
print()


