#! /usr/bin/env python3

import operator
import functools

def greatest_product(number, series_length):
    """
    Project Euler Problem 8

    Returns the subseries of specified length that yield the greatest product, within a given series.

    Also returns the value of that product.
    e.g.,
    Input: 14592, series_length = 4
    Output: [4,5,9,2], 360
    """
    str_rep = str(number)
    series = [int(letter) for letter in str_rep]

    if len(series) == 0:
        return [series, 0]
    
    if series_length > len(series):
        raise ValueError("specified length of subseries is greater than the number of digits in the specified number...")
    elif series_length == len(series):
        series_product = functools.reduce(operator.mul, series)
        return [series, series_product]
    
    subseries = make_subseries(series, series_length)
    max_product = 0
    max_index = 0 # if series is allowed to contain negative numbers then max_product and max_index need to be handled differently...
    for i in range(0, len(subseries)):
        product = functools.reduce(operator.mul, subseries[i])
        if product > max_product:
            max_product = product
            max_index = i

    return [subseries[max_index], max_product]
        


def make_subseries(series, subseries_length):
    """
    Returns a list of subseries of length subseries_length, generated from series.
    
    e.g.,
    Input: [1,2,3,4,5], 2
    
    Output: [[1,2], [2,3], [3,4], [4,5]]
    """
    if len(series) == 0 and subseries_length == 0:
        return series
    if subseries_length <= 0:
        raise ValueError("specified subseries_length is <= 0...")
    if len(series) < subseries_length:
        raise ValueError("specified subseries_length exceeds the length of the given series...")

    subseries = []
    for i in range(0, len(series) - subseries_length + 1):
        subseries.append(series[i:i+subseries_length])
    
    return subseries



PROBLEM_STATEMENT = "Project Euler Problem 8\n\n\tReturns the subseries of specified length that yield the greatest product, within a given series.\n\n\tAlso returns the value of that product.\n\te.g.,\n\tInput: 14592, series_length = 4\n\tOutput: [4,5,9,2], 360"


a = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450


print(PROBLEM_STATEMENT)
print(greatest_product(a, 13))
