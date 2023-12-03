strigits = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

with open("inputs/aoc_input_1.txt", "r") as f:
    lines = [line for line in f]

number = 0

for line in lines:

    # print(line)

    digs = {}
    start = -1
    for i in line:
        if i.isdigit():
            digs[line.find(i, start+1)] = int(i)
            start = line.find(i, start+1)

    stigs = {}
    for sub in strigits.keys():
        if sub in line:
            cnt = line.count(sub)
            start = -1
            for occ in range(cnt):
                stigs[line.find(sub, start+1)] = strigits[sub]
                start = line.find(sub, start+1)

    digstig = {**digs, **stigs}


    adtn = int(digstig[min(digstig.keys())])*10+int(digstig[max(digstig.keys())])
    number += adtn

    # print(line, digstig)
    # print(digstig[min(digstig.keys())], digstig[max(digstig.keys())])
    # print(adtn, number)

print(number)
