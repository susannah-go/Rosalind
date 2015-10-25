# Solution to Rosalind problem INI6 using sample dataset

s = 'We tried list and we tried dicts also we tried Zen'

dict = {}
words = s.split()

for w in words:
    if w in dict:
        dict[w] += 1
    else:
        dict[w] = 1

for key, value in dict.items():
    print key + ' ' + str(value)