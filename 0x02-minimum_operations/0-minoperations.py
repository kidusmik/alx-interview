#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    return the min operation that takes to write h n times
    """

    if not isinstance(n, int):
        return 0

    cp = last = 0
    h = 1
    while h < n:
        rest = n - h
        if rest % h == 0:
            last = h
            h += last
            cp += 2
        else:
            h += last
            cp += 1

    return cp
