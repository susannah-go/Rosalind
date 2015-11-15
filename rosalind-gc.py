# Solution to Rosalind problem gc using sample dataset

from __future__ import division

inputFile = open('rosalind-gcinput.txt', 'r')

max_label = ""                                              # label of DNA string with highest GC-content
max_gc = 0                                                  # highest GC-content

c_count = 0                                                 # temp variables
g_count = 0
temp_label = ""
temp_gc = 0.0
temp_len = 0

for line in inputFile:
    if line.startswith('>'):                                # line containing w/ label
        if temp_len != 0:                                   # block executes only if a previous DNA string exists
            temp_gc = (c_count + g_count) / temp_len * 100  # compute gc of previous DNA string
            if temp_gc > max_gc:                            # update max_label and max_gc
                max_label = temp_label
                max_gc = temp_gc
            c_count = 0                                     # reset counter variables
            g_count = 0
            temp_len = 0
        temp_label = line[1:14]
    else:                                                   # line containing DNA string fragment
        c_count += line.count('C')
        g_count += line.count('G')
        temp_len += len(str.strip(line))

temp_gc = (c_count + g_count) / temp_len * 100              # repeat calculations for last DNA string
if temp_gc > max_gc:
    max_label = temp_label
    max_gc = temp_gc

print max_label                                             # print DNA string with maximal GC-content
print max_gc

inputFile.close()
