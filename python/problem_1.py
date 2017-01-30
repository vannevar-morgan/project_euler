#! /usr/bin/env python3

def problem_1(n = 1000):
    """
       Project Euler Problem 1
       
       If we list all the natural numbers below 10 that are multiples of 3 or 5, 
       we get 3, 5, 6 and 9. The sum of these multiples is 23.
       
       Find the sum of all the multiples of 3 or 5 below 1000.
    """
    
    mults_sum = 0
    
    for i in range(3, n):
        if i % 3 == 0 or i % 5 == 0:
            mults_sum += i
        
    return mults_sum


PROBLEM_STATEMENT = "Project Euler Problem 1\n\n\tIf we list all the natural numbers below 10 that are multiples of 3 or 5,\n\twe get 3, 5, 6 and 9. The sum of these multiples is 23.\n\n\tFind the sum of all the multiples of 3 or 5 below 1000."

print(PROBLEM_STATEMENT)
print("\n\n" + str(problem_1()))
