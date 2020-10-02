matrixA = []
matrixB = []

def matrix_input():
    global matrixA
    global matrixB
    nAm = [int(i) for i in input("Enter size of first matrix: > ").split()]
    for i in range(nAm[0]):
        rows = [int(i) for i in input("> ").split()]
        matrixA.append(rows)

    nBm = [int(i) for i in input("Enter size of second matrix: > ").split()]
    for i in range(nBm[0]):
        rows = [int(i) for i in input("> ").split()]
        matrixB.append(rows)

def matrix_output(matrix):
    if matrix != False:
        for n in range(len(matrix)):
            print(*matrix[n])
    else:
        print("error")

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
        print("The operation cannot be performed")

if __name__ == '__main__':
    matrix_input()
    matrix_output(matrix_multiplication())
