import itertools

from aoc_helpers import *
freq_changes = get_input(1)

# Part 1 done in R

# Part 2 lives here

seen_freqs = set()
current_freq = 0
for delta_f in itertools.cycle(freq_changes):
    current_freq += delta_f

    if current_freq in seen_freqs:
        print(current_freq)
        break

    seen_freqs.add(current_freq)
