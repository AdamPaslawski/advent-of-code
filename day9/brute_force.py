with open("input9.txt", "r") as f:
    example = f.read().strip()

# Take me to jail for this one.

example = "20202"
example = "02020"
example = "12345"
example = "2333133121414131402"

with open("input9.txt", "r") as f:
    example = f.read().strip()
def to_integer_array(s: str) -> list[int]:
    return [int(c) for c in s]


example_as_int_array = to_integer_array(example)
print(example_as_int_array)

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

print(example_expanded)

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


filled = fillerino(example_expanded)

print(filled)


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