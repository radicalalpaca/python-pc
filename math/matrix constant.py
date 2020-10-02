matrixA = []

def matrix_input():
    global matrixA
    nAm = [int(i) for i in input().split()]
    for i in range(nAm[0]):
        rows = [int(i) for i in input().split()]
        matrixA.append(rows)

def multiplication_by_constant():
    c = int(input())
    matrixB = []
    for n in range(len(matrixA)):
        matrixB.append([])
        for m in range(len(matrixA[0])):
            matrixB[n].append(c * matrixA[n][m])
    return matrixB

def matrix_output(matrix):
    if matrix != False:
        for n in range(len(matrix)):
            print(*matrix[n])
    else:
        print("error")

if __name__ == '__main__':
    matrix_input()
    matrix_output(multiplication_by_constant())