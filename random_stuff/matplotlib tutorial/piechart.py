import matplotlib.pyplot as plt

slices = [7, 2, 2, 13]
activities = ["sleeping", "eating", "working", "playing"]
colors = ["c", "m", "r", "b"]

plt.pie(slices, labels=activities, colors=colors,
        startangle=90, explode=(0, 0.1, 0, 0),
        autopct="%1.1f%%")
plt.title("pie chart")

plt.show()
