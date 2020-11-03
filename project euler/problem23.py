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

def abundant(n):
    abundant_numbers = []
    for i in range(n):
        if sumdivisors(i) > i:
            abundant_numbers.append(i)
    return abundant_numbers

if __name__ == '__main__':
    numbers = abundant(14063)
    print(numbers)

