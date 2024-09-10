#!/usr/bin/env python
# coding: utf-8

# # Problem 3 - Largest Prime Factor
# 
# https://projecteuler.net/problem=3
# 
# The rpime factors of 13195 are 5, 7, 13, and 29.
# 
# What is the largest prime factor of the number 600851475143?

# In[1]:


# The prime number that we are factorizing
target_prime = 600851475143


# ## Prime Theory
# 
# - Each number is either a prime number or the factor of primes (see Fundamental
# Theorem of Arithmetic).
# - No *efficient* algorithm exists for factorizing primes which is why
# cryptographic algorithms like RSA are powerful

# ## Ideas
# 
# - We could just manually find all prime factors...but that sounds like a bad
# idea.
# - I found the General Number Field Sieve (GNFS) which is promising though!
#   - It can factor integers larger than $10^{100}$
# 

# In[ ]:


# Before looking at the GNFS, Wikipedia suggests looking at the Rational Sieve
# which is less efficient but is easier to conceptually understand (there is
# even the Special Number Field Sieve lol).
# All the sieves have the common purpose of factoring integers into prime
# factors.

