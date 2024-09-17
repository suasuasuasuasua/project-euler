#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
from typing import Iterable
import functools as ft


# # Problem 5 - Smallest Multiple
#
# https://projecteuler.net/problem=5
#
# $2520$ is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
#
# What is the smallest positive number that is *evenly divisible* by all the
# numbers from 1 to 20?

# Ideas
# A naiive solution would be to check every positive integer and attempt to
# divide 1, 2, 3, ..., 20 and skipping any number that fails.
# Obviously this is a bad idea because we can search for an indeterminate
# amount of time.
#
# <stealing work from ./p3.py>

# An interesting note is that since the


def prod(l: Iterable) -> float:
    return ft.reduce(lambda x, y: x * y, l)


def is_prime(n: int):
    """Check if a number is prime. Naiive solution.

    Prime number: a whole number greater than 1 that cannot be exactly divided
    by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).

    A naiive solution is to check every single prime number that *could* compose
    the target prime.

    n (int): the number to check.
    """
    result = True

    for i in range(2, n // 2 + 1):
        d, m = divmod(n, i)

        if m == 0:
            result = False
            break

    return result


def prime_factorize(n: int):
    # Generate all the primes up to the square root of the number
    # We don't need to go farther than the square root of the prime
    # primes = (i for i in range(2, int(math.sqrt(n)) + 1) if is_prime(i))
    primes = (i for i in range(2, n + 1))
    # Track the factors in a dictionary
    factors = defaultdict(int)

    if n <= 1:
        factors[n] = 1
        return factors

    # Destructively track the number and prime
    current_n = n
    current_prime = next(primes)

    while True:
        # Find the dividend and remainder from the current number and prime
        current_n, remainder = divmod(current_n, current_prime)
        if remainder == 0:
            factors[current_prime] += 1
            continue

        # Reset the dividing element
        current_n = (current_n * current_prime) + remainder

        if current_n < current_prime:
            break

        # Get the next prime if possible
        try:
            current_prime = next(primes)
        # If we run out of primes, then we've probably found all the factors
        except:
            break

    return factors


lower = 1
upper = 20

factors = defaultdict(int)

# Prime factorize each of the numbers in the range to calculate the least common
# multiple
for i in range(1, upper + 1):
    fs = prime_factorize(i)

    # For each of the factors, only update the factors dictionary if the count
    # is larger
    for k, v in fs.items():
        current = factors.get(k, 0)
        if v > current:
            factors[k] = v

least_common_multiple = 1
for k, v in factors.items():
    least_common_multiple *= k**v

# %% The final answer
print(f"The answer is {least_common_multiple}")
