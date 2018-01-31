#! /usr/bin/env python3

def problem_4(digits = 3):
    """
       Project Euler Problem 4
	
       A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

       Find the largest palindrome made from the product of two 3-digit numbers.
    """

    if digits < 1:
        raise ValueError("specified digits is out of range...cannot generate palindrome numbers with less than one digit...")

    # i'm sure there is a mathematical property that could be used to reduce numbers to search, but I don't know it off the
    # top of my head so I'm just going to bruteforce because I want to solve it myself.
    # for 2 digits I can see that 99*91 = palindrome, 99*82 = palindrome, 99*73 = palindrome.... not sure for 3 digits.
    
    a = b = int("9" * digits) # largest number with digits number of digits
    c = int("1" + "0" * (digits - 1)) # smallest number with digits number of digits

    # find all palindrome numbers with factors with digits number of digits
    factor1 = []
    factor2 = []
    palindromes = []
    for i in range(a, c, -1):
        for j in range(b, c, -1):
            if is_number_palindrome(i*j):
                palindromes.append(i*j)
                factor1.append(i)
                factor2.append(j)

    # return if there were no palindromes found
    if len(palindromes) <= 0:
        print("no palindromes exist with factors with digits = " + str(digits))
        return

    # find the index of all palindrome numbers equal to the maximum palindrome number
    max_val = max(palindromes)
    indexes = []
    for i in range(0, len(palindromes)):
        if palindromes[i] == max_val:
            indexes.append(i)

    # print the factors and the maximum palindrome number
    print("\nMaximum palindrome number with factors of " + str(digits) + " digits is: " + str(max_val))
    print("Factors are: ")
    for i in range(0, len(indexes)):
        index = indexes[i]
        print(str(factor1[index]) + " x " + str(factor2[index]))
    
    """
    # print all palindrome numbers with factors of specified number of digits
    print("\nAll palindrome numbers in the range:")
    for i in range(0, len(palindromes)):
        print(str(factor1[i]) + " x " + str(factor2[i]) + " = " + str(palindromes[i]))
    """
    unique_palindromes = set(palindromes)
    print("\nThere are " + str(len(unique_palindromes)) + " palindromes with factors with " + str(digits) + " digits...")


def is_number_palindrome(n):
    """
      is_number_palindrome(n) returns True if n is a palindrome number, False otherwise.
    """
    word = str(n)
    if word == word[::-1]:
        return True
    else:
        return False


PROBLEM_STATEMENT = "Project Euler Problem 4\n\n\tA palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.\n\n\tFind the largest palindrome made from the product of two 3-digit numbers."

print(PROBLEM_STATEMENT)
problem_4()
