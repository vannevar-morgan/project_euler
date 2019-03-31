#! /usr/bin/env python3

import time

def read_file(filename):
    """
    read file and return data as a list
    """
    data = []
    with open(filename) as in_file:
        for line in in_file:
            data.append(line)
    return data


def parse_data(data):
    """
    parse data as a list of 50-digit numbers and return a list of those numbers
    """
    nums = []
    for line in data:
        nums.append(int(line.strip()))
    return nums


def get_digits(value, n):
    """
    return the first n digits of value, or all digits if n > total number of digits
    """
    svalue = str(value)
    if n > len(svalue):
        n = len(svalue)
    return svalue[:n]


def main():
    """
    Project Euler, Problem 13

    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers. (provided in problem_13_data.txt)
    """
    t_begin = time.time()
    data_filename = "problem_13_data.txt"
    number_of_digits = 10
    data = read_file(data_filename)
    nums = parse_data(data)
    val = sum(nums)
    print(get_digits(val, number_of_digits))
    print("elapsed time: " + str(time.time() - t_begin))



if __name__ == "__main__":
    main()
