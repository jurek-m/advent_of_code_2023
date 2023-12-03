import numpy as np


def extract_games(lines):

    games = dict()

    for line in lines:
        # print(line)

        line = line.replace('\n', '')
        elems = line[5:].split(':')
        
        gm_no = int(elems[0])
        games[gm_no] = list()

        sets_list = elems[1].split(';')

        for set_str in sets_list:
            clrs_list = set_str.split(',')
            set_dict = dict()

            for clr_str in clrs_list:
                clr_elems = clr_str[1:].split(' ')
                set_dict[clr_elems[1]] = int(clr_elems[0])
            
            games[gm_no].append(set_dict)

    return games


def check_game_possibility(game, moeglich):

    for st in game:
        for clr, nr in st.items():
            if nr > moeglich[clr]:
                # print(False, clr, game)
                return False

    return True


def get_fewest_set(game):

    game_fewest_set = {'red': 0, 'green': 0, 'blue': 0}

    for st in game:
        for clr, nr in st.items():

            if nr > game_fewest_set[clr]:
                game_fewest_set[clr] = nr
                a =1

    return game_fewest_set


with open("inputs/aoc_input_2.txt", "r") as lines:
    games = extract_games(lines)

# 1 ------------------------------------------

moeglich = {'red': 12, 'green': 13, 'blue': 14}

possible_gmixs = list()

for gmix, gm in games.items():

    # print(gm)

    game_possible = check_game_possibility(gm, moeglich)
    if game_possible:
        possible_gmixs.append(gmix)

print(sum(possible_gmixs))


# 2 ------------------------------------------

powers = list()

for gmix, gm in games.items():

    # print(gm)

    lowest_set = get_fewest_set(gm)
    # print(lowest_set)
    power = np.prod(list(lowest_set.values()))
    powers.append(power)

print(sum(powers))
