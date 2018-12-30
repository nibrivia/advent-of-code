from aoc_helpers import *
scans = get_input(2)

# Part one

# counts[n] will be the number of scans with a character appearing n times
counts = dict()

for scan in scans:
    freq_set = set(scan.count(c) for c in scan)

    # Update the global counters for each frequency
    for f in freq_set:
        counts[f] = counts.get(f, 0) + 1

#print(counts)
print(counts[2] * counts[3])

