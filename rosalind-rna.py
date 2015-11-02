# Solution to Rosalind problem rna using sample dataset

dna = 'GATGGAACTTGACTACGTAAATT'
rna = ''

for c in dna:
    if c == 'T':
        rna += 'U'
    else:
        rna += c

print rna