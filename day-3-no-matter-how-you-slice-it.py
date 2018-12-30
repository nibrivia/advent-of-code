from aoc_helpers import *
from parse import parse
claims_str = get_input(3)

def parse_claims(claims_str):
    claim_format = "#{:d} @ {:d},{:d}: {:d}x{:d}"
    return [parse(claim_format, c) for c in claims_str]

claims = parse_claims(claims_str)

# Part one
board = dict()

for claim_id, x, y, width, height in claims:
    for dx in range(width):
        for dy in range(height):
            position = (x+dx, y+dy)
            board[position] = board.get(position, 0) + 1

contested = [c for c in board.values() if c > 1]
print(len(contested))
