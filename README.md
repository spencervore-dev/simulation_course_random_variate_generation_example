# Random Variate Generation Examples for Simulation Course
Summer 2021

## Summary of Project

This repository contains examples of how to generate various probability distributions using random numbers. Although we know that a lot of different packages exist to create these distributions, one of our goals was to gain a deeper understanding of these distributions so we decided to code up the underlying math ourselves.

This project was create for our masters level simulation course.


## What's in this repository:
random_distributions.py - This is our main distribution library that contains our various random distribution generators.

plot_distributions.ipynb - A jupyter notebook that calls all the functions in the random_distributions library many times to generate histograms.

test.py - This file compares our random distribution library to other standard random python libraries such as numpy.random. It uses the Kolomogorov-Smirnoff test to compare the output of the distributions from our library and another standard library to see if statistically they are the same.

plots - Directory with png versions of all the distribution plots generated in the Jupyter notebook.

requirements.txt - pip install this into a Python 3.8 environment to build the environment needed for this project.

## Description of the different library functions

The following is a brief how-to for each of the routines in the library. Extensive tests were done on each of the routines to ensure accuracy.

#### Linear Congruential Generator (lcg)
The default inputs are for the “Desert Island” lcg used in class. It has a full cycle and is known to be a good lcg. If the user wishes, the code can be adjusted to change the a, c, and mod parameters for a different lcg. This generates a Uniform(0,1) pseudo-random number every time it’s called. The seed is set based on the system time.

#### Bernoulli
A Bernoulli distribution returns 1 or 0 based on a specified probability. For this function, a user need only enter the probability, p, as a parameter, and the function will use a Uniform(0,1) number to determine success or failure. If U <= p then it will return 1, otherwise it will return 0.

#### Binomial
A binomial distribution counts the number of successes in a specified number of trials. A user would call this function, specifying the number of trials, n, and the probability of success, p. Since the binomial distribution is the sum of n Bernoulli distribution, this could have been set up using the convolution method, however, we chose to put the inverse transform method in a for loop to solve. This function will return the number of successes in the specified n trials.

#### Geometric
A geometric distribution counts the number of trials until the first success. As with the Bernoulli routine, this function will take the probability of success, p, as an input. The inverse transform method is then used with the lcg to return the number of trials.

#### Negative Binomial
A negative binomial distribution counts the number of trials until the specified nth success. This distribution is just the sum of geometric random variables until the nth success happens. Therefore, the convolution method was used for this routine. A user submits the number of successes, n, probability of success, p, and the routine calls the previously mentioned geometric routine n times and adds the results to get the total number of trials.

#### Poisson
A poisson distribution counts the number of arrivals within a given period of time, which also can be modeled using the exponential distribution for the interarrival times. For this routine, a user enters parameter lambda as the mean number of arrivals, and the function uses convolution to add up the number of exponential distributions called until just before the sum of the exponential random variates equals 1. It will return this total which is the Poisson estimate for the number of arrivals.
#### Uniform
A uniform distribution contains all values within two specified points, all having equal probability. For this routine, the user inputs the two specified points, a and b, and the inverse transform method with the lcg is used to return an x value between a and b.

#### Triangular
A triangular distribution is often used if there is little information known about the overall distribution aside from the minimum, maximum, and most likely numbers. For this routine, the user enters the min and max, and the most likely is calculated as halfway between these two values. The inverse transform method and the lcg is then used to return a value from the triangular distribution.

#### Exponential
An exponential distribution is used to measure interarrival times, as well as many other scenarios. The parameter, lambda, is entered when the function is called, and the inverse transform method is used with the lcg to return a value from the exponential distribution with lambda as the parameter.

#### Weibull
A Weibull distribution is very similar to the exponential distribution, but with an additional parameter, beta. It is also a special case of the gamma distribution. For this function, a user will specify the lambda and beta parameters. The Weibull cdf luckily has a closed form, so the inverse transform method is used with the lcg to then return a value from the Weibull distribution desired.

#### Normal
A normal distribution has mean and standard deviation parameters. This cdf also doesn’t have a closed form, so we used the Box-Muller transformation to find the random variates for the normal distribution. This transformation uses two Uniform(0,1) random numbers, and also has two options for formulas, a sin or cos. The default for this function uses cos, but the user can change this optional parameter when they also enter the parameters for mu and sigma in the function call. The function then returns a value from the normal distribution.

