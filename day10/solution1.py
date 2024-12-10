matrix = []
with open("input10.txt", "r") as f:
    for line in f.readlines():
        matrix.append(line.rstrip("\n"))

num_rows = len(matrix)
num_columns = len(matrix[0])

trailheads = set()
for r in range(num_rows):
    for c in range(num_columns):
        if int(matrix[r][c]) == 0:
            trailheads.add((r, c))

score = 0

from collections import deque

def find_trail_ends(trail_head: tuple):
    ends = set()
    # Count for part 2
    counter = 0

    q = deque()
    q.append(trail_head)

    while len(q) > 0:
        r, c = q.pop()

        trail_location_value = int(matrix[r][c])

        up = (r-1, c) if r-1 >= 0 else None
        down = (r+1, c) if r+1 < num_rows else None
        left = (r, c-1) if c-1 >= 0 else None
        right = (r, c+1) if c+1 < num_columns else None

        for neighbor in [up, down, left, right]:
            if neighbor:
                nr, nc = neighbor
                val = int(matrix[nr][nc])
                if val == trail_location_value + 1:
                    if val == 9:
                        ends.add((nr, nc))
                        counter += 1
                    else:
                        q.append(neighbor)

    return len(ends), counter

pt_2 = 0
for trailhead in trailheads:
    unique_ends, all_ends =  find_trail_ends(trailhead)
    score += unique_ends
    pt_2 += all_ends

print(score)

print(pt_2)