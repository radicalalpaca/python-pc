import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

p0 = np.array([0, 0])
f1 = np.array([(0.0, 0.0), (0.0, 0.16)], dtype=float)
f2 = np.array([(0.85, 0.04), (-0.04, 0.85)], dtype=float)
f3 = np.array([(0.20, -0.26), (0.23, 0.22)], dtype=float)
f4 = np.array([(-0.15, 0.28), (0.26, 0.24)], dtype=float)

shape = [p0]
n = 10000000
p = p0

for i in range(n):
    choice = np.random.choice(4, p=[0.01, 0.85, 0.07, 0.07])
    if choice == 0:
        p = np.dot(f1, p) + np.array([0.0, 0.0])
        shape.append(p)
    elif choice == 1:
        p = np.dot(f2, p) + np.array([0.0, 1.6])
        shape.append(p)
    elif choice == 2:
        p = np.dot(f3, p) + np.array([0.0, 1.6])
        shape.append(p)
    elif choice == 3:
        p = np.dot(f4, p) + np.array([0.0, 0.44])
        shape.append(p)

plt.scatter(*zip(*shape), c="green", marker=".", linewidths=0, s=0.1)
plt.savefig("ferns/fern5.png", dpi=1000)
plt.show()
print(f"{time.time() - start_time} seconds")