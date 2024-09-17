#!/usr/bin/env python
# coding: utf-8

# # Problem 4 - Largest Palindrome Product
#
# https://projecteuler.net/problem=4
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is $9009 = 91 * 99$
#
# Find the largest palindrome made from the product of 3-digit numbers.

# Ideas
# The product of two 3-digit numbers can range from 100*100 = 10,000 (5 digits)
# to 999*999 = 998,001 (6 digits)
#
# A naiive solution might be to just check 100*100, then 100*101 onward to find
# palindromes, and iteratively updating the largest number
#
# Another interesting idea is to enumerate all the possible palindromes, then
# factorize the number.


def is_palindrome(n: int) -> bool:
    s = str(n)
    midpoint, remainder = divmod(len(s), 2)

    if remainder:
        # If digits in n is odd, then we don't need to check the midpoint
        #
        # XYZYX
        lhs, rhs = s[:midpoint], s[midpoint + 1 :]
    else:
        # Otherwise, if the number was a palindrome, it would look like
        #
        # XYZZYX
        lhs, rhs = s[:midpoint], s[midpoint:]

    # Check if the lefthand and righthand side are the same (if one is reversed)
    return lhs == rhs[::-1]


# Generate all the palindromes between some ranges
lower, upper = 100, 999
lower_bound = lower ** 2
upper_bound = upper ** 2

palindromes = [
    i for i in range(lower_bound, upper_bound+1) if is_palindrome(i)
]

# Find all valid palindromes for this problem space (because I'm extra)
valid_palindromes = dict()

# Find all valid palindromes -- ones that can be factorized into two 3-digit
# numbers
for palindrome in palindromes:
    # Loop over each number in the bound
    for i in range(lower, upper+1):
        d, r = divmod(palindrome, i)

        # Ensure that the palindrome, if it is divisible, can be factored into
        # 3-digit number exclusively
        if r == 0 and lower < d < upper:
            valid_palindromes.setdefault(palindrome, (d, i))

largest_palindrome = max(valid_palindromes.keys())

# %% The final answer
print(f"The answer is {largest_palindrome}")
