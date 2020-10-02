def congruence(m, a, b, c):
    for i in range(1, m):
        if i % b == a and i % c == a:
            print(i)
