from aoc_helpers import *
polymer = get_input(5)[0].rstrip() # Remove the \n

# Part 1

def simplify(polymer):
    prev = ""
    done = [" "]
    for i, c in enumerate(list(polymer)):
        # Don't check the first
        if c == prev.swapcase():
            done.pop()
            prev = done[-1]
        else:
            done.append(c)
            prev = c

    return done[1:]

#simplified = simplify("dabAcCaCBAcCcaDA")
simplified = simplify(polymer)
#print(simplified)
print(len(simplified))

# Part 2
import string

def optimize(polymer):
    lengths = dict()
    for c in string.ascii_lowercase:
        trimmed = polymer.replace(c, "").replace(c.capitalize(), "")
        lengths[c] = len(simplify(trimmed.replace(c, "")))
    return lengths

optimized_lengths = sorted(optimize(polymer).items(), key = dict_key)
print(optimized_lengths)
