from dataclasses import dataclass
import re
    
MAX_Y = 103 # 0-100 is 101 tiles
MAX_X = 101 # 

quadrant_counts = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    "bound": 0
}

NUMBER_OF_MOVES = 100
TIME_TO_TRAVEL = 100 #seconds

@dataclass
class Robot:
    x:int
    y: int
    velocity: tuple[int,int]

    def time_travel(self, seconds: int):
        print(self.x)
        print(self.y)
        self.x = (self.x + (seconds * self.velocity[0])) % MAX_X
        self.y = (self.y + (seconds * self.velocity[1])) % MAX_Y

        return True

    def get_quadrant(self):
        if self.x < MAX_X//2 and self.y < MAX_Y//2:
            return 1
        elif self.x > MAX_X//2 and self.y < MAX_Y//2:
            return 2
        if self.x < MAX_X//2 and self.y > MAX_Y//2:
            return 3
        elif self.x > MAX_X//2 and self.y > MAX_Y//2:
            return 4
        else:
            return "bound"

with open("input14.txt", "r") as f:
    for i,line in enumerate(f.readlines()):
        line = line.strip().rstrip("\n")

        # How this works
        # Left to right
        # Hard match "p="
        # Then either one of "+" or "-" followed by digits, 1 till they end.
        # Then hard match a , followed by again a "+" or "-" followed by digits

        # At this point we have p=-123,-456

        # Okay next is the " "+v= which is one whitespace followed by "v="
        # I guess we could use \s to allow for any amount of whitespace but it looks pretty consistent.
        # Now we're ready to pase velocities
        # again "+" or "-" followed by digits
        # then ","
        # And lastly "+" or "-" and digits to finish it off.
        pattern = r"p=([-]?\d+),([-]?\d+) +v=([-]?\d+),([-]?\d+)"
        match = re.search(pattern, line)

        print(f"Parsed match {match}")

        robot = Robot(
            x=int(match.group(1)),  # y goes to row
            y=int(match.group(2)),  # x goes to col
            velocity=(int(match.group(3)), int(match.group(4)))
        )
        robot.time_travel(TIME_TO_TRAVEL)
        quadrant = robot.get_quadrant()
        quadrant_counts[quadrant] += 1

print(quadrant_counts)
print(quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3] * quadrant_counts[4])
