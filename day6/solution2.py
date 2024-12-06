from solution1 import matrix, start_location, DIRECTIONS

# WIP Trying to optimize this..

matrix = []

with open("input6.txt", "r") as f:
    for line in f.readlines():
        matrix.append(line.rstrip("\n"))

num_rows = len(matrix)
num_columns = len(matrix[0])

print(f"Dimensions of grid: {num_rows,num_columns}")

DIRECTIONS = {
    "<": (0, -1),
    ">": (0,1),
    "^": (-1,0),
    "v": (1,0),
}

# Wth does 90 degrees mean
turn = { 
    (0,-1):(-1,0),
    (-1,0):(0,1),
    (0,1):(1,0),
    (1,0):(0, -1)
}
for row in range(num_rows):
    for col in range(num_columns):
        if matrix[row][col] in DIRECTIONS:
            start_location = row,col
            start_direction = DIRECTIONS[matrix[row][col]]
            break

def navigate(locaysh, matrix, direction, block_locaysh, num_rows, num_columns, turn):
    next_locaysh = (locaysh[0] + direction[0], locaysh[1] + direction[1])

    if next_locaysh[0] < 0 or next_locaysh[0] >= num_rows or next_locaysh[1] < 0 or next_locaysh[1] >= num_columns:
        return (-1, -1), direction

    next_locaysh_content = matrix[next_locaysh[0]][next_locaysh[1]]

    if next_locaysh_content == "#" or next_locaysh == block_locaysh:
        direction = turn[direction]
        next_locaysh = (locaysh[0] + direction[0], locaysh[1] + direction[1])

        if next_locaysh[0] < 0 or next_locaysh[0] >= num_rows or next_locaysh[1] < 0 or next_locaysh[1] >= num_columns:
            return (-1, -1), direction

    return next_locaysh, direction


def analyze_grid(block_locaysh, locaysh, direction, matrix, num_rows, num_columns, turn):
    visited = set() 
    direction_map = {}

    visited.add(locaysh)
    direction_map[locaysh] = [direction]

    while True:
        locaysh, direction = navigate(locaysh, matrix, direction, block_locaysh, num_rows, num_columns, turn)

        if locaysh == (-1, -1):
            break

        if locaysh in visited and direction in direction_map.get(locaysh, []):
            return "Cycle detected! Danger ahead."

        visited.add(locaysh)
        if locaysh in direction_map:
            direction_map[locaysh].append(direction)
        else:
            direction_map[locaysh] = [direction]

    return visited



block_posishskis = 0

og_visited = analyze_grid(
    block_locaysh=None,
    locaysh=start_location,
    direction=start_direction,
    matrix=matrix,
    num_rows=num_rows,
    num_columns=num_columns,
    turn=turn
)

print(f"Guard is at: {start_location} facing {start_direction}")
print(f"Part 1 answer: {len(og_visited)} unique locations visited")

for block_locaysh in sorted(list(og_visited)):
    if block_locaysh == start_location:
        continue  

    result = analyze_grid(
        block_locaysh=block_locaysh,
        locaysh=start_location,
        direction=start_direction,
        matrix=matrix,
        num_rows=num_rows,
        num_columns=num_columns,
        turn=turn
    )
    if result == "Cycle detected! Danger ahead.":
        block_posishskis += 1

print(f"Part 2 answer: {block_posishskis} locations cause a cycle if blocked")
