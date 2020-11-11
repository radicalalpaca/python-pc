# import files here
import math


# Function to generate primes by Eratosthenes' sieve
def eratosthenes(max_prime):
    primes = list(range(2, max_prime + 1))
    for i in primes:
        j = 2
        while i * j <= primes[-1]:
            if i * j in primes:
                primes.remove(i * j)
            j += 1
    return primes


# 5A Write your functions below
# E.g., a function which takes an integer and squares it
# def semiprime_factorisation1

def semiprime_factorisation1(n):
    possible_factors = eratosthenes(n)
    for i in possible_factors:
        for j in possible_factors:
            if i * j == n:
                return i, j
    return None


def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


## DO NOT CHANGE THE FUNCTION NAMES!! ##

def euler_phi(n):
    counter = 0
    for i in range(1, n):
        if hcf(i, n) == 1:
            counter += 1
    return counter


def semiprime_factorisation2(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return i, n // i


def prime_factorisation(n):
    divisors = []
    i = 2
    start = n
    while i * i <= start:
        while n % i == 0:
            divisors.append(i)
            n //= i
        i += 1
    return divisors
