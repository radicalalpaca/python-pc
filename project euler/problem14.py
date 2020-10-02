
def collatz():
    sequence = []
    lengths = []
    for number in range(1, 1000000):
        sequence.append(number)
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                sequence.append(number)
            else:
                number = (3 * number) + 1
                sequence.append(number)
        lengths.append(len(sequence))
        sequence = []
    return lengths

if __name__ == '__main__':
    m = max(collatz())
    print([i for i, j in enumerate(collatz()) if j == m])