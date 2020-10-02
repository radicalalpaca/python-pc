from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(111, projection="3d")

x = list(range(1, 11))
y = np.random.randint(10, size=10)
z = np.random.randint(10, size=(1, 10))

ax1.plot_wireframe(x, y, z)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()