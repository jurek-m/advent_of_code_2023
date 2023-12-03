import numpy as np


def get_adjacent_subarr(arr, ix):

    a = ix[0]-1 if ix[0]-1 >= 0 else 0
    b = ix[0]+2 if ix[0]+2 < len(arr) else len(arr)-1
    c = ix[1]-1 if ix[1]-1 >= 0 else 0
    d = ix[1]+2 if ix[1]+2 < len(arr) else len(arr)-1

    return arr[a:b, c:d]


def identify_numbers(arr):
    
    numbers = list()
    sum_part_nrs = 0
    temp_nr = {'number': 0, 'part_nr': False, 'elems': {}}

    for ix, elem in np.ndenumerate(arr):
        # print(ix, elem)

        if elem.isdigit():
            
            # print(ix, elem)
            temp_nr['elems'][ix] = elem                                     # add elem to current number

            # check if symbol is adjacent
            adjacent_fields = get_adjacent_subarr(arr, ix)
            are_digits = np.char.isdigit(adjacent_fields)
            are_dots = (adjacent_fields == '.')
            symbol_adjacent = np.invert(are_digits + are_dots).any()
            if symbol_adjacent:
                temp_nr['part_nr'] = True
            
            # identify end of a number
            if (ix[1] == len(arr)-1) or (not arr[ix[0], ix[1]+1].isdigit()):
                
                temp_nr['number'] = int("".join(temp_nr['elems'].values()))

                # sum part number
                if temp_nr['part_nr']:
                    sum_part_nrs += temp_nr['number']
                
                # close the number
                numbers.append(temp_nr)                                     # add temp_nr to numbers
                temp_nr = {'number': 0, 'part_nr': False, 'elems': {}}      # clear temp_nr
    
    return numbers, sum_part_nrs


lists = list()

# change input to an array
with open("inputs/aoc_input_3.txt", "r") as lines:
    for line in lines:
        line = line.replace('\n', '')
        lst = list(line)
        lists.append(lst)
arr = np.array(lists)

numbers, sum_part_nrs = identify_numbers(arr)

print(sum_part_nrs)