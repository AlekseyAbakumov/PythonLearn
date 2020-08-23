from sys import stdin

stdin = open('input.txt', 'r', encoding='utf8')


class MatrixError(BaseException):
    def __init__(self, first_operand, other):
        self.matrix1 = first_operand
        self.matrix2 = other


class Matrix:
    def __init__(self, lists):
        tmp_size = [0, 0]
        self.data = []
        for row in lists:
            tmp_size[0] += 1
            tmp_size[1] = 0
            tmp_row = []
            for elem in row:
                tmp_row.append(elem)
                tmp_size[1] += 1
            self.data.append(tmp_row)
        self.sz = tuple(tmp_size)

    def __str__(self):
        out_str = ''
        for row in self.data:
            row_str = ''
            for elem in row:
                row_str += (str(elem) + '\t')
            row_str = row_str.strip()
            row_str += '\n'
            out_str += row_str
        out_str = out_str.strip()
        return out_str

    def size(self):
        return self.sz

    def __add__(self, other):
        result = []
        if isinstance(other, Matrix) and self.size() == other.size():
            for srow, orow in zip(self.data, other.data):
                row_res = []
                for selem, oelem in zip(srow, orow):
                    row_res.append(selem + oelem)
                result.append(row_res)
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        if isinstance(other, int) or isinstance(other, float):
            for row in self.data:
                row_res = []
                for elem in row:
                    row_res.append(elem * other)
                result.append(row_res)
        elif isinstance(other, Matrix) and self.sz[1] == other.sz[0]:
            tmp_matr = Matrix.transposed(other)
            for n_row in range(self.sz[0]):
                row_res = []
                for n_col in range(other.sz[1]):
                    row_res.append(sum(
                        map(lambda x, y: x * y, self.data[n_row],
                            tmp_matr.data[n_col])))
                result.append(row_res)
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        self.data = list(map(list, zip(*self.data)))
        rows = len(self.data)
        if rows:
            cols = len(self.data[0])
            self.sz = (rows, cols)
        else:
            self.sz = (rows, 0)
        return self

    @staticmethod
    def transposed(matrix):
        new_m = Matrix(matrix.data)
        return new_m.transpose()


exec(stdin.read())
