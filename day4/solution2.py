from collections import deque

matrix = []
target = "XMAS"
count = 0

with open("input4.txt", "r") as f:
    for line in f.readlines():
        matrix.append(line.rstrip("\n"))

num_rows = len(matrix)
num_columns = len(matrix[0])

q = deque()

for row in range(num_rows):
    for col in range(num_columns):
        if matrix[row][col] == "A":
            q.append((row, col))

def is_x_mas(row, col):
    if (
        row - 1 >= 0 and col - 1 >= 0 and row + 1 < num_rows and col + 1 < num_columns
    ):
        top_left = matrix[row - 1][col - 1] 
        top_right = matrix[row - 1][col + 1] 
        bottom_left = matrix[row + 1][col - 1]
        bottom_right = matrix[row + 1][col + 1]
        
        # Bit of a hack lol
        if sorted([top_left,bottom_right]) == ["M", "S"] and sorted([top_right,bottom_left]) == ["M", "S"]:
            return True

    return False

while q:
    row, col = q.popleft()
    if is_x_mas(row, col):
        count += 1

print(count)
