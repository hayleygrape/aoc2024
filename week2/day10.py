import re
import os
from itertools import combinations

def get_neighbors(row, col):
    return [(row-1, col), (row, col-1), (row, col+1), (row+1, col)]

def get_next(pos,num,board):
    next_pos = set()
    for row,col in get_neighbors(pos[0], pos[1]):
        if board[row][col] != "." and int(board[row][col]) == num:
            next_pos.add((row,col))
    return next_pos

if __name__=='__main__':
    day_num = "10"
    cdir = os.path.dirname(os.path.realpath(__file__))
    testing = False  
    fname = f"day{day_num}_test.txt" if testing else f"day{day_num}.txt"
    f = open(os.path.join(cdir, "inputs", fname)).read().split("\n")

    # pad f
    f = ["."*len(f)] + f + ["."*len(f)]
    f = ["." + x + "." for x in f]

    start_list = []
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] != "." and int(f[i][j]) == 0:
                start_list.append((i,j))

    paths = 0
    for cord in start_list:
        curr_locs = [cord]
        for i in range(1, 10):
            next_locs = [] # change to list for part 2
            for pos in curr_locs:
                next_locs += list(get_next(pos, i, f))
            curr_locs = next_locs
        paths += len(next_locs)
    print(paths)
