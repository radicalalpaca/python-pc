import numpy as np
import matplotlib.pyplot as plt

n = 100

ix = []
ir = []

for r in np.arange(3.5441, 3.57, 0.00001):
    x0 = 0.5
    x = x0
    xs = []
    ir.append(r)
    for i in range(n):
        x = r * x * (1 - x)
    for i in range(n):
        x = r * x * (1 - x)
        xs.append(x)
    ix.append(xs)

for xe, ye in zip(ir, ix):
    plt.scatter([xe] * len(ye), ye, c="red", marker=".", linewidths=0, s=0.1)

plt.title(r"$x_{n+1} = \lambda x_{n} (1 - x_{n})$")
plt.ylabel(r"$\lim_{n\to\infty}x_{n}$")
plt.xlabel(r"$\lambda$")
plt.savefig("logisticmaps/logisticmap9.png", dpi=1000)
plt.show()
