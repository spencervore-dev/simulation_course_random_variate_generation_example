# This script is a demostration / test of all the different
# random distribution generation functions in our library.

import random_distributions as rds
# Import the other script where we define all the functions


# Demo each distribution

unifs = []
for i in range(0,9):
    unifs.append(rds.unif(3,6))
print("Sample uniform distributions between 3 and 6")
print(unifs)
