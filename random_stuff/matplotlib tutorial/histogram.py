import matplotlib.pyplot as plt
import numpy as np

population_ages = np.random.randint(5, 100, size=30)
bins = [i for i in range(0, 110, 10)]

plt.hist(population_ages, bins)
plt.xlabel("age")
plt.ylabel("Freq density")
plt.title("histogram of ages")


plt.show()
