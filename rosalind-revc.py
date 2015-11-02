# Solution to Rosalind problem revc using sample dataset

input = 'AAAACCCGGT'

# reverse input string
reverse = ''
l = len(input)

for i in range(l):
    reverse += input[l - i - 1]


# take complement
output = ''

for c in reverse:
    if c == 'T':
        output += 'A'
    elif c == 'A':
        output += 'T'
    elif c == 'C':
        output += 'G'
    else:
        output += 'C'

print output