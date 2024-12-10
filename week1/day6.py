import re
import os

def get_starting_pos_and_sym(board):
    pos, sym = None, ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in ['^', '>', 'v', '<']:
                sym += f[i][j]
                pos = (i,j)
                break
        if pos != None:
            break
    return pos, sym

def move(row, col, sym):
    if sym == '^':
        row-=1
    elif sym == '>':
        col+=1
    elif sym == '<':
        col-=1
    elif sym == 'v':
        row+=1
    return (row,col)

def check_bounds(f, row, col):
    return True if row >= 0 and col >= 0 and row < len(f) and col < len(f) else False

if __name__=='__main__':
    day_num = "6"
    cdir = os.path.dirname(os.path.realpath(__file__))
    testing = True  
    fname = f"day{day_num}_test.txt" if testing else f"day{day_num}.txt"
    f = open(os.path.join(cdir, "inputs", fname)).read().split("\n")
    f = [list(x) for x in f]

    pos, sym = get_starting_pos_and_sym(f)

    # day 1
    row,col = pos
    curr_sym = sym
    visited_locs = {(4,6)}
    all_visited_locs = [(row,col)]
    next_sym = {'^': '>','>': 'v','v': '<','<': '^'}
    while row != 0 and col != 0 and row != len(f) and col != len(f):
        next_row, next_col = move(row,col, curr_sym)
        if check_bounds(f, next_row, next_col) and f[next_row][next_col] == "#":
            curr_sym = next_sym[curr_sym]
        else:
            row,col = next_row, next_col
            visited_locs.add((row,col))
            all_visited_locs.append((row,col))
    print(len(visited_locs))  # minus 1 for exit loc 