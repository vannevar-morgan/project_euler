#! /usr/bin/env python3

#
# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
#

from bitarray import bitarray
import math
import time


def get_primes(n):
    """
    return a bitarray representing all primes <= n
    """
    if n < 2:
        return bitarray()
    primes = bitarray("1"*(n+1))
    primes[0] = False
    primes[1] = False
    i = 2
    while i <= math.floor(n**0.5):
        if primes[i]:
            j = i * 2
            while j <= n:
                primes[j] = False
                j += i
        i += 1
    return primes


def get_digits(i):
    """
    return a list containing the digits of i
    """
    ret = []
    digits = []
    m = 10
    while True:
         d = i % m
         digits.append(d)
         i = i // m
         if i < 1:
             break
    return digits[::-1]


def digits_even(digits):
    """
    check if any digits are even, if so then a rotation using the digits cannot be prime because all rotations will include e.g., XXXXE
    """
    exclude = {0,2,4,6,8}
    for i in digits:
        if i in exclude:
            return True
    return False


def get_rotations(i):
    """
    return a list of all rotations of i e.g., 197 -> 197, 971, 719
    """
    j = str(i)
    n = len(j)
    rots = []
    for i in range(n):
        j = j[1:] + j[0]
        k = int(j[1:] + j[0])
        if k not in rots:
            rots.append(k)
    return rots


def check_primes(primes, rots):
    """
    return True if all rotations are prime, False otherwise
    """
    for i in rots:
        if not i in primes:
            return False
    return True


def main():
    """
    Project Euler, Problem 35
    """
    # find all primes < n, for n = 1000000
    # group primes by number of digits
    # generate rotations of primes
    # check if all of the rotations are also in the primes collection
    n = 999999
    t1_begin = time.time()
    primes = get_primes(n)
    sprimes = {2, 3, 5, 7}
    i = 11
    while True:
        if i > n:
            break
        if primes[i]:
            digits = get_digits(i)
            if not 5 in digits and not digits_even(digits):
                sprimes.add(i)
        i += 2
        if i > n:
            break
        if primes[i]:
            digits = get_digits(i)
            if not 5 in digits and not digits_even(digits):
                sprimes.add(i)
        i += 4
    
    lprimes = list(sprimes)
    cprimes = set()
    for i in lprimes:
        rots = get_rotations(i)
        if check_primes(sprimes, rots):
            cprimes.add(i)
    print("number of circular primes less than " + str(n + 1) + ":\t" + str(len(cprimes)))
    print("elapsed time:\t" + str(time.time() - t1_begin))


if __name__ == "__main__":
    main()
