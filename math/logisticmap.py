import numpy as np
import matplotlib.pyplot as plt

#  X_(n+1) = r * X_(n) * (1 - X_(n))

r = 22.3
x0 = 0.5
n = 200

x = x0

ix = [x0]
iy = [0]

for i in range(n):
    x = r * x * (1 - np.tanh(x))
    ix.append(x)
    iy.append(i + 1)

plt.plot(iy, ix, linewidth=1)
plt.ylim(min(ix) - 0.1, max(ix) + 0.1)
plt.title(f"$\lambda$ = {r}")
plt.show()