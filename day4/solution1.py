from collections import deque

matrix = []
target = "XMAS"
count = 0

with open("input4.txt", "r") as f:
    for line in f.readlines():
        matrix.append(line.rstrip("\n"))

num_rows = len(matrix)
num_columns = len(matrix[0])

directions = [
    (-1, 0),  
    (1, 0),   
    (0, -1),  
    (0, 1),   
    (-1, -1), 
    (-1, 1),  
    (1, -1),  
    (1, 1)    
]

q = deque()

for row in range(num_rows):
    for col in range(num_columns):
        if matrix[row][col] == "X":
            q.append(("X", row, col, None))

while len(q) > 0:
    substring, row, col, direction = q.pop()

    if substring == target:
        count += 1
        continue

    if substring != target[0:len(substring)]:
        continue

    for row_incr, col_incr in directions:
        if direction is not None and direction != (row_incr, col_incr):
            continue
        
        new_row, new_col = row + row_incr, col + col_incr
        if 0 <= new_row < num_rows and 0 <= new_col < num_columns:
            new_substring = substring + matrix[new_row][new_col]
            q.append((new_substring, new_row, new_col, (row_incr, col_incr)))

print(count)
