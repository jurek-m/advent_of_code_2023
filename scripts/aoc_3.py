import numpy as np
from itertools import groupby


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


def get_abs_ix(aster_index_subarr, ix):

    a = ix[0]-1+aster_index_subarr[0] if ix[0]-1 >= 0 else aster_index_subarr[0]
    c = ix[1]-1+aster_index_subarr[1] if ix[1]-1 >= 0 else aster_index_subarr[1]

    return [a, c]


def identify_gears(arr):
    
    gear_nrs = list()
    temp_nr = {'number': 0, 'gear_attached': False, 'aster_pos': [], 'elems': {}}

    for ix, elem in np.ndenumerate(arr):
        # print(ix, elem)

        if elem.isdigit():
            
            # print(ix, elem)
            temp_nr['elems'][ix] = elem                                     # add elem to current number

            # check if asterisk is adjacent
            adjacent_fields = get_adjacent_subarr(arr, ix)
            is_aster = (adjacent_fields == '*')
            asterisk_adjacent = is_aster.any()

            if asterisk_adjacent:
                temp_nr['gear_attached'] = True
                np.where(is_aster)[0]
                for pos in range(len(np.where(is_aster)[0])):
                    aster_index_subarr = [np.where(is_aster)[0][pos], np.where(is_aster)[1][pos]]
                    aster_index_arr = get_abs_ix(aster_index_subarr, ix)
                    # print(aster_index_arr, arr[aster_index_arr[0], aster_index_arr[1]])
                    temp_nr['aster_pos'].append(aster_index_arr)
            
            # identify end of a number
            if (ix[1] == len(arr)-1) or (not arr[ix[0], ix[1]+1].isdigit()):
                
                temp_nr['number'] = int("".join(temp_nr['elems'].values()))
                
                # close the number
                gear_nrs.append(temp_nr)                                                        # add temp_nr to numbers
                temp_nr = {'number': 0, 'gear_attached': False, 'aster_pos': [], 'elems': {}}   # clear temp_nr
    
    return gear_nrs


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


# change input to an array
lists = list()
with open("inputs/aoc_input_3.txt", "r") as lines:
    for line in lines:
        line = line.replace('\n', '')
        lst = list(line)
        lists.append(lst)
arr = np.array(lists)


# 1 ------------------------------------------

numbers, sum_part_nrs = identify_numbers(arr)

print(sum_part_nrs)

# 2 ------------------------------------------

gear_nrs = identify_gears(arr)
gears = dict()

# check results and match gear numbers
for nr in gear_nrs:
    if nr['gear_attached'] is True:
        if nr['aster_pos'] == []:
            print('no positions')
        if not all_equal(nr['aster_pos']):
            print('not all positions are equal')
        pos_key = tuple(nr['aster_pos'][0])             # change position list to tuple
        if pos_key in gears.keys():
            gears[pos_key].append(nr['number'])
        else:
            gears[pos_key] = [nr['number']]

# calc sum of gear ratios
gear_ratios_sum = 0
for nrs in gears.values():
    if len(nrs) > 2:
        print('more than 2 numbers attached to asterisk')
    elif len(nrs) == 2:
        gear_ratios_sum += np.prod(nrs)

print(gear_ratios_sum)
