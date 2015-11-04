# Solution to Rosalind problem fib using sample dataset

n = 5
k = 3

val1 = 1
val2 = 1

if n > 2:
    for i in range(3, n + 1):
        temp = val2
        val2 = k * val1 + val2
        val1 = temp

print val2


