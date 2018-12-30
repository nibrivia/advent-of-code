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


# Part two

def compute_values(graph):
    working = True
    values = dict()
    while not 0 in values:
        for uid, node in graph.items():
            if uid in values:
                continue

            children = node["children"]
            data     = node["data"]

            if len(children) == 0:
                values[uid] = sum(data)
            else:
                ready = True
                value_uids = []
                for child_num in data:
                    # Doesn't point to a real child
                    if child_num == 0 or child_num > len(children):
                        continue

                    # It does, check if we have the value, else skip
                    child_uid = children[child_num-1]
                    value_uids.append(child_uid)
                    if not child_uid in values:
                        ready = False
                if ready:
                    values[uid] = sum(values[child_uid] for child_uid in value_uids)

    return values[0]

value = compute_values(graph)
print(value)
