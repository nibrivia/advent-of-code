from aoc_helpers import *
import parse
from toposort import toposort_flatten, toposort

parser = parse.compile("Step {} must be finished before step {} can begin.")
steps_list = [parser.parse(step_str) for step_str in get_input(7)]

depends = dict()
for fst, snd in steps_list:
    cur_deps = depends.get(snd, set())
    cur_deps.add(fst)
    depends[snd] = cur_deps

def topo_sort_alpha(graph):
    nodes = set()
    for dest, deps in graph.items():
        nodes.add(dest)
        nodes.update(deps)

    available = nodes - set(graph.keys())
    removed = set()
    order = []
    while len(available) > 0:
        # Get the next node
        node = sorted(available)[0]
        available.discard(node)
        order.append(node)

        # Update the dependencies
        for dest, deps in graph.items():
            graph[dest].discard(node)
            if len(graph[dest]) == 0 and dest not in removed:
                removed.add(dest)
                available.add(dest)

    return order




print(depends)
order = topo_sort_alpha(depends)
print(''.join(order))

