
# Take me to jail for this one.

#example = "65432"
#example = "02020"
#example = "20202"
#example = "2333133121414131402"

print("Part 1:")

with open("input9.txt", "r") as f:
    example = f.read().strip()
def to_integer_array(s: str) -> list[int]:
    return [int(c) for c in s]


example_as_int_array = to_integer_array(example)

def expand(int_array: list[int]) -> list[int]:
    result: list = []
    f_id = 0

    space = False
    for width in int_array:
        if not space:
            result = result + width*[f_id]
            space = True
            f_id += 1
        else:
            result = result + width*[-1]
            space = space = False

    return result

example_expanded = expand(example_as_int_array)

def fillerino(expanded_array: list[int]):
    lptr = 0
    while lptr < len(expanded_array):

        num = expanded_array[lptr]

        if num == -1:
            # search right
            for i in range(len(expanded_array) - 1, -1, -1):
                if i == lptr:
                    return expanded_array

                if expanded_array[i] != -1:
                    expanded_array[lptr] = expanded_array[i]
                    expanded_array[i] = -1
                    break
        
        lptr += 1
    return expanded_array


filled = fillerino(example_expanded)


def do_the_checksum(expanded_array: list[int]):
    tot = 0
    for i,num in enumerate(expanded_array):
        if num == -1:
            pass
        else:
            tot += i*num
    return tot

check_summed = do_the_checksum(filled)

print(check_summed)



# part 2
# Index, how much space that index has
with open("input9.txt", "r") as f:
    example = f.read().strip()

print("Part 2:")

example_as_int_array = to_integer_array(example)
example_expanded = expand(example_as_int_array)

def build_space_map(example_as_int_array):
    space_array = []

    offset = 0

    for i in range(0,len(example_as_int_array)):

        if i % 2 == 0:
            # space is taken here
            offset += example_as_int_array[i]
        else:
            # This is open space
            space_index_start = offset
            space_index_end = offset + example_as_int_array[i]
            if space_index_start != space_index_end:
                space_array.append( [space_index_start, space_index_end] )
            offset += example_as_int_array[i]

    return space_array
     
space_map = build_space_map(example_as_int_array)

def space_map_size(start, end):
    #meaning if we found a block with val end-start or smaller we can put it there.
    return end-start


i = len(example_expanded) -1
while i > 0:

    if example_expanded[i] == -1:
        i -= 1
        continue

    block_val = example_expanded[i]
    block_size = 0

    while example_expanded[i-block_size] == block_val:
       block_size += 1
    
    
    for space in space_map:
        if space[0] > i:
            break
        if (space[1] - space[0]) >= block_size and space[0] < i:
            #move it!
            for j in range(space[0], space[0] + block_size):
                example_expanded[j] = block_val
            for j in range(i-block_size + 1, i + 1):
                example_expanded[j] = -1
            
            space[0] = space[0] + block_size
            if space[0] == space[1]:
                del space
            break

    i -= block_size

part_2 = do_the_checksum(example_expanded)

print(part_2)


