
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def matrix_input_1():
    global matrixA
    nAm = [int(i) for i in input("Enter size of matrix: > ").split()]
    for i in range(nAm[0]):
        elements = input("> ").split()
        if all(is_number(i) for i in elements):
            rows = [int(i) for i in elements]
        else:
            rows = [float(i) for i in elements]
        matrixA.append(rows)

def matrix_input_2():
    global matrixA
    global matrixB
    nAm = [int(i) for i in input("Enter size of first matrix: > ").split()]
    for i in range(nAm[0]):
        elements = input("> ").split()
        if all(is_number(i) for i in elements):
            rows = [int(i) for i in elements]
        else:
            rows = [float(i) for i in elements]
        matrixA.append(rows)

    nBm = [int(i) for i in input("Enter size of second matrix: > ").split()]
    for i in range(nBm[0]):
        elements = input("> ").split()
        if all(is_number(i) for i in elements):
            rows = [int(i) for i in elements]
        else:
            rows = [float(i) for i in elements]
        matrixB.append(rows)

def matrix_output(matrix):
    if matrix != False:
        for n in range(len(matrix)):
            print(*matrix[n])
    else:
        print("The operation cannot be performed")

def matrix_addition():
    if len(matrixA) == len(matrixB) and len(matrixA[0]) == len(matrixB[0]):
        matrixC = []
        for n in range(len(matrixA)):
            matrixC.append([])
            for m in range(len(matrixA[0])):
                matrixC[n].append(matrixA[n][m] + matrixB[n][m])
        return matrixC
    else:
        return False

def multiplication_by_constant():
    c = float(input("Enter constant: > "))
    matrixB = []
    for n in range(len(matrixA)):
        matrixB.append([])
        for m in range(len(matrixA[0])):
            matrixB[n].append(c * matrixA[n][m])
    return matrixB

def matrix_multiplication():
    matrixC = []
    if len(matrixA[0]) == len(matrixB):
        for i in range(len(matrixA)):
            matrixC.append([])
            for j in range(len(matrixB[0])):
                sum = 0
                for k in range(len(matrixB)):
                    sum += matrixA[i][k] * matrixB[k][j]
                matrixC[i].append(sum)
        return matrixC
    else:
        return False

if __name__ == '__main__':
    while True:
        matrixA = []
        matrixB = []
        print("")
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("0. Exit")
        user_choice = int(input("Your choice: > "))
        if user_choice == 1:
            matrix_input_2()
            matrix_output(matrix_addition())
        elif user_choice == 2:
            matrix_input_1()
            matrix_output(multiplication_by_constant())
        elif user_choice == 3:
            matrix_input_2()
            matrix_output(matrix_multiplication())
        elif user_choice == 0:
            break
        else:
            print("Choice invalid")
