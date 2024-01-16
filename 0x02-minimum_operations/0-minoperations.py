#!/usr/bin/python3
"""
Module 0-minoperations
"""


def minOperations(n):
    """
    In a text file, there is a single character H.r 
    """
    operation = 0
    if n < 2:
        return 0
    for i in range(2, n + 1):
        while(n % i == 0):
            operation += i
            n /= i
            if n < i:
                break
    return operation
