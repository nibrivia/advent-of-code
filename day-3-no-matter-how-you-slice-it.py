from aoc_helpers import *
from parse import parse
claims_str = get_input(3)

def parse_claims(claims_str):
    claim_format = "#{:d} @ {:d},{:d}: {:d}x{:d}"
    return [parse(claim_format, c) for c in claims_str]

claims = parse_claims(claims_str)

# Part one
board = dict()
conflict_free = set(claim_id for claim_id, _, _, _, _ in claims)

for claim_id, x, y, width, height in claims:
    for dx in range(width):
        for dy in range(height):
            position = (x+dx, y+dy)

            # Add claim to the board
            current_claims = board.get(position, set())
            current_claims.add(claim_id)
            board[position] = current_claims

            if len(current_claims) >= 2:
                conflict_free -= current_claims

contested = [c for c in board.values() if len(c) > 1]
print(len(contested))

print(conflict_free)
