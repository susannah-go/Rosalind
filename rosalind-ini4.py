# Solution to Rosalind problem INI4 using sample dataset

a = 100
b = 200
sum = 0

for i in range(a, b + 1):
    if i % 2 == 1:
        sum += i

print sum