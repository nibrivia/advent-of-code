from aoc_helpers import *
graph_desc = [int(n) for n in get_input(8)[0].split()]

def extract_first_child(desc):
    stack = [dict(data = None, n_children =  1, n_data = 0, children = [])] # This will hold the parents that arent' finished
    parse_new = True
    graph = dict()
    uid = 0
    while len(desc) > 0:
        # Work with whatever's the latest on the stack
        # Basically, these are our local vars
        element    = stack[-1]
        n_children = element["n_children"]

        # Try to read something new if our current element is not done
        # This will then add something to the stack
        if n_children > 0:
            # Get header
            n_children, n_data = desc[0:2]
            desc = desc[2:]

            # Add ourselves to the stack (function call), go back up top
            element = dict(uid = uid, data = [], children = [], n_children = n_children, n_data = n_data)
            uid += 1
            stack.append(element)
        else:
            # If we're done (0 children left to collect)
            # Get the data, update the string, decrement parent, pop ("return")
            n_data = element["n_data"]
            el_uid = element["uid"]
            element["data"] = desc[:n_data]
            desc = desc[n_data:]

            # "return"
            graph[el_uid] = stack.pop()

            # update parent
            stack[-1]["children"].append(el_uid)
            stack[-1]["n_children"] -= 1

    return graph


def print_graph(graph, pad = "", uid = 1):
    print("%s data [%s]: %s" % (pad, uid, graph["data"]))
    for child in graph["children"]:
        uid += 1
        print_graph(child, pad = " " + pad, uid = uid)

def sum_data(graph):
    return sum(sum(child["data"]) for child in graph.values())

#graph_desc = [int(d) for d in "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()]
graph = extract_first_child(graph_desc)

s = sum_data(graph)
print(s)
