import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

def get_iter(c:complex, thresh:int = 4, max_steps:int = 25):
    #  Z(n) = Z(n-1)^2 + c
    #  Z(0) = c
    z = c
    i = 1
    while i < max_steps and (z*z.conjugate()).real < thresh:
        z = z*z + c
        i += 1
    return i

def plotter(n, thresh, max_steps = 25):
    mx = 2.48 / (n - 1)
    my = 2.26 / (n - 1)
    mapper = lambda x, y: (mx * x - 2, my*y - 1.13)
    img = np.full((n, n), 255)

    for x in range(n):
        for y in range(n):
            it = get_iter(complex(*mapper(x, y)), thresh=thresh, max_steps=max_steps)
            img[y][x] = 255 - it

    return img

n = 1000
img = plotter(n, thresh=4, max_steps=50)
plt.imshow(img, cmap="nipy_spectral")
plt.axis("off")
plt.savefig("mandelbrots/mandelbrot10.png", dpi=1000)
plt.show()
print(f"{time.time() - start_time} seconds")