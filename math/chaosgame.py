import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

n = 1000000
fraction = 0.45

v1 = np.array([0, 0])
v2 = np.array([1, 0])
v3 = np.array([1 / 2, np.sqrt(3) / 2])

triangle = [v1, v2, v3]

s, t = sorted([np.random.random_sample(), np.random.random_sample()])
p = np.array((t - s) * v2 + (1 - t) * v3)
# plt.scatter(*p, c="red", s=10)

for i in range(n):
    vertex = np.random.choice([v1, v2, v3])
    point = p + fraction * (vertex - p)
    triangle.append(point)
    p = point


plt.scatter(*zip(*triangle), s=0.1, marker=".", linewidths=0)
plt.title("triangle, fraction=0.45")
plt.savefig("chaosgames/chaos14.png", dpi=1000)
plt.show()
print(f"{time.time() - start_time} seconds")