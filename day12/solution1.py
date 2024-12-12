from collections import deque
grid = []

with open("input12.txt", "r") as f:
    for line in f.readlines():
        grid.append(line.rstrip("\n"))

rows = len(grid)
cols = len(grid[0])

print(f"Dimensions of grid: {rows,cols}")



def calculate_fencing_cost(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    total_cost = 0
    visited = set()

    for r in range(rows):
        for c in range(cols):
            if (r, c) in visited:
                continue

            visited.add((r, c))
            flavour = grid[r][c]
            q = deque()
            q.append((r, c))
            area = 0
            perimeter = 0

            print(f"Beginning exploration at ({r}, {c}) for flavour {flavour}")

            while q:
                cr, cc = q.popleft()
                area += 1
                print(f"cell ({cr}, {cc}), area: {area}, perimeter: {perimeter}")

                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = cr + dr, cc + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        perimeter += 1
                    elif grid[nr][nc] != flavour:
                        perimeter += 1
                    elif (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

            cost = area * perimeter
            print(f"Done exploring f;lav {flavour}  area = {area} perimeter = {perimeter} cost = {cost}")
            total_cost += cost

    return total_cost

total = calculate_fencing_cost(grid)
print(f"fencing cost: {total}")

