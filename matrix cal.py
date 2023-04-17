def find_trace(matrix):
    if len(matrix) != len(matrix[1]):
        print('Math error')
    else:
        trace = 0
        for i in range(len(matrix)):
            trace = trace + matrix[i][i]
        print('The trace of ', matrix, ' is ', trace)


def multiply(matrixA, matrixB):
    if len(matrixA[1]) != len(matrixB):
        print('Math error')
    else:
        matrixC = [[0 for x in range(len(matrixB[1]))]
                   for y in range(len(matrixA))]
        print(matrixC)
        temp = 0
        temp1 = 0
        for i in range(len(matrixA)):
            for j in range(len(matrixB[i])):
                temp1 = 0
                for a in (range(len(matrixA[1]))):

                    temp = 0
                    temp = matrixA[i][a] * matrixB[a][j]
                    temp1 = temp1 + temp

                matrixC[i][j] = temp1

        print('The product of ', matrixA, 'and ', matrixB, ' is ', matrixC)


def transpose(matrix):
    temp = 0
    k = 0
    for i in range(len(matrix)):

        for j in range(k, len(matrix[i])):
            temp = 0
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        k = k+1
    return matrix

# def reducerow(matrix):



if __name__ == '__main__':
    A = [[1, 4, 5], [5, 4, 2], [3, 8, 12]]
    B = [[2, 4], [8, 3], [4, 8]]
    test = 8
    for x in B:
        if test in x:
            print(B.index(x),x.index(test))
    

    # multiply(A, B)
    # find_trace(B)

    # test for transpose
    # print('expected output: [[1,5,3],[4,4,8],[5,2,12]]')
    # print('actual output:', transpose(A))
