#! /usr/bin/env python3

import copy
import time

def read_data(filename):
    """
    read filename and return data as a list.
    """
    data = []
    with open(filename) as in_file:
        for line in in_file:
            data.append(line)
    return data


def parse_data(text_list):
    """
    parse text_list as a list of space delimited numbers, for each line
    """
    data = []
    for line in text_list:
        vals = line.strip().split(" ")
        nums = []
        for v in vals:
            nums.append(int(v))
        data.append(nums)
    return data


def get_cols(data):
    """
    return a list of the column values of data, as a list of rows
    """
    cols = []
    n_cols = len(data[0])
    for i in range(n_cols):
        c = []
        for r in data:
            c.append(r[i])
        cols.append(c)
    return cols


def get_left_diags(data, chain_length):
    """
    return a list of the negative slope, lower diagonals, as a list of rows
    """
    diags = []
    rows = len(data)
    cols = len(data[0])
    r = 0
    c = 0
    while r < rows:
        line = []
        r2 = r
        c = 0
        while c < cols and r2 < rows:
            line.append(data[r2][c])
            r2 += 1
            c += 1
        r += 1
        if len(line) < chain_length:
            break
        diags.append(line)
    return diags


def get_diag(data, chain_length):
    """
    return a list of the negative slope diagonals, as a list of rows
    """
    # get the left diagonals of data
    diags = get_left_diags(data, chain_length)
    # flip the matrix about the main negative slope diagonal to get the right, negative slope diagonals of data
    cols = get_cols(data)
    d2 = get_left_diags(cols, chain_length)
    del d2[0]
    diags.extend(d2)
    return diags


def find_max(lines, chain_length):
    """
    given a set of rows representing the vertical, hoizontal, and diagonal lines in a grid,
    return the max possible product of the elements in a chain of a given length.
    """
    max_val = 0
    max_elems = []
    current = 0
    for l in lines:
        cols = len(l)
        i = 0
        while i + (chain_length - 1) < cols:
            current = 1
            elems = []
            for j in range(i, i + chain_length):
                current *= l[j]
                elems.append(l[j])
            if current > max_val:
                max_val = current
                max_elems = elems
            i += 1
    return [max_elems, max_val]


def main():
    """
    project euler, problem 11
    
    In the 20x20 grid in problem_11_data.txt, four numbers along a diagonal line have been marked in red. [(6, 8), (7, 9), (8, 10), (9, 11)].

    The product of these numbers is 26*63*78*14 = 1788696.
    What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?
    """
    t_begin = time.time()
    p11_data_fn = "problem_11_data.txt"
    chain_length = 4
    
    fdata = read_data(p11_data_fn)
    data = parse_data(fdata)

    cols = get_cols(data)
    row_flip = copy.deepcopy(data)
    row_flip = row_flip[::-1]
    ns_diag = get_diag(data, chain_length)
    ps_diag = get_diag(row_flip, chain_length)
    
    lines = copy.deepcopy(data) # rows
    lines.extend(cols)          # cols
    lines.extend(ns_diag)       # negative slope diagonals
    lines.extend(ps_diag)       # positive slope diagonals

    [max_elems, max_val] = find_max(lines, chain_length)
    print("greatest product: " + str(max_val))
    print("elements: ", end="")
    for i in max_elems:
        print(i, end=" ")
    print()

    print("elapsed time: " + str(time.time() - t_begin))



if __name__ == "__main__":
    main()
