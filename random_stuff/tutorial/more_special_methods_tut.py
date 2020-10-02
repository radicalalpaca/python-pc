def range_gen(end):
    current = 0
    while current < end:
        yield current
        current += 1

for i in range_gen(5):
    print(i)

x = 5
print(dir(x))