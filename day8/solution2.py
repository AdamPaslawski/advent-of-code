from itertools import combinations
import math
lines = []



with open("input8.txt", "r") as f:
    s = f.read().strip()
# Grid prep
with open("input8.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.rstrip("\n"))

g = [list(r) for r in s.split("\n")]
n,m = len(g),len(g[0])


locations = {}

for row in range(n):
    for col in range(m):
        if g[row][col] == ".":
            continue
        if g[row][col] in locations:
            locations[g[row][col]].append((row,col))
        else:
            locations[g[row][col]] = [(row,col)]

count = 0

# incase antinodes created in the same place by diff frequencies idk.
antinode_set = set()

for frequency in locations:
    coords = locations[frequency]

    for combination in combinations(coords, 2):
        p1 = combination[0]
        p2 = combination[1]

        og_dr = p2[0] - p1[0] 
        og_dc = p2[1] - p1[1]

        gcd = math.gcd(og_dr,og_dc)
        # Make these things the smallest unit vector possible... aka gcd(a,b) == 1
        dr = og_dr//gcd
        dc = og_dc//gcd

        assert og_dc == dc and og_dr == dr
        # Wth nvm looks like they only give you unit vectors that's kind of crazy they thought of that...?
        # dr,dc is an arrow TOWARDS p2 

        # Keep extending in both directions along this vector till we're off grid
        continue_1 = True
        continue_2 = True
        step = 0

        while continue_1 or continue_2:

            # Walk in both directions between antinodes as far as we can...
            
            forward = (p2[0] + step*dr, p2[1] + step*dc)  
            backward = (p1[0] - step*dr, p1[1] - step*dc)  
            

            if 0 <= forward[0] < n and 0 <= forward[1] < m:
                antinode_set.add(forward)
            else:
                continue_1 = False

            if 0 <= backward[0] < n and 0 <= backward[1] < m:
                antinode_set.add(backward)
            else:
                continue_2 = False

            step += 1

print(len(antinode_set))
