import re


with open("input3.txt", "r") as f:
    content = f.read()


pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"

total = 0

matches = re.findall(pattern,content)
enabled = True
for match in matches:
    if match[0] == "don't()":
        enabled = False
    elif match[0] == "do()":
        enabled = True
    else:
        total += enabled*(int(match[1]) * int(match[2]))

print(total)
