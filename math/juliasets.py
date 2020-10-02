import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

phi = (1 + 5 ** 0.5) / 2
n = 1000
abs_z_max = 2
num_iter_max = 2000
c = complex(np.e / np.pi, np.e / np.pi)
xmin, xmax = -1.5, 1.5
xwidth = xmax - xmin
ymin, ymax = -1.5, 1.5
yheight = ymax - ymin

julia = np.zeros((n, n))
for ix in range(n):
    for iy in range(n):
        num_iter = 0
        z = complex(ix / n * xwidth + xmin,
                    iy / n * yheight + ymin)

        while abs(z) <= abs_z_max and num_iter < num_iter_max:
            z = z**2 + c
            num_iter += 1

        ratio = num_iter / num_iter_max
        julia[iy, ix] = ratio

plt.imshow(julia, cmap="gist_ncar", origin="lower")
plt.title("c = e/pi + (e/pi)*i")
plt.axis("off")
plt.savefig("julia_sets/julia16.svg", dpi=1000)
plt.show()
print(f"{time.time() - start_time} seconds")
