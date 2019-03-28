#! /usr/bin/env python3

def main():
    """
    project euler problem 39
    
    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
    
    {20,48,52}, {24,45,51}, {30,40,50}
    
    For which value of p ≤ 1000, is the number of solutions maximised?
    """
    keys = range(1,1001)
    vals = [0]*1000
    p_lens = dict(zip(keys, vals))

    # NOTE: Problem does not specify if {a,b,c} describes a unique solution for all permutations of {a,b,c} -- this solution counts all permutations as a unique solution.  The value of P will be correct but the count may be double of other solutions.
    # NOTE: It is not necessary to check all side lengths to 1000, obviously those can't satisfy the perimeter constraint, p = 1000, for larger side lengths.  You can save iterations by calculating a limit for the inner loop, assuming {a,b,c} == {b,a,c}
    for i in range(1,1001):
        for j in range(1,1001):
            if i + j > 1000:
                continue
            c2 = i**2 + j**2
            c = c2 ** 0.5
            if c % 1 != 0:
                continue
            if i + j + c > 1000:
                continue
            p_lens[i + j + c] += 1

    index = 0
    count = 0
    for i in range(1,1001):
        if p_lens[i] > count:
            count = p_lens[i]
            index = i
    print("there are " + str(count) + " solutions for p = " + str(index))



if __name__ == "__main__":
    main()
