import matplotlib.pyplot as plt

def add(a, b, *args):
    total = a + b
    for n in args:
        total += n
    return total


def will_survive(*names):
    for name in names:
        print(f"Will {name} survive?")


def func(positional_args, defaults, *args, **kwargs):
    pass


def recipe(*args, sep=" or "):
    return sep.join(args)


# print(*"fun")  # print("f", "u", "n")
# print(*[5, 10, 15])

def capital(**kwargs):
    for key, value in kwargs.items():
        print(f"{value} is the capital city of {key}.")


def say_bye(**names):
    for name in names:
        print(f"Au revoir {name}")
        print(f"See you on {names[name]['next appointment']}")
        print()


humans = {"Laura": {"next appointment": "Tuesday"},
          "Robin": {"next appointment": "Friday"}}

def graph(x, y):
    print(f"Function that graphs {str(x)} and {str(y)}.")
    plt.plot(x, y)
    plt.show()

x1 = [1, 2, 3]
y1 = [2, 3, 1]

graph_me = [x1, y1]

graph(*graph_me)
