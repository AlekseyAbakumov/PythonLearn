from sys import stdin
from copy import deepcopy
from functools import reduce
from operator import mul, sub


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class MatrixSolveError(BaseException):
    def __init__(self, error):
        self.error = error


class Matrix:
    def __init__(self, matr):
        self.body = deepcopy(matr)

    def __str__(self):
        result = ''
        body_lng = len(self.body)
        for k in range(body_lng):
            k_lng = len(self.body[k])
            for i in range(k_lng):
                result += str(self.body[k][i])
                if i != k_lng - 1:
                    result += '\t'
                elif k != body_lng - 1:
                    result += '\n'
        return result

    def size(self):
        return len(self.body), len(self.body[0])

    def __add__(self, other):
        if self.size() == other.size():
            result = []
            body_lng = len(self.body)
            for k in range(body_lng):
                line = []
                k_lng = len(self.body[k])
                for i in range(k_lng):
                    line.append(self.body[k][i] + other.body[k][i])
                result.append(line)
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = []
            body_lng = len(self.body)
            for k in range(body_lng):
                line = []
                k_lng = len(self.body[k])
                for i in range(k_lng):
                    line.append(self.body[k][i] * other)
                result.append(line)
        elif isinstance(other, Matrix):
            l1, v1 = self.size()
            l2, v2 = other.size()
            if v1 == l2:
                result = [[0 for row in range(v2)] for col in range(l1)]
                for i in range(l1):
                    for j in range(v2):
                        for k in range(v1):
                            result[i][j] += self.body[i][k] * other.body[k][j]
            else:
                raise MatrixError(self, other)
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        self.body = list(map(list, zip(*self.body)))
        return self

    @staticmethod
    def transposed(matrix):
        body1 = deepcopy(matrix.body)
        body1 = list(map(list, zip(*body1)))
        return Matrix(body1)

    @staticmethod
    def column(row):
        i = 0
        n = len(row)
        while not row[i] and i < n:
            i += 1
        return i if i < n else -1

    @staticmethod
    def sign(indexes):
        s = sum((0, 1)[x < y]
                for k, y in enumerate(indexes)
                for x in indexes[k + 1:])
        return (s + 1) % 2 - s % 2

    def det(self):
        m = self.body[:]
        n = len(m)

        indexes = [0 for _ in range(n)]

        for i in range(n):
            k = Matrix.column(m[i])
            for j in (x for x in range(n) if x != i):
                m[j] = tuple(map(sub, m[j],
                                 map(mul, m[i],
                                     [m[j][k] / m[i][k]] * (n + 1))))
            indexes[i] = k

        return reduce(mul,
                      (m[i][indexes[i]] for i in range(n)),
                      1) * Matrix.sign(indexes)

    def solve(self, line):
        n = len(self.body)
        tmp = list(zip(*self.body))
        b = line

        delta = self.det()
        if not delta:
            raise MatrixSolveError

        result = []
        for i in range(n):
            a = tmp[:]
            a[i] = b
            A = Matrix(a)
            result.append(A.det() / delta)
        return result


exec(stdin.read())
