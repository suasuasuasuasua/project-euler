#!/usr/bin/env python
# coding: utf-8

# # Problem 6 - Sum Square Difference
#
# https://projecteuler.net/problem=6
#
# The sum of the squares of the first ten natural numbers is,
#   $$
#       1^2 + 2^2 + ... + 10^2 = 385
#   $$
#
# The square of the sum of the first ten natural numbers is,
#   $$
#       (1 + 2 + ... + 10)^2 = 55^2 = 3025
#   $$
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is $3025 - 385 = 2640$.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


# First one hundred natural numbers
n = 100
numbers = [i for i in range(1, n+1)]

sum_square = sum(i**2 for i in numbers)
square_sum = sum(numbers)**2

difference = abs(sum_square - square_sum)

print(f"The final anwer is {difference}")
