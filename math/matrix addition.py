matrixA = []
matrixB = []

def matrix_input():
    global matrixA
    global matrixB
    nAm = [int(i) for i in input("Enter rows x columns: ").split()]
    for i in range(nAm[0]):
        rows = [int(i) for i in input().split()]
        matrixA.append(rows)

    nBm = [int(i) for i in input("Enter rows x columns: ").split()]
    for i in range(nBm[0]):
        rows = [int(i) for i in input().split()]
        matrixB.append(rows)

def matrix_addition():
    matrixC = []
    if len(matrixA) == len(matrixB) and len(matrixA[0]) == len(matrixB[0]):
        for n in range(len(matrixA)):
            matrixC.append([])
            for m in range(len(matrixA[0])):
                matrixC[n].append(matrixA[n][m] + matrixB[n][m])
        return matrixC
    else:
        print("error: return false")
        return False

def matrix_output(matrix):
    if matrix != False:
        for n in range(len(matrix)):
            print(*matrix[n])
    else:
        print("error")


if __name__ == '__main__':
    matrix_input()
    matrix_output(matrix_addition())
