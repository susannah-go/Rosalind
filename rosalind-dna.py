# Solution to Rosalind problem dna using sample dataset

s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
countA = 0
countC = 0
countG = 0
countT = 0


for c in s:
    if c == 'A':
        countA += 1
    elif c == 'C':
        countC += 1
    elif c == 'G':
        countG += 1
    else:
        countT += 1

print str(countA) + ' ' + str(countC) + ' ' + str(countG) + ' ' + str(countT)