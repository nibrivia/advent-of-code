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


# Part two
## differ in at most one place
import re

def part_two():
    for scan in scans:
        for i in range(len(scan)):
            # Builds a regex accepting an arbitrary character in the middle
            before, after = scan[:i], scan[i+1:]
            regex_str = before + '.' + after
            regex = re.compile(regex_str)

            # filter returns an iterator, and we're gonna match ourselves
            for match in filter(regex.match, scans):
                if match != scan:
                    print(before + after)
                    return

part_two()
