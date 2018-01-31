#! /usr/bin/env python3

def sum_square_diff(low, high, interval = 1):
    """
    Project Euler Problem 6

    Calculates the difference of the sum of the squares and the square of the
    sums of numbers in a specified range (For Problem 6, [1 - 100]).
    """
    num_range = range(low, high + 1, interval)
    sum_squares = sum([i ** 2 for i in num_range])
    squares_sum = sum(num_range) ** 2
    return squares_sum - sum_squares


PROBLEM_STATEMENT = "Project Euler Problem 6\n\n\tCalculates the difference of the sum of the squares and the square of the\n\tsums of numbers in a specified range (For Problem 6, [1 - 100])."

print(PROBLEM_STATEMENT)
print("\n" + str(sum_square_diff(1, 100)))
