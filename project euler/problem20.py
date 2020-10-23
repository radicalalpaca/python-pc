import numpy as np

def factorial_digit_sum(n):
    num = np.math.factorial(n)
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

print(factorial_digit_sum(100))

