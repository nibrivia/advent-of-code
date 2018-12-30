from aoc_helpers import *
import parse
targets = [parse.parse("{:d}, {:d}", coord) for coord in get_input(6)]

xs, ys = zip(*targets)
min_x, max_x = min(xs)-1, max(xs)+2
min_y, max_y = min(ys)-1, max(ys)+2

def closest(coord, targets):
    x, y = coord
    closest = (0, max_x)
    for t_x, t_y in targets:
        best_coord, best_dist = closest
        distance = abs(x-t_x) + abs(y-t_y)
        if distance < best_dist:
            closest = ((t_x, t_y), distance)
        if distance == best_dist:
            closest = (None, distance)
    return closest

board = {(x, y): ((0,0), max(max_x, max_y)) for x in range(min_x, max_x) for y in range(min_y, max_y)}


def part1(targets):
    for pos in board:
        board[pos] = closest(pos, targets)

    exclude = set()
    for x, y in board:
        if x in [min_x, max_x-1] or y in [min_y, max_y-1]:
            owner, _ = board[(x,y)]
            if owner is not None:
                exclude.add(owner)

    print(exclude)

    debug = False
    if debug:
        for x in range(min_x, max_x):
            row = [board[(x, y)][1] for y in range(min_y, max_y)]
            print(row)

    from collections import Counter
    sizes = Counter(owner for owner, _ in board.values() if not owner in exclude)
    return sizes.most_common(1)

#print(part1(targets))

def part2(targets):
    count = 0

    for x, y in board:
        distance = 0
        for t_x, t_y in targets:
            distance += abs(x-t_x) + abs(y-t_y)

        if distance < 10000:
            count += 1
    return count



print(part2(targets))

