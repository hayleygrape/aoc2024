import re
import os
from itertools import combinations

def get_antenna_locs(f):
    ant_locs = {}
    for row in range(len(f)):
        for match in re.finditer(r'[a-zA-Z0-9]', f[row]):
            col = match.span()[0]
            char = f[row][col] 
            if char not in ant_locs:
                ant_locs[char] = []
            ant_locs[char].append((row,col))
    return ant_locs

def get_antinode_locs(cord1, cord2):
    rise, run = cord2[0]-cord1[0], cord2[1]-cord1[1]
    loc1 = (cord1[0]-rise, cord1[1]-run)
    loc2 = (cord2[0]+rise, cord2[1]+run)
    return loc1,loc2

def is_valid_cord(cord, row_len, col_len):  # written in (y,x)
    if cord[0] >= row_len or cord[0] < 0 or cord[1] >= col_len or cord[1] < 0:
        return False
    return True

def get_all_antinode_locs(cord1, cord2, col_len):
    locs = []
    m = (cord2[0]-cord1[0])/(cord2[1]-cord1[1])
    b = cord1[0]-(m*cord1[1])
    for x in range(col_len):
        y = round((m*x)+b,10)
        if y % 1 == 0:
            locs.append((y,x))
    return locs

if __name__=='__main__':
    cdir = os.path.dirname(os.path.realpath(__file__))
    testing = False
    fname = "day8_test.txt" if testing else "day8.txt"
    # fname = "day8_test2.txt"
    f = open(os.path.join(cdir, "inputs", fname)).read().split("\n")
    ant_locs = get_antenna_locs(f)
    row_len, col_len = len(f), len(f[0])

    # part 1
    antinode_locs = set()
    for k,v in ant_locs.items():
        for cord1, cord2 in list(combinations(ant_locs[k], 2)):
            loc1, loc2 = get_antinode_locs(cord1, cord2)
            if is_valid_cord(loc1, row_len, col_len):
                antinode_locs.add(loc1)
            if is_valid_cord(loc2, row_len, col_len):
                antinode_locs.add(loc2)
    print("Part 1:", len(antinode_locs))

    # part 2
    antinode_locs2 = set()
    for k,v in ant_locs.items():
        for cord1, cord2 in list(combinations(ant_locs[k], 2)):
            locs = get_all_antinode_locs(cord1, cord2, col_len)
            for loc in locs:
                if is_valid_cord(loc, row_len, col_len):
                    antinode_locs2.add(loc)
    print("Part 2:", len(antinode_locs2))

    # save board state 
    ant_locs_rev = {}
    for k,v in ant_locs.items():
        for x in v:
            ant_locs_rev[x] = k
    board = []
    for i in range(row_len):
        line = ""
        for j in range(col_len):
            if (i,j) in ant_locs_rev:
                line += ant_locs_rev[(i,j)]
            elif (i,j) in antinode_locs2:
                line += "#"
            else:
                line += "."
        board.append(line)
    with open(f'board{str(len(antinode_locs2))}.txt', 'w') as f:
        for line in board:
            f.write(f"{line}\n")

    # 1183 wrong
    # 944 -- too low