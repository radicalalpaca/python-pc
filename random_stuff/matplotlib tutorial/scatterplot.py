import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(1, 9)]
y = np.random.randint(1, 9, 8)

plt.scatter(x, y, label="scatter", c="b")  # s - size of points

plt.legend()
plt.show()
