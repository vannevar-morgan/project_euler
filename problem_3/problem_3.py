#! /usr/bin/env python3


def problem_3(n = 600851475143, prime_set_size = 100):
    """
       Project Euler Problem 3
       
       The prime factors of 13195 are 5, 7, 13 and 29.
       
       What is the largest prime factor of the number 600851475143 ?
    """
    import math
    
    if n < 2:
        return []
    elif is_prime(n):
        return [n]
    else:
        # prime_set_size specifies the number of primes to pre-generate.
        primes = get_n_primes(prime_set_size)
        prime_index = 0
        
        prime_factors = []
        while not is_prime(n):
            if n % primes[prime_index] == 0:
                prime_factors.append(primes[prime_index])
                n = n / primes[prime_index]
            else:
                prime_index += 1
                if prime_index == prime_set_size:
                    primes = get_n_primes(prime_set_size, primes[prime_index - 1] + 2)
                    prime_index = 0
            
        prime_factors.append(math.floor(n))
        return prime_factors
      
  



def get_n_primes(n, begin = 2):
    """
       get_n_primes(n, begin = 2) returns a list of the n primes starting from begin.
       If begin is not specified then it returns the n primes starting with prime[0] = 2
    """
    
    if n == 0:
        return []
  
    if begin < 0:
        begin = 2
  
    primes = []
    n_primes = 0
  
    if begin == 2:
        primes.append(begin)
        n_primes += 1
        begin += 1
    elif begin % 2 == 0:
        begin += 1
    
    while n_primes < n:
        if is_prime(begin):
            primes.append(begin)
            n_primes += 1
        begin += 2
  
    return primes
    

def is_prime(n):
    """
       is_prime(n) returns true if n is prime, false otherwise
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i < int(n**0.5) + 1:
            if n % i == 0:
                return False
            i += 2
        return True


PROBLEM_STATEMENT = "Project Euler Problem 3\n\n\tThe prime factors of 13195 are 5, 7, 13 and 29.\n\n\tWhat is the largest prime factor of the number 600851475143 ?"

print(PROBLEM_STATEMENT)
print("\n\n" + str(problem_3()))
