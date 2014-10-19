def rows(matrix):
    i = 1
    row0 = 0
    row0 = sum(matrix[0])
    while i < len(matrix):
        if sum(matrix[i]) != row0:
            return False
        i += 1
    return row0


def colums(matrix):
    i = 0
    j = 0
    col0 = 0
    while i < len(matrix):
        col0 += matrix[i][0]
        i += 1
    i = 1
    while i < len(matrix):
        col_i = 0
        while j < len(matrix):
            col_i += matrix[j][i]
            j += 1
        j = 0
        i += 1
        if col_i != col0:
            return False
    return col0


def f_diagonal(matrix):
    diag = 0
    i = 0
    while i < len(matrix):
        diag += matrix[i][i]
        i += 1
    return diag


def b_diagonal(matrix):
    diag = 0
    i = 0
    j = len(matrix) - 1
    while j >= 0:
        diag += matrix[j][i]
        i += 1
        j -= 1
    return diag


def magic_square(matrix):
    summ = b_diagonal(matrix)
    if summ != colums(matrix):
        return False
    if summ != f_diagonal(matrix):
        return False
    if summ != rows(matrix):
        return False
    return True


def main():
    print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))


if __name__ == '__main__':
    main()
