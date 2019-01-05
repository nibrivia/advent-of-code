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

def pots_to_n(context):
    num = 0
    for p in context:
        num *= 2
        if p == "#":
            num += 1
    return num

rules = frozenset(pots_to_n(llcrr) for llcrr, n in rules.items() if n == "#")

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


def evolve(pots, rules, generations = 20):
    pots = {i: v for i, v in pots.items() if v != "."}
    pots = set(pots.keys())
    psum = 0
    diff = 0
    pred = 0

    for gen in range(generations):
        context = 0
        evolved = set()

        min_x, max_x = min(pots), max(pots)

        for index in range(min_x-2, max_x+3):
            context = (context*2) % 32
            if index+2 in pots:
                context += 1

            if context in rules:
                evolved.add(index)
        pots = evolved
        if gen > 100:
            ppsum = psum
            psum  = sum(pots)
            diff  = psum-ppsum

            pred_prev = pred 
            pred = (generations-gen-1)*diff+sum(pots)

            if diff == 58: # visually
                #print(sum(pots) - psum)
                print(" -{} {}".format(pred, diff))
                return pred
                #pass


    return sum(pots)

def part1(pots, rules):
    print(evolve(pots, rules, generations = 20))

def part2(pots, rules):
    generations = 50000000000
    #generations = int(5e4) # 2901856
    print(evolve(pots, rules, generations = generations))

part1(pots, rules) # 2823
part2(pots, rules)
