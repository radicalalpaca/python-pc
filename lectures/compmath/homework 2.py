# import math
#
# def cubed(x):
#     return x ** 3
#
#
# def meanpair(x, y):
#     return 0.5 * (x + y)
#
#
# def pyth(a, b, c):
#     if c ** 2 == a ** 2 + b ** 2:
#         return True
#     else:
#         return False
#
#
# def meanlist(list):
#     return sum(list) // len(list)
#
#
# def mygcd(a, b):
#     return math.gcd(a, b)
#
#
# def meanpair_or_gcd(a, b):
#     values = [meanpair(a, b), 2 * mygcd(a, b)]
#     return max(values)
#
# def Euclid(a,b):
#     if b == 0:
#         return a
#     else:
#         return Euclid(b, a%b)
#
#
# def ExtEuclid(a,b):
#     r_0, r_1 = a, b
#     x_0, x_1 = 1, 0
#     y_0, y_1 = 0, 1
#     while r_1 != 0:
#         q = r_0 // r_1
#         r_0, r_1 = r_1, r_0 - q * r_1
#         x_0, x_1 = x_1, x_0 - q * x_1
#         y_0, y_1 = y_1, y_0 - q * y_1
#     return (r_0, x_0, y_0)
#
# def CountEuclid(a,b):
#     n_steps = 0
#     r_0, r_1 = a, b
#     x_0, x_1 = 1, 0
#     y_0, y_1 = 0, 1
#     while r_1 != 0:
#         n_steps += 1
#         q = r_0 // r_1
#         r_0, r_1 = r_1, r_0 - q * r_1
#         x_0, x_1 = x_1, x_0 - q * x_1
#         y_0, y_1 = y_1, y_0 - q * y_1
#     return (r_0, n_steps)
#
# print(CountEuclid(375, 279))
