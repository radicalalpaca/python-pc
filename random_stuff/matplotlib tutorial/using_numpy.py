import matplotlib.pyplot as plt
import numpy as np


def f(t):
    return t**2 * (np.cos(t))

t1 = np.arange(-5.0, 5.0, 0.001)

plt.plot(t1, f(t1))

plt.show()
