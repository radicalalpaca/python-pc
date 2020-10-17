# import files here
import math


# 4A Write your functions below
# E.g., a function which takes an integer and squares it
# def squared 

def squared(x):
    xx = x ** 2
    return xx


## DO NOT CHANGE THE FUNCTION NAMES!! ##
# (1)  def twocubedplusone
def twocubedplusone(x):
    return 2 * (x ** 3) + 1


# (2) def sumanddiff
def sumanddiff(x, y):
    return x + y, abs(x - y)


# (3) def sin2cos2
def sin2cos2(x):
    return (math.cos(x) ** 2) + (math.sin(x) ** 2)


# (4) def lucas
def lucas(n):
    lucas_numbers = [2, 1]
    for i in range(3, n + 1):
        lucas_numbers.append(lucas_numbers[i - 2] + lucas_numbers[i - 3])
    return lucas_numbers


# (5) def polartocartesian
def polartocartesian(r, theta):
    return r * math.cos(theta), r * math.sin(theta)

# (6) def cartesiantopolar
def cartesiantopolar(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    if y >= 0 and r != 0:
        theta = math.acos(x / r)
    elif y < 0:
        theta = -math.acos(x / r)
    elif r == 0:
        return "undefined"
    return r, theta


## DO NOT CHANGE THE FUNCTION NAMES!!
# 4B
# 
# (1) def horner(x,coeffs):
def horner(x, coeffs):
    coeffs.reverse()
    b = 0
    for a in coeffs:
        b = a + x * b
    return b


# (2)
# e.g.,
# print(horner( ... ))
print(horner(4, [1, 5, 0, 1]))
print(horner(math.sqrt(3), [4, 0, -1]))

# Are the answers exact?
# (a) is exact, (b) is not exact

# (3)
# def hornerderiv
def hornerderiv(x, coeffs):
    coeffs.reverse()
    b = 0
    Q_coeffs = []
    for a in coeffs:
        b = a + x * b
        Q_coeffs.append(b)
    P_x = Q_coeffs.pop()
    Q_coeffs.reverse()
    Q_x = horner(x, Q_coeffs)
    return P_x, Q_x

# (4)
# e.g., 
# print(hornerderiv( ... ))
print(hornerderiv(1, [0, 0, 1, 5, 0, 0, 0, -1]))
print(hornerderiv(math.pi, [0, 0, 1, 5, 0, 0, 0, -1]))

# (5)
# e.g.
# print(horner( ... ))
print(horner((math.pi / 3), [0, 1, 0, - 1 / 6, 0, 1 / 125, 0, - 1 / 5040]))