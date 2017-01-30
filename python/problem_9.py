#! /usr/bin/env python3

def pythag_triplet(a, sum_val):
    """
    Returns a pair consisting of the first triplet found and the product of its triplet values.

    The triplet is found using a as the first triplet value, sum_val as the value for the triplet to sum to.

    If no triplet is found then a pair is returned consisting of:
    >an empty list
    >-1
    """
    for i in range(a, sum_val - 1):
        for j in range(i, sum_val):
            c = sum_val - i - j
            if i**2 + j**2 == c**2:
                return [[i, j, c], i*j*c]
    return [[], -1]


PROBLEM_STATEMENT = "Project Euler Problem 9\n\n\tA Pythagorean triplet is a set of three natural numbers, a < b < c, for which,\n\ta^2 + b^2 = c^2\n\n\tFor example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.\n\n\tThere exists exactly one Pythagorean triplet for which a + b + c = 1000.\n\tFind the product abc."


print(PROBLEM_STATEMENT)
[triplet, product] = pythag_triplet(6, 1000)
print("\nproduct(" + str(triplet) + ") = " + str(product))
