#! /usr/bin/env python3.6

import time


def collatz(n, collatz_map):
    """
    Calculate Collatz sequence with C_0 = n
    """
    if n in collatz_map:
        return
    seq = [n]
    index = n

    while True:
        if n%2 == 0:
            n = int(n / 2)
        else:
            n = int(3*n + 1)
        seq.append(n)
    
        if n == 1:
            collatz_map[index] = seq
            break
        elif n in collatz_map:
            seq.extend(collatz_map[n][1:])
            collatz_map[index] = seq
            break

    # for i in range(len(seq)):
    #     if seq[i] <= index:
    #         continue
    #     if seq[i] not in collatz_map:
    #         collatz_map[seq[i]] = seq[i:]
            

def main():
    """
    Project Euler, Problem 14
    Longest Collatz Sequence
    Which starting number, under one million, produces the longest chain?
    """
    collatz_map = {}
    longest = []
    longest_seq_len = 0

    start = time.time()
    for n in range(1, 1000000):
        collatz(n, collatz_map)
        seq_len = len(collatz_map[n])
        if seq_len > longest_seq_len:
            longest.clear()
            longest.append(n)
            longest_seq_len = seq_len
        elif seq_len == longest_seq_len:
            longest.append(n)
    time_total = time.time() - start
    print("seeds for longest seq:" + str(longest))
    print("length is " + str(longest_seq_len))
    print("time to calculate: " + str(time_total))


if "__main__" == __name__:
    main()
