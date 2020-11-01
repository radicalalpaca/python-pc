import numpy as np


def divisorGenerator(n):
    divisors = []
    for i in range(1, int(np.sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return divisors


def sumdivisors(n):
    return sum(divisorGenerator(n)) - n


amicable_numbers = []
for j in range(10001):
    if sumdivisors(sumdivisors(j)) == j and sumdivisors(j) != j:
        amicable_numbers.append(j)


print(sum(amicable_numbers))

