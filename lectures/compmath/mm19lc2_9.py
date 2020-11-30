# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:59:26 2020

@author: amtrjs
"""

## I'm not asking for specific functions to be
## written this week - please organise your code
## neatly, so that it produces graphs when run,
## includes any answers or discussion as Python
## comments (like this one), and doesn't take more
## than about 10 seconds to run!

## By all means test your code with longer runs, but
## then turn the resolution down when submitting!

# you can use:
from box import boxcounting
# because the markers will also have this file

## Exercise 9A

from box import boxcounting
import matplotlib.pyplot as plt
import numpy as np


def forward_henon(x, y, a, b):
    return 1.0 - a * x * x + y, b * x


def plot_henon(a, b):
    xs = [0.1]
    ys = [0.2]
    for k in range(10000):
        x, y = forward_henon(xs[-1], ys[-1], a, b)
        xs.append(x)
        ys.append(y)
    plt.scatter(xs, ys, marker=".", s=1)
    return xs, ys


x_henon, y_henon = plot_henon(1.4, 0.3)
plt.show()
N_eps_list_henon = []
eps_list_henon = []

for eps in [x / 100 for x in range(99, 0, -1)]:
    N_eps_list_henon.append(boxcounting(x_henon, y_henon, eps)[1])
    eps_list_henon.append(boxcounting(x_henon, y_henon, eps)[0])

gradient_henon = (N_eps_list_henon[98] - N_eps_list_henon[70]) / (eps_list_henon[98] - eps_list_henon[70])
print(gradient_henon)
# The gradient is 1.2636963252919253. This is quite close to the true dimension of 1.261.
# To get a more accurate result, I could increase the number of points in the fractal set.
plt.plot(N_eps_list_henon, eps_list_henon)
plt.show()


def forward_ikeda(x, y, R, c_1, c_2, c_3):
    t = c_1 - (c_3 / (1 + x ** 2 + y ** 2))
    return R + c_2 * (x * np.cos(t) - y * np.sin(t)), c_2 * (x * np.sin(t) + y * np.cos(t))


def plot_ikeda(R, c_1, c_2, c_3):
    xs = [0.1]
    ys = [0.2]
    for i in range(10000):
        x, y = forward_ikeda(xs[-1], ys[-1], R, c_1, c_2, c_3)
        xs.append(x)
        ys.append(y)
    plt.scatter(xs, ys, marker=".", s=1)
    return xs, ys


x_ikeda, y_ikeda = plot_ikeda(1.0, 0.4, 0.9, 6.0)
plt.show()
N_eps_list_ikeda = []
eps_list_ikeda = []

for eps in [x / 100 for x in range(99, 0, -1)]:
    N_eps_list_ikeda.append(boxcounting(x_ikeda, y_ikeda, eps)[1])
    eps_list_ikeda.append(boxcounting(x_ikeda, y_ikeda, eps)[0])

gradient_ikeda = (N_eps_list_ikeda[90] - N_eps_list_ikeda[70]) / (eps_list_ikeda[90] - eps_list_ikeda[70])
print(gradient_ikeda)
# The box_counting dimension for the ikeda map is approximately 1.71.
