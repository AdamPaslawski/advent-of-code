from dataclasses import dataclass
import re

MAX_Y = 103
MAX_X = 101 

@dataclass
class Robot:
    x: int
    y: int
    velocity: tuple[int,int]

    def time_travel(self, seconds: int):
        self.x = (self.x + (seconds * self.velocity[0])) % MAX_X
        self.y = (self.y + (seconds * self.velocity[1])) % MAX_Y
        return True

robots = []

with open("input14.txt", "r") as f:
    for line in f:
        line = line.strip()

        pattern = r"p=([-]?\d+),([-]?\d+)\s+v=([-]?\d+),([-]?\d+)"
        match = re.search(pattern, line)

        robot = Robot(
            x=int(match.group(1)),
            y=int(match.group(2)),
            velocity=(int(match.group(3)), int(match.group(4)))
        )

        robots.append(robot)



def render(robots):

    grid = [['.' for _ in range(MAX_X)] for _ in range(MAX_Y)]
    position_counts = {}
    for r in robots:
        pos = (r.y, r.x)
        if pos not in position_counts:
            position_counts[pos] = 0
        position_counts[pos] += 1

    for (row, col), count in position_counts.items():
        if count == 1:
            grid[row][col] = 'R'
        else:
            grid[row][col] = str(count if count <= 9 else '9')

    for row in range(MAX_Y):
        print(''.join(grid[row]))


# Watch this rip by and try to catch the tree.
for i in range(10000):
    for robot in robots:
        robot.time_travel(1)
    print(f"############ RENDER {i} ########################\n")
    render(robots)
