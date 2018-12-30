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
    nodes = set().union(*[k for k in graph.values()]).union(graph.keys())

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
            # skip if we've removed
            # (we're not actually removing because iterating on a thing we change is sketch)
            if dest in removed: continue

            graph[dest].discard(node)
            if len(graph[dest]) == 0:
                removed.add(dest)
                available.add(dest)

    return order


#order = topo_sort_alpha(depends)
#print(''.join(order))

def worker_sort(graph):
    nodes = set().union(*[k for k in graph.values()]).union(graph.keys())

    available = nodes - set(graph.keys())
    t = 0
    order = []
    workers = {i: None for i in range(5)}

    # One iteration == one timestep
    while len(order) < len(nodes) and t < 100000:
        t += 1
        # Schedule not-working workers
        for worker, task_state in workers.items():
            if task_state is None and len(available) > 0:
                node = sorted(available)[0]
                available.discard(node)
                task_len = 60+ord(node)-64
                #print("Scheduled worker #%s on task (%s, %s)" % (worker, node, task_len))
                workers[worker] = (node, task_len)

        #print("%s: %s" % (t, workers))

        done = set()
        for worker, task_state in workers.items():
            if task_state is None:
                continue
            task, remaining = task_state
            if remaining == 1:
                done.add(task)
                order.append(task)
                workers[worker] = None
            else:
                workers[worker] = (task, remaining-1)

        removed = set()
        for d in done:
            for dest in graph.keys():
                graph[dest].discard(d)
                if len(graph[dest]) == 0:
                    available.add(dest)
                    removed.add(dest)

        for r in removed:
            del graph[r]

    return t


print(worker_sort(depends))

