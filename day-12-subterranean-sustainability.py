from aoc_helpers import *

input_str = get_input(12)

state = input_str[0].split(": ")[1]
#state = "#..#.#..##......###...###"
pots = {i: status for i, status in enumerate(state)}

rules_str = input_str[2:]
#rules_str = """...## => #
#            ..#.. => #
#            .#... => #
#            .#.#. => #
#            .#.## => #
#            .##.. => #
#            .#### => #
#            #.#.# => #
#            #.### => #
#            ##.#. => #
#            ##.## => #
#            ###.. => #
#            ###.# => #
#            ####. => #""".splitlines()
rules = dict([rule.split(" => ") for rule in rules_str])


def pots_str(pots):
    pots = {i: v for i, v in pots.items() if v != "."}
    indices = list(pots.keys()) + [-3, 34]
    min_x, max_x = min(indices), max(indices)
    pot_str = ""
    bot_str = ""
    for pot_i in range(min_x, max_x+1):
        bot_str += "^" if pot_i % 10 == 0 else " "
        pot_str += pots.get(pot_i, ".") 

    return "{} ({}, {})".format(pot_str, min_x, max_x)#+ "\n" + bot_str

from collections import deque

def evolve_pots(pots, rules):
    llcrr = deque('.....', maxlen = 5)
    evolved = dict()

    # We iterate over indices to make sure we don't miss entries
    indices = pots.keys()
    min_x, max_x = min(indices), max(indices)

    for index in range(min_x-5, max_x+5):
        llcrr.append(pots.get(index+2, ".")) # maxlen is 5, will pop too
        context = ''.join(llcrr)
        evolution = rules.get(context, ".")
        #print(" @{}, {} -> {}".format(index, context, evolution))
        if evolution == "#":
            evolved[index] = "#"


    return evolved

def evolve_n(pots, rules, generations = 20):
    print(" 0: %s" % (pots_str(pots)))
    for gen in range(generations):
        pots = evolve_pots(pots, rules)
        print("{:>2}: {}".format(gen+1, pots_str(pots)))
    return pots

print(pots_str(pots))
pots = evolve_n(pots, rules, generations = 20)
print(pots_str(pots))

pot_sum = 0
for pos, content in pots.items():
    if content == "#":
        pot_sum +=pos


print(pot_sum)
print()
