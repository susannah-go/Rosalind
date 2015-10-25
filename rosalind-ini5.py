# Solution to Rosalind problem INI5 using sample dataset

f1 = open('rosalind-ini5input.txt', 'r')
f2 = open('rosalind-ini5output.txt', 'w')
count = 1

for line in f1:
    if count % 2 == 0:
        f2.write(line)
    count += 1

f1.close()
f2.close()
