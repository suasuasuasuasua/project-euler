#!/usr/bin/env python
# coding: utf-8

# # Problem 1 - Multiples of 3 or 5
# 
# https://projecteuler.net/problem=1
# 
# If we list all the natural numbers below that are multiples of 3 or 5, we get 3,
# 5, 6, and 9. The sum of these multiples is 23. Find the sum of all the multiples
# of 3 or 5 below 1000. 

# %% Setup
n = 1000

# %% Filter all numbers that are not divisible by 3 and 5
multiples = (i for i in range(n) if i % 3 == 0 or i % 5 == 0)

# %% Calculate the sum of all the multiples
answer = sum(multiples)

# %% Final Answer
print(f"The answer is {answer}")
