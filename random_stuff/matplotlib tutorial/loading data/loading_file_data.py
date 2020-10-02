import matplotlib.pyplot as plt
import csv

x = []
y = []

with open("example.txt", "r") as f:
    plots = csv.reader(f, delimiter=",")
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label="Loaded from csv")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Using built-in module")

plt.legend()
plt.show()
