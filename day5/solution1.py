rules = {}

updates = []

with open("input5.txt", "r") as f:
    for line in f.readlines():
        if "|" in line:
            numbers = line.split("|")
            n0 = int(numbers[0])
            n1 = int(numbers[1].rstrip("\n"))
            if n1 in rules:
                rules[n1].append(n0)
            else:
                rules[n1] = [n0]
        else:
            update = line.split(",")
            update = [int(num) for num in update if num != "\n"]
            if update != []:
                updates.append(update)

print(rules)
print(f"Parsed {len(updates)} updates")
print(f"Parsed {len(rules)} rules")

def is_valid(update: list[int], rules: dict):

    seen = set()

    for i in range(len(update)-1, -1, -1):

        number = update[i]
        can_not_have_seen = rules.get(number, [])
        
        if any(rule_number in seen for rule_number in can_not_have_seen):
            return False

        seen.add(number)

    # Middle update... problem seems to guarentee it's an odd number?
    if len(update) % 2 == 0:
        raise Exception("even numbered elements in update")

    return update[len(update)//2]

def reorder_invalid_update(update: list[int], rules: dict):
    seen = {}
    for i in range(len(update)-1, -1, -1):
        
        number = update[i]
        can_not_have_seen = rules.get(number, [])

        # Get intersection of can_not_have_seen and seen
        intersection = [number for number in can_not_have_seen if number in seen]


        if len(intersection) > 0:
            for number in intersection:
                # Remove number at that index that is causing this to fail.
                invalid_element = update.pop(seen[number])
                update.insert(0,invalid_element)
                del seen[number]
                # is this incredibly sweaty? yes absolutely.
                return reorder_invalid_update(update,rules)

        seen[number]=i 

    # Middle update... problem seems to guarentee it's an odd number?
    if len(update) % 2 == 0:
        raise Exception("even numbered elements in update")

    return update[len(update)//2]
    pass


sum = 0
bad_sum = 0
for update in updates:
    result=is_valid(update, rules)
    sum+=result
    if result is False:
        bad_sum += reorder_invalid_update(update,rules)


print(sum)
print(bad_sum)
