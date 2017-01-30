#! /usr/bin/env python3

def get_smallest_multiple(interval = [1,20]):
    """
    Project Euler Problem 5

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    -----------
    Smallest positive number evenly divisible by all numbers in [a,b] is the multiple of the highest number
    of prime factors for all prime factors in the interval.

    e.g.,

    For [1,5] the smallest multiple is: 2 * 3 * 2 * 5 = 60
    prime factors:
    2 = 2
    3 = 3
    4 = 2 * 2
    5 = 5

    Therefore, 2 * 3 * 2 * 5 = 2 * 3 * 2 * 5, not 2 * 3 * 2 * 2 * 5
    """
    low = interval[0]
    high = interval[1]

    factors = {}
    for i in range(low, high+1):
        prime_factors = get_prime_factors(i)
        prime_dict = {}
        for prime in prime_factors:
            if prime_dict.get(prime):
                prime_dict[prime] += 1
            else:
                prime_dict[prime] = 1

        primes = prime_dict.keys()
        for prime in primes:
            if factors.get(prime):
                if factors[prime] < prime_dict[prime]:
                    factors[prime] = prime_dict[prime]
            else:
                factors[prime] = prime_dict[prime]

    smallest_mult = 1
    keys = factors.keys()
    for prime in keys:
        smallest_mult *= (prime ** factors[prime])
        
    return smallest_mult


def get_prime_factors(num, prime_set_size = 1):
    """
    Returns the prime factors of a number.

    Input:
       Integer > 1
    Output:
       List representing the prime factors of the number.
    """
    prime_factors = []
    prime_begin = 2
    while num > 1:
        primes = get_primes(prime_begin, prime_set_size)
        index = 0
        while(index < len(primes)):
            if (num % primes[index]) == 0:
                prime_factors.append(primes[index])
                num = num / primes[index]
            else:
                index += 1
        prime_begin = primes[index - 1] + 1
    
    return prime_factors


def get_primes(prime_begin, prime_set_size):
    """
    Returns a list of primes of length prime_set_size, starting at prime_begin.
    """
    primes = []
    if is_prime(prime_begin) and prime_set_size > 0:
        primes.append(prime_begin)
    
    while len(primes) < prime_set_size:
        prime_begin = find_next_prime(prime_begin)
        primes.append(prime_begin)
    
    return primes


def find_next_prime(begin = 1):
    """
    Returns the next prime after begin.
    """
    begin += 1
    if begin == 2:
        return begin
    
    if (begin % 2) == 0:
        begin += 1
    
    while True:
        if is_prime(begin):
            return begin
        else:
            begin += 2


def is_prime(num):
    """
    Returns True if num is prime, false otherwise.
    """
    if num < 2:
        return False
    
    i = 2
    while i <= int(num ** 0.5):
        if (num % i) == 0:
            return False
        else:
            i += 1
    
    return True


PROBLEM_STATEMENT = "Project Euler Problem 5\n\n2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.\nWhat is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?\n-----------\nSmallest positive number evenly divisible by all numbers in [a,b] is the multiple of the highest number\nof prime factors for all prime factors in the interval.\n\ne.g.,\n\nFor [1,5] the smallest multiple is: 2 * 3 * 2 * 5 = 60\nprime factors:\n2 = 2\n3 = 3\n4 = 2 * 2\n5 = 5\n\nTherefore, 2 * 3 * 2 * 5 = 2 * 3 * 2 * 5, not 2 * 3 * 2 * 2 * 5"


print(PROBLEM_STATEMENT)
print("\n\n" + str(get_smallest_multiple()))
