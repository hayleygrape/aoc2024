import re
import os
from itertools import combinations

def check_sum(line):
    return sum([i*int(line[i]) for i in range(len(line)) if line[i] != "."])

def get_locs(disk):
    blank_locs, file_locs, curr_len = [], [], 0
    for i in range(len(disk)):
        if i % 2 == 1:
            blank_locs += [j for j in range(curr_len, curr_len+int(disk[i]))]
        else:
            file_locs += [j for j in range(curr_len, curr_len+int(disk[i]))]
        curr_len += int(disk[i])
    return blank_locs, file_locs

def create_rep(disk):
    rep = []
    id_num = 0
    for i, num in enumerate(disk):
        num = int(num)
        if i % 2 == 0:
            rep += [str(id_num) for i in range(num)]
            id_num += 1 
        else:
            rep += list("."*num)
    return rep


def get_loc_blocks(disk):  # disk rep 
    blank_blocks, file_blocks = [], []
    curr_char = disk[0]
    start = 0
    for i in range(1, len(disk)):
        char = disk[i]
        if char != curr_char:
            if curr_char.isdigit():
                file_blocks.append([start, i, i-start])
            else:
                blank_blocks.append([start, i, i-start])
            curr_char = char
            start = i
    # get last char
    if curr_char.isdigit():
        file_blocks.append((start, i+1, i+1-start))
    else:
        blank_blocks.append((start, i+1, i+1-start))
    return blank_blocks, file_blocks

if __name__=='__main__':
    cdir = os.path.dirname(os.path.realpath(__file__))
    testing = False
    fname = "day9_test.txt" if testing else "day9.txt"
    f = open(os.path.join(cdir, "inputs", fname)).read()
    
    # part 1
    blank_locs, file_locs = get_locs(f)
    disk = create_rep(f)
    j = len(file_locs)-1
    for i in range(len(blank_locs)):
        disk[blank_locs[i]] = disk[file_locs[j]]
        j -= 1
    max_len = len(disk) - len(blank_locs)
    print(check_sum(disk[:max_len]))

    # part 2
    disk = create_rep(f)
    blank_blocks, file_blocks = get_loc_blocks(disk)
    file_blocks = file_blocks[::-1]
    for i in range(len(file_blocks)):
        file_len = file_blocks[i][2]
        for j in range(len(blank_blocks)):
            if file_blocks[i][0] < blank_blocks[j][0]:
                break
            blank_len = blank_blocks[j][2]
            if blank_len >= file_len:
                extra = blank_len-file_len
                new_end = blank_blocks[j][1]-extra
                disk[blank_blocks[j][0]:new_end] = disk[file_blocks[i][0]:file_blocks[i][1]]
                disk[file_blocks[i][0]:file_blocks[i][1]] = ["."]*file_len
                blank_blocks[j] = [new_end, blank_blocks[j][1], blank_blocks[j][1]-new_end]
                break
    print(check_sum(disk))