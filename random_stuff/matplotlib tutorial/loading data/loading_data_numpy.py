import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt("example.txt", delimiter=",", unpack=True)
plt.plot(x, y, label="loaded from file")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Using numpy")

plt.legend()
#plt.show()
