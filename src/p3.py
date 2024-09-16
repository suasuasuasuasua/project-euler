#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
import math
import numpy as np

# # Problem 3 - Largest Prime Factor
#
# https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13, and 29.
#
# What is the largest prime factor of the number 600851475143?

# The prime number that we are factorizing
target_prime = 600_851_475_143

# ## Prime Theory
#
# - Each number is either a prime number or the factor of primes (see
#   Fundamental Theorem of Arithmetic).
# - No *efficient* algorithm exists for factorizing primes which is why
#   cryptographic algorithms like RSA are powerful

# ## Ideas
#
# - We could just manually find all prime factors...but that sounds like a bad
# idea.
# - I found the General Number Field Sieve (GNFS) which is promising though!
# - It can factor integers larger than $10^{100}$
#

# Before looking at the GNFS, Wikipedia suggests looking at the Rational Sieve
# which is less efficient but is easier to conceptually understand (there is
# even the Special Number Field Sieve lol).
# All the sieves have the common purpose of factoring integers into prime
# factors.


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


prime_factors = prime_factorize(target_prime)
largest_prime = max(prime_factors)


# %% The final answer
print(f"The answer is {largest_prime}")

# %% The final answer
print(f"The answer is {largest_prime}")
