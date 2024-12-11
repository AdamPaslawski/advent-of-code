from math import log10, ceil
from functools import cache

input = [int(num) for num in "17639 47 3858 0 470624 9467423 5 188".split(" ")]

print(f"input: {input}")

@cache
def num_digits(num: int):

    num_digits = ceil(log10(num + 1))

    return num_digits


def split_int_down_middle(num: int):

    nd = num_digits(num)

    assert nd%2 == 0 , "Behaviour not defined for splitting odd numbers of digits"

    middle_power_of_10 = nd//2

    left= num// 10**(middle_power_of_10)
    right=num%10**(middle_power_of_10)

    return (left,right)



@cache
def apply_rules(num):

    if num == 0:
        return [1]
    elif num_digits(num)%2==0:
        return split_int_down_middle(num)
    else:
        return [num*2024]


@cache
def expand_num(num: int, depth: int) -> int:

    if depth == 0:
        return 1

    res = apply_rules(num)
    
    ans = sum([expand_num(n, depth - 1) for n in res])

    return ans


assert expand_num(num=123, depth=2) == 2
assert expand_num(num=0, depth = 2) == 1
assert expand_num(num=1, depth = 2) ==  2

counter = 0
print("part1")
for num in input:
    counter += expand_num(num, 25)

print(counter)
counter = 0

print("part2")
for num in input:
    counter += expand_num(num, 75)

print(counter)


