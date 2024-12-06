import re


with open("input3.txt", "r") as f:
    content = f.read()


pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

total = 0

matches = re.findall(pattern,content)

for match in matches:
    total += int(match[0]) * int(match[1])

print(total)
