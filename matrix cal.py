def matrix_init(choose, row, col):
    if choose == 'matrixA':
        A = [[0 for x in range(col)]for y in range(row)]
        return A
    if choose == 'matrixB':
        B = [[0 for x in range(col)]for y in range(row)]
        return B
    if choose == 'matrixC':
        C = [[0 for x in range(col)]for y in range(row)]
        return C
    if choose == 'matrixD':
        D = [[0 for x in range(col)]for y in range(row)]
        return D
    if choose == 'matrixE':
        E = [[0 for x in range(col)]for y in range(row)]
        return E


def assign_matrix():
    check = 0
    choose = input('Choose the slot you want to assign (matrixA to matrixE):')
    while choose not in ['matrixA', 'matrixB', 'matrixC', 'matrixD', 'matrixE']:
        choose = input(
            'There is no such slot, please choose again (matrixA to matrixE):')
    inp = input(
        'declare the dimension of the matrix (in term of row*column):').split('*')
    while check < 2:
        for x in inp:
            if x.isdigit():
                check = check + 1
        if check != 2:
            inp = input('incorrect format, plz input again:').split('*')
    row = int(inp[0])
    col = int(inp[1])
    matrix_init(choose, row, col)


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


def det(matrix):
    det_num = 0
    if len(matrix) == 2:
        output = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        return output
    else:
        for x in range(len(matrix)):
            temp_matrix = [sub[:] for sub in matrix]
            temp_matrix.remove(temp_matrix[x])
            for z in temp_matrix:
                z.pop(0)
            if x % 2 == 0:
                det_num = det_num + matrix[x][0]*det(temp_matrix)
            if x % 2 != 0:
                det_num = det_num - matrix[x][0]*det(temp_matrix)
        return det_num


if __name__ == '__main__':
    A = [[0, 1, 4, 2, 3], [4, 2, 0, 1, 5], [
        2, 2, 1, 0, 3], [3, 4, 5, 3, 0], [9, 5, 4, 3, 7]]
    # assign_matrix()
    # print('/n'.join([' '.join([''.format(item)for item in row])
    #       for row in list(matrix_init)]))
    # print(matrix_init)
    print(transpose(A))

    # test = 8
    # for x in B:
    #     if test in x:
    #         print(B.index(x),x.index(test))

    # multiply(A, B)
    # find_trace(B)

    # test for transpose
    # print('expected output: [[1,5,3],[4,4,8],[5,2,12]]')
    # print('actual output:', transpose(A))
