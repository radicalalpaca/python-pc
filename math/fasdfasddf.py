import numpy as np

m1 = np.array([(0.0, 0.0), (0.0, 0.16)], dtype=float)
p0 = np.array([2, 3])

print(np.dot(m1, p0) + np.array([0, 0.02]))