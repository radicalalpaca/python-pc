# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:25:52 2019

@author: amtrjs
"""

## Please don't change function names!

import numpy as np
import matplotlib.pyplot as plt


########
# Part 1
# 

# Q1a
def pi_gl(n):
    pi_approx = 0
    for i in range(n):
        pi_approx += ((-1) ** i) * (1 / (2 * i + 1))
    return 4 * pi_approx


# Q1b
def pi_nik(n):
    pi_approx = 3
    for i in range(1, n):
        pi_approx += (4 * (-1) ** (i + 1)) / (2 * i * (2 * i + 1) * (2 * i + 2))
    return pi_approx


# Q1c
def pi_wallis(n):
    pi_approx = 1
    for i in range(1, n + 1):
        pi_approx *= (2 * i / (2 * i - 1)) * (2 * i / (2 * i + 1))
    return 2 * pi_approx


# Q1d
def plot_error(method):
    method_error = []
    for i in range(1, 501):
        method_error.append(abs(method(i) - np.pi))
    plt.loglog(range(1, 501), method_error, label=method.__name__)


for pi_method in [pi_gl, pi_nik, pi_wallis]:
    plot_error(pi_method)
plt.ylabel("Error")
plt.xlabel("n")


# Q1e
# Add answers as comments:
# The gradient of each line on the log-log plot gives the rate of convergence for that sequence.
# So pi_nik has the fastest rate of convergence, followed by pi_wallis and pi_gl.

########
# Part 2
#
def isprime(n):
    i = 3
    if n == 2:
        return True
    while n % 2 == 0:
        return False
    while i ** 2 <= n:
        if n % i == 0:
            return False
        else:
            i += 2
    return True


def first_n_primes(n):
    primes = []
    i = 3
    while len(primes) != n:
        if isprime(i):
            primes.append(i)
        i += 1
    return primes


def round_to_4(x):
    return 4 * round(x / 4)


def prime_factorisation(n):
    divisors = []
    i = 2
    while i <= n:
        if n % i == 0:
            divisors.append(i)
            n //= i
        else:
            i += 1
    return divisors


def find_sign(n):
    # Returns True if positive.
    positive_sign = True
    if n == 2:
        return positive_sign
    if isprime(n):
        if n - round_to_4(n) > 0:
            positive_sign = False
    else:
        signs = 0
        for prime_factor in prime_factorisation(n):
            if not find_sign(prime_factor):
                signs += 1
        if signs % 2 == 0:
            positive_sign = True
        else:
            positive_sign = False
    return positive_sign


# Q2a 
def pi_euler1(n):
    pi_approx = 1
    for prime in first_n_primes(n):
        pi_approx *= (prime / round_to_4(prime))
    return 4 * pi_approx


# Q2b
def pi_euler2(n):
    pi_approx = 1
    for i in range(2, n + 1):
        if find_sign(i):
            pi_approx += 1 / i
        else:
            pi_approx -= 1 / i
    return pi_approx


# Q2c
# The second Euler method converges slower than any of the other methods, while the first Euler
# method converges at a similar rate to pi_gl and pi_wallis.
for pi_method in [pi_euler1, pi_euler2]:
    plot_error(pi_method)


# Q2d
def montecarlo(M):
    i = 0
    hits = 0
    for j in range(M):
        x, y = np.random.uniform(0, 1), np.random.uniform(0, 1)
        i += 1
        if (x - 1 / 2) ** 2 + (y - 1 / 2) ** 2 <= 1 / 4:
            hits += 1
    return 4 * (hits / i)


# Q2e
def montecarlo_accuracy(eps):
    pi_approx = 0
    n = 1
    while abs(pi_approx - np.pi) >= eps:
        pi_approx = montecarlo(n)
        n += 1
    return pi_approx, n


# Add answers as comments
# The rate of convergence is a random variable, it changes each time the monte carlo method is run.
# The variance of the random variable is what matters for the rate of convergence.


##############
# Part 3 below
#

def gauss_legendre(n):
    a, b, t, p = 1, 1 / np.sqrt(2), 1 / 4, 1
    for i in range(n):
        an = (a + b) / 2
        b = np.sqrt(a * b)
        t -= p * (a - an) * (a - an)
        a, p = an, 2 * p
    return ((a + b) ** 2) / (4 * t)


plot_error(gauss_legendre)
plt.legend()
plt.show()
# The Gauss-Legendre algorithm is much faster than all the other algorithms tested,
# giving a more accurate result after just a few iterations.
