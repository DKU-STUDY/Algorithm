import sys


class Matrix:
    def __init__(self):
        N, M = sys.stdin.readline().split()
        N, M = int(N), int(M)
        data = {}
        for j in range(N):
            row = sys.stdin.readline().split()
            for i in range(M):
                data[(i, j)] = int(row[i])

        self._N, self._M = N, M
        self._data = data

    def __str__(self):
        string = ('「' + ('     ' * (self._M + 1)) + '┐')
        for j in range(self._N):
            row = '│    '
            for i in range(self._M):
                minus_check = False
                row += str(self._data[(i, j)])
                if self._data[(i, j)] < 0:
                    minus_check = True
                if i < self._M - 1:
                    if minus_check:
                        row += '   '
                    else:
                        row += '    '
            row += '    │'
            string += ('\n' + row)
        string += ('\n' + '└' + ('     ' * (self._M + 1)) + '┘')
        return string


def dotmult(matrixA, matrixB):
    return_mat = ''
    for i in range(matrixA._N):
        row = ''
        for j in range(matrixB._M):
            ele = 0
            for k in range(matrixA._M):
                ele += (matrixA._data[(k, i)] * matrixB._data[(j, k)])
            row += (str(ele) + ' ')
        return_mat += (row + '\n')
    return return_mat


def solution():
    matrixA = Matrix()
    matrixB = Matrix()
    print(f'N,M = {matrixA._N}, {matrixA._M}\ndata = {matrixA._data}')
    print(f'N,M = {matrixB._N}, {matrixB._M}\ndata = {matrixB._data}')
    print(f'matrixA:\n{matrixA}')
    print(f'matrixB:\n{matrixB}')
    print(dotmult(matrixA, matrixB))


solution()
