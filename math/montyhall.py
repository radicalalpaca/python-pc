import matplotlib.pyplot as plt
import numpy as np

swap = False
n = 10000
wins = 0
losses = 0
prob_win = []
prob_lose = []


def game(strategy, num_doors):
    prize_door = np.random.randint(num_doors)
    choice = np.random.randint(num_doors)
    closed_doors = [x for x in range(num_doors)]

    while len(closed_doors) > 2:
        open_door = np.random.choice(closed_doors)

        if open_door == prize_door or open_door == choice:
            continue
        closed_doors.remove(open_door)

    if strategy:
        closed_doors.remove(choice)
        choice = closed_doors[0]

    return choice == prize_door


for i in range(n):
    if game(swap, 3):
        wins += 1
    else:
        losses += 1

    prob_win.append(wins / (i + 1))
    prob_lose.append(losses / (i + 1))

plt.plot(np.arange(1, n + 1), prob_win, c="blue", label="win %")
plt.ylim(0, 1)
plt.title("strategy: sticking")
plt.xlabel("n")
plt.axhline(y=1 / 3, c="black")

plt.legend()
plt.show()
