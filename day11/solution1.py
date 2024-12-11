from math import log10, ceil
from collections import defaultdict
import sys
sys.setrecursionlimit(1500)

input = [int(num) for num in "17639 47 3858 0 470624 9467423 5 188".split(" ")]

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



def apply_rules(num):

    if num == 0:
        return [1]
    elif num_digits(num)%2==0:
        return split_int_down_middle(num)
    else:
        return [num*2024]

manual_cache = {}
def expand_num(num: int, depth: int) -> int:

    if (num,depth) in manual_cache:
        ans,hits = manual_cache[(num,depth)]
        manual_cache[(num,depth)] = (ans,hits+1)
        return ans

    if depth == 0:
        return 1

    res = apply_rules(num)


    ans = sum([expand_num(n, depth - 1) for n in res])
    manual_cache[(num,depth)] = (ans,1)

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

counter = 0
for num in input:
    counter += expand_num(num, 300)
print("Super high depth...")
print(counter)


# Pretty sure this whole thing just loops eventually... Lets see..
hit_totals = defaultdict(int)
for (num, depth), (ans, hits) in manual_cache.items():
    hit_totals[(num, depth)] += hits
hit_list = [(total_hits, depth, num) for (num, depth), total_hits in hit_totals.items()]
# Unique numbers hit
nums = set([num for (num, depth), total_hits in hit_totals.items()])

#cache hit count high to low by number of hits
# I guess the hypothesis is it's some cycle inlcuding alot of 0->1->2024->...->0->1 you get the idea.
sorted_hit_list = sorted(hit_list, key=lambda x: x[2])

print(f"Total unique numbers {len(nums)}")
