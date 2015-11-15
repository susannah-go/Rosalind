# Solution to Rosalind problem iprb using sample dataset

from __future__ import division

k = 2
m = 2
n = 2
p = k + m + n   # population size

num = 4 * k ** 2 - 4 * k + 8 * k * m + 8 * k * n + 3 * m ** 2 - 3 * m + 4 * m * n
den = 4 * p * (p - 1)

print num/den

