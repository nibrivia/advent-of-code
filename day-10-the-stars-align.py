import parse
from aoc_helpers import *

parser = parse.compile("position=<{:g}, {:g}> velocity=<{:g}, {:g}>")
parsed_input = [parser.parse(s) for s in get_input(10)]
points = [(int(x), int(y), int(vx), int(vy)) for x, y, vx, vy in parsed_input]

def step(points, steps=1):
    return [(x+steps*vx, y+steps*vy, vx, vy) for x, y, vx, vy in points]

#print('\n'.join(str(x) for x in xs))


def spread(points):
    xs, ys, _, _ = zip(*points)
    spread_x = max(xs) - min(xs)
    spread_y = max(ys) - min(ys)
    return spread_x*spread_y


def part_one(points):
    original = points

    find_best = False
    if find_best:
        offset = 10230
        points = step(original, steps=offset)
        for i in range(20):
            points = step(points)
            if i % 1 == 0:
                print("%s: %s" % (offset+i, spread(points)))


    # By manual inspection
    best = 10242
    for dn in range(-1, 2):
        points = step(original, steps=best+dn)
        print(best+dn)
        render(points)


def render(points):
    xs, ys, _, _ = zip(*points)

    min_x, max_x = min(xs), max(xs)
    min_y, may_y = min(ys), max(ys)
    spread_x = max(xs) - min(xs) +1
    spread_y = max(ys) - min(ys) +1


    sky = [[" " for x in range(spread_x)] for y in range(spread_y)]
    for x, y, _, _ in points:
        sky[y-min_y][x-min_x] = "#"

    sky = '\n'.join([''.join(line) for line in sky])
    print(sky)






part_one(points)
