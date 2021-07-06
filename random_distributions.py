# A basic library of random distribution generation functions

# More info about what is already built into the basic python 
# random library that comes with base python

from random import random

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
