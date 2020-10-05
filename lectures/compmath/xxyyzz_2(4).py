import math


# Template file for Week 2
# Lines that start with '#'
# are comments and are ignored
# by Python.

# 2A Write your functions below
# Example, a function which takes an integer and squares it:
def squared(x):
    xx = x ** 2
    return xx


## DO NOT CHANGE THE FUNCTION NAMES!! ##
# (i)  
def cubed(x):
    return x ** 3


# (ii)
def meanpair(x, y):
    return 0.5 * (x + y)


# (iii)
def pyth(a, b, c):
    if c ** 2 == a ** 2 + b ** 2:
        return True
    else:
        return False


# (iv) 
def meanlist(input_list):
    return sum(input_list) / len(input_list)


# (v) 
def mygcd(a, b):
    return math.gcd(a, b)


# (vi)
def meanpair_or_gcd(a, b):
    values = [meanpair(a, b), 2 * mygcd(a, b)]
    return max(values)


# 2B Insert your Euclidean algorithm program lines here:
def Euclid(a, b):
    if b == 0:
        return a
    else:
        return Euclid(b, a % b)


# 2C Insert your extended Euclidean algorithm here:
def ExtEuclid(a, b):
    r_0, r_1 = a, b
    x_0, x_1 = 1, 0
    y_0, y_1 = 0, 1
    while r_1 != 0:
        q = r_0 // r_1
        r_0, r_1 = r_1, r_0 - q * r_1
        x_0, x_1 = x_1, x_0 - q * x_1
        y_0, y_1 = y_1, y_0 - q * y_1
    return r_0, x_0, y_0


# 2D Insert your counting-steps Euclid program here:
def CountEuclid(a, b):
    n_steps = 0
    r_0, r_1 = a, b
    x_0, x_1 = 1, 0
    y_0, y_1 = 0, 1
    while r_1 != 0:
        n_steps += 1
        q = r_0 // r_1
        r_0, r_1 = r_1, r_0 - q * r_1
        x_0, x_1 = x_1, x_0 - q * x_1
        y_0, y_1 = y_1, y_0 - q * y_1
    return r_0, n_steps
