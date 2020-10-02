"""
Solves Mordell's equation.
"""


# noinspection PyCompatibility
def mordell(k, m):
    """
    Solves Mordell's equation: y = x^3 + k for integer k.

    :param k: Integer constant.
    :param m: Test integers up to but not including m.
    """
    for i in range(-m, m):
        for j in range(-m, m):
            if i * i == j * j * j + k:
                print(f"y = {i}, x = {j}")


if __name__ == '__main__':
    mordell(16, 1000)
