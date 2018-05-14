#! /usr/bin/env python3

"""
Project Euler, Problem 36
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

# sieve the base 10's
# check sieved numbers base 2
# sum those that are plaindromic for both

# 101
# 111
# 121
# 131
# 141
# ...
# 191
# 202
# ...
# 303
# ...
# ...
# 909
# ...
# 1001
# 1111
# 1221
# 1331
# ...
# ...
# 9999
# 10001
# 10101
# ...
# ...

import sys
import time

def timing_func(fut):
    # times the function under test
    def wrapper(*args, **kwargs):
        time_start = time.time()
        fut_retval = fut(*args, **kwargs)
        time_end = time.time()
        print("runtime: " + str(time_end - time_start))
        return fut_retval
    return wrapper

def check_palindrome(word):
    for k in range(len(word) // 2):
        if word[k] != word[-1 - k]:
            return False
    return True
    
def sieve_base_10(ceil_val = 1000000):
    # it would be more efficient to generate the palindrome numbers 
    # and only check those in base 2 (or vice-versa).
    for i in range(1, ceil_val + 1, 2):
        # yield i if word[k] == word[-1 - k] for k in range(len(word) // 2)
        if check_palindrome(str(i)):
            yield i

def check_base_2(num_base_10):
    return check_palindrome("{0:b}".format(num_base_10))


@timing_func
def p36(ceiling_val):
    sum_palindromes = 0
    for i in sieve_base_10(ceiling_val):
        if check_base_2(i):
            sum_palindromes += i
            print(str(i) + " : " + "{0:b}".format(i))
    print("palindromes sum: " + str(sum_palindromes))

    
def main(args):
    USAGE_MSG = "usage: ./p36 (ceiling_value > 0)"
    ceiling_val = 1000000
    if len(args) == 1:
        pass
    elif len(args) == 2:
        ceiling_val = int(args[1])
        if ceiling_val < 1:
            print(USAGE_MSG)
            sys.exit(1)
    else:
        print(USAGE_MSG)
        sys.exit(1)
    p36(ceiling_val)


if __name__ == "__main__":
    main(sys.argv)
