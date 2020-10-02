matrix = [[1, 2.0, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0][0])

for n in range(len(matrix)):
    print(*matrix[n])

elements = input("> ").split()
print(elements)
if all(isinstance(i, int) for i in elements):
    rows = [int(i) for i in elements]
    print(rows)
else:
    rows = [float(i) for i in elements]
    print(rows)