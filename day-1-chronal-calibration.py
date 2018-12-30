import itertools

from aoc_helpers import *

# Part 1 done in R

# Part 2 lives here

def main():
    puzzle_input = get_input(1)
    freq_changes = [int(line) for line in puzzle_input.split()]

    seen_freqs = set()
    current_freq = 0
    for i, delta_f in enumerate(itertools.cycle(freq_changes)):
        current_freq += delta_f
        if current_freq in seen_freqs:
            print("Duplicate frequncy %s found at iteration %s" % (current_freq, i))
            return
        else:
            seen_freqs.add(current_freq)

if __name__ == "__main__":
    main()
