#! /usr/bin/env python3

import time
from bitarray import bitarray
from functools import lru_cache


def sieve_primes(bit_array):
    """
    sieve for primes using bitarray representation
    """
    bit_array.setall(True)
    bit_array[0] = False
    bit_array[1] = False
    begin = 2
    size = len(bit_array)
    for i in range(begin, size):
        if bit_array[i]:
            j = i
            while True:
                j += i
                if j >= size:
                    break
                bit_array[j] = False
    
"""
I have a bad habit of trying to do more than the problem statement requires.
I like to see all solutions (for example, all amicable numbers within the limit, or all divisors)
even if the problem only requires the sum of those numbers.

Obviously it's more efficient to simply return the sum of the divisors rather than the list of the divisors (and avoid appending to that list).

Using lru_cache was suggested here:
https://codereview.stackexchange.com/questions/202783/project-euler-problem-21-in-python-summing-amicable-numbers

Tested to run in ~0.05 seconds.
"""    
@lru_cache(None)
def sum_proper_divisors(n):
    """
    return proper divisors of n
    """
    ret = 1
    for i in range(2, int(n**0.5)):
        if n%i == 0:
            ret += i
            temp = n // i
            if temp > i:
                ret += temp
    return ret


def main():
    """
    Project Euler, Problem 21
    Amicable numbers

    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
    
    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
    
    Evaluate the sum of all the amicable numbers under 10000.
    """
    start_time = time.time()
    # amis = []
    amis_sum = 0
    max_n = 10000
    # primes = bitarray(max_n)
    # sieve_primes(primes)
    for i in range(1,max_n):
        # if primes[i]:
            # continue # exclude primes since they cannot be amicable numbers
        # if i in amis:
            # continue
        j = sum_proper_divisors(i)
        if i == j or j >= max_n:
            continue
        if i == sum_proper_divisors(j):
            amis_sum += i
            # amis_sum += j
            # amis.append(i)
            # amis.append(j)
    elapsed_time = time.time() - start_time
        
    # print(amis)
    # print(sum(amis))
    print(amis_sum)
    print("elapsed time: " + str(elapsed_time))




if "__main__" == __name__:
    main()
