#!/usr/bin/python3
"""Module 0-minoperations"""


def minOperations(n):
    """ calculates minimum number of ops needed to result"""
    if (n > 1):
        primes = []

        while (n > 1):
            leastFactor = primeFactors(n)

            primes.append(leastFactor)

            n = int(n / leastFactor)

        return (sum(primes))
    else:
        return (0)


def primeFactors(n):
    """Get the least prime factor of an integer"""

    isPrime = False

    for i in range(1, (n + 1)):
        for j in range(1, i):
            isPrime = False
            if (i % j == 0 and j != 1 and j != i):
                isPrime = True
                break
        if (i != 1 and isPrime is False and n % i == 0):
            return (i)
