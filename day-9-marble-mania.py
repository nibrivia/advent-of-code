from aoc_helpers import *
from blist import blist
split_str = get_input(9)[0].split()
n_players, n_marbles = int(split_str[0]), 100*int(split_str[6])

print(n_players)
print(n_marbles)

#n_players, n_marbles = 9, 25
#n_players, n_marbles = 10, 1618
#n_players, n_marbles = 13, 7999
#n_players, n_marbles = 17, 1104
#n_players, n_marbles = 21, 6111
#n_players, n_marbles = 30, 5807

circle = blist([0, 1])
current = 1
scores = [0 for i in range(n_players)]
player = 1
for n in range(2, n_marbles+1):
    player = (player+1) % n_players
    if n % 23 > 0:
        current = (current + 2) % len(circle)
        if current == 0:
            circle.append(n)
            current = len(circle)-1
        else:
            circle.insert(current, n)
    else:
        current = (current - 7) % len(circle)
        val = circle.pop(current)
        scores[player] += n + val
        #print(val)
    #print((player+1, circle))

print(max(scores))
print("ok")
