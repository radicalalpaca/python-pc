# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:27:46 2020

@author: amtrjs
"""


# Ex 3 solutions
# No need to import any libraries
# or modules this week!
# Please make sure your file runs,
# and submit only your .py file
#
# 3Ai
# greatestgcd
def Euclid(a, b):
    if b == 0:
        return a
    else:
        return Euclid(b, a % b)


def greatestgcd(a, b, c):
    results = [Euclid(a, b), Euclid(a, c), Euclid(b, c)]
    return max(results)


# 3Aii
# evenodd
def evenodd(a):
    if a % 2 == 0:
        return True
    else:
        return False


# 3Aiii
# listelements
def listelements(input_list):
    if len(input_list) < 4:
        return False
    else:
        return [input_list[0], input_list[1], input_list[-2], input_list[-1]]


# 3Aiv
# double
def double(input_list):
    return [2 * i for i in input_list]


# 3Av
# isprime
def isprime(n):
    i = 3
    while n % 2 == 0:
        return False
    while i ** 2 <= n:
        if n % i == 0:
            return False
        else:
            i += 2
    return True


# 3Bi
# dectobin
def dectobin(n):
    binary = []
    while n > 0:
        binary.append(n % 2)
        n //= 2
    binary.reverse()
    return binary


# 3Bii
# bintodec(binary):
def bintodec(binary):
    result = 0
    binary.reverse()
    for i in range(len(binary)):
        result += (2 ** i) * binary[i]
    return result


# 3C
# eratosthenes
def eratosthenes(n):
    multiples = []
    primes = []
    for i in range(2, n + 1):
        if i not in multiples:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                multiples.append(j)
    return primes


# 3C
# primesbetween
def primesbetween(n, m):
    j = 0
    for i in eratosthenes(m):
        if i >= n:
            j += 1
    return j


# 3D
# sundaram(n):
def sundaram(n):
    integers = list(range(1, n + 1))
    for j in range(1, n + 1):
        for i in range(1, j + 1):
            if i + j + 2 * i * j in integers:
                integers.remove(i + j + 2 * i * j)
    return [2 * i + 1 for i in integers]
