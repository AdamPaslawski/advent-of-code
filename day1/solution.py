from collections import Counter
def read_file_to_numpy_array(f_name: str , max_lines = None):
    f = open(f_name, "r")
    v1 = []
    v2 = []

    for index, line in enumerate(f.readlines()):

        left, right = line.split("   ")
        right.rstrip("\n")

        v1.append(int(left))
        v2.append(int(right))

    return v1, v2

def calculate_distance(v1, v2):
    diff_vector = abs(v1 - v2)
    distance = sum(diff_vector)
    return distance

v1,v2 = read_file_to_numpy_array("input.txt", max_lines = None)

v1_counter = Counter(v1)
v2_counter = Counter(v2)
#dist = calculate_distance(v1, v2)

total = 0

for val in v1_counter:
    if val in v2_counter:
        multiplier = v2_counter[val]
        scalar = val

        total += scalar*multiplier

print(total)

