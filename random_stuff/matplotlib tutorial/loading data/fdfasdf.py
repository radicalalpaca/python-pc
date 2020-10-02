import matplotlib.pyplot as plt
import numpy as np


source_url = "http://www1.maths.leeds.ac.uk/~voss/data/buffalo/buffalo.csv"
year, snowfall = np.loadtxt(source_url, skiprows=1, delimiter=",", unpack=True)
colors = np.where(snowfall > 118.11, "r", "k")

plt.scatter(year, snowfall, c=colors, s=5)
plt.xlabel("Year")
plt.ylabel("Snowfall (inches)")
plt.show()
