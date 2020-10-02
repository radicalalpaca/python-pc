num = 2 ** 1000

def sum_digits():
    digits = []
    sum = 0
    for digit in str(num):
        sum += int(digit)
    print(sum)



if __name__ == '__main__':
    sum_digits()