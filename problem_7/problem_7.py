#! /usr/bin/env python3

def calc_prime_n(n = 10001):
    """
    Project Euler Problem 3

    Calculates the nth prime number (For Problem 7, n = 10001).
    """
    nth_prime = 2
    for i in range(1, n):
        nth_prime = find_next_prime(nth_prime)
    
    return nth_prime

def find_next_prime(n):
    """
    Returns the next prime after n.
    """
    n += 1
    if n == 2:
        return n

    if n % 2 == 0:
        n += 1

    while True:
        if is_prime(n):
            return n
        else:
            n += 2

def is_prime(n):
    """
    Returns True if n is prime, False otherwise
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
            
PROBLEM_STATEMENT = "Project Euler Problem 3\n\n\tCalculates the nth prime number (For Problem 7, n = 10001)."

print(PROBLEM_STATEMENT)
print("\n" + str(calc_prime_n()))
