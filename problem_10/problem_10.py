#! /usr/bin/env python3

import time


def get_prefilter_list(n):
    """
    return a list of possible primes <= n
    NOTE:
      All primes except 2, 3 end in 1 or 5 expressed in base 6.
    """
    ret = []
    if n >= 2:
        ret.append(2)
    if n >= 3:
        ret.append(3)
    i = 5
    while True:
        if i > n:
            break
        ret.append(i)
        i += 2
        if i > n:
            break
        ret.append(i)
        i += 4
    return ret


def sieve2(data, limit):
    """
    sieve data to remove non-primes.
    """
    sdata = {i:0 for i in data}
    sieve_index = 0
    while True:
        s = data[sieve_index]
        if s**2 > limit:
            break
        for i in range(sieve_index + 1, len(data)):
            if data[i]%s == 0:
                del sdata[data[i]]
        sieve_index += 1
        data = [*sdata]
        if sieve_index == len(data) - 1:
            break
    return data


def main():
    """
    Project Euler, Problem 10
    Summation of Primes
    Find the sum of all the primes below 2 million.

    NOTE:
      There are better solutions with superior runtimes.
      My sieving is less efficient computationally and wrt memory.
      Was originally implemented purely with a list but list has linear deletion;
      Complemented list with a map for average constant time deletion.
      But this approach requires reassigning the list on each iteration of the sieve.

      ALTERNATIVE:
      Using a bitarray representation of primes is particularly efficient and has some cpu caching advantages.
    """
    start = time.time()
    limit = 2000000
    print("getting search space")
    search_space = get_prefilter_list(limit)
    temp = search_space[2:]
    print("sieving")
    temp = sieve2(temp, limit)
    print("finished sieving")
    sieved = search_space[:2]
    sieved.extend(temp)
    elapsed = time.time() - start
    print("sum of primes less than " + str(limit) + ": " + str(sum(sieved)))
    print("elapsed time: " + str(elapsed))


if "__main__" == __name__:
    main()
