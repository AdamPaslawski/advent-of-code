from itertools import combinations
lines = []

with open("input8.txt", "r") as f:
    s = f.read().strip()

with open("input8.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.rstrip("\n"))

# Grid input prep
g = [list(r) for r in s.split("\n")]
n,m = len(g),len(g[0])


locations = {}

# Get locations for all antenae with all frequencies
for row in range(n):
    for col in range(m):
        if g[row][col] == ".":
            continue
        if g[row][col] in locations:
            locations[g[row][col]].append((row,col))
        else:
            locations[g[row][col]] = [(row,col)]

#print(locations)
count = 0
antinode_set = set()

for frequency in locations:
    coords = locations[frequency]

    for combination in combinations(coords, 2):
        p1 = combination[0]
        p2 = combination[1]

        dr = p2[0] - p1[0] 
        dc = p2[1] - p1[1]
        # dr,dc is an arrow TOWARDS p2 

        forward = (p2[0] + dr, p2[1] + dc)  # Extended position from p2
        backward = (p1[0] - dr, p1[1] - dc)  # Extended position from p1

        # Add valid antinodes within grid bounds
        if 0 <= forward[0] < n and 0 <= forward[1] < m:
            antinode_set.add(forward)
        if 0 <= backward[0] < n and 0 <= backward[1] < m:
            antinode_set.add(backward)

print(len(antinode_set))
