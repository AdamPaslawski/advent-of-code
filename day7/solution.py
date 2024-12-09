from itertools import product

equations = []

with open("input7.txt", "r") as f:
    for line in f.readlines():
        equations.append(line.rstrip("\n"))
from math import floor, log10, log
def concat_numbers(n1, n2):
    
    # add 1 in the logarithm because 100 needs three decimal places not 2 even though 10^2 == 2
    # 99 for example only needs 2 zeroes, so 99  -> 100 == 10^2. wild
    n1_but_with_enough_zeroes_to_slap_n2_on_the_back = n1*10**(floor(log10(n2 + 1)) + 1)                                                                                             
    result = n1_but_with_enough_zeroes_to_slap_n2_on_the_back + n2
    #print(f"Concatted {n1} and {n2} to get {result}")
    return result

def concat_binary_representation(n1,n2):
    
    print(f"inputs: {n1,n2}, as binary: {bin(n1),bin(n2)}")

    space = floor(log(n2+1, 2) + 1)
    # Shift bits according to space calculated
    n1 = n1 << space
    
    # we can use OR or XOR because if we created proper space there should be no overlap.
    # I guess one check would be that XOR(n1,n2) == OR(n1,n2)?
    concatenated_binary = n1 | n2

    print(f"after concatenation: {concatenated_binary} or as binary: {bin(concatenated_binary)}")

    return concatenated_binary

def concat_n_nary_representation(n1:int,n2:int,degree_of_number_system: int = 10):

    n1= n1*degree_of_number_system**(floor(log(n2 + 1 , degree_of_number_system)) + 1)                                                                                             
    return (n1 + n2)


def try_to_hit_target_with_ops(nums, ops, target):
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i + 1]
        elif ops[i] == '*':
            result *= nums[i + 1]
        elif ops[i] == '||':
            #result = int(str(result) + str(nums[i + 1]))
            result = concat_numbers(result, nums[i + 1])
        if result > target: #early stopping optimization since there's no negative numbers or numbers inside interval (-1, 1) ∈ R
            return result

    return result

def brute_force_all_op_combinations(target, nums):
    n = len(nums)
    # Cartesian product of all the possible combinations of operations
    for ops in product(['+', '*', '||'], repeat=n-1):
        if try_to_hit_target_with_ops(nums, ops, target) == target:
            return True
    return False

def sum_valid_targets(equations):
    total = 0
    for equation in equations:
        target, nums = equation.split(':')
        target = int(target.strip())
        nums = list(map(int, nums.strip().split()))
        if brute_force_all_op_combinations(target, nums):
            total += target
    return total

# Playing with concatenation different number systems. Binary, decimal, n-nary..? 
n1 = 100
n2 = 1000
base_10 = concat_numbers(n1, n2)
base_2 = concat_binary_representation(n1, n2)
base_10_check = concat_n_nary_representation(n1, n2, 10)
base_2_check = concat_n_nary_representation(n1, n2, 2)

assert base_10 == base_10_check
assert base_2 == base_2_check, f"comparison failed for {base_2, base_2_check}"

import time
t0 = time.time()
result = sum_valid_targets(equations)
print(f"Time taken {time.time() - t0}")
print("Total Calibration Result:", result)
