import time
import math


def count_factors(num):
    count = 2
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            count += 2
    return count


def triangle_number(num):
    return (num * (num + 1) // 2)


def divisors_of_triangle_number(num):
    if num % 2 == 0:
        return count_factors(num // 2) * count_factors(num + 1)
    else:
        return count_factors((num + 1) // 2) * count_factors(num)


def factors_greater_than_triangular_number(n):
    x = n
    while divisors_of_triangle_number(x) <= n:
        x += 1
    return triangle_number(x)


def main():
    start = time.time()
    print("The answer is", factors_greater_than_triangular_number(500))
    print("Answer found in", time.time() - start, "seconds")

main()

    

