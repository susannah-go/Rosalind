# Solution to Rosalind problem hamm using sample dataset

s1 = "GAGCCTACTAACGGGAT"
s2 = "CATCGTAATGACGGCCT"

length = len(s1)
hamm = 0

for i in range(length):
    if s1[i] != s2[i]:
        hamm += 1

print hamm