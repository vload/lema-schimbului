#!/usr/bin/env python
from echelon import reduced_echelon_form
from my_util import read_matrix


def inverse(matrix, e=1e-10):
    N = len(matrix)

    if len(matrix[0]) != N:
        raise ArithmeticError("Matrix is not invertible!")

    for i, line in enumerate(matrix):
        matrix[i] = line + [0] * N
        matrix[i][N + i] = 1

    matrix = reduced_echelon_form(matrix)

    for i, line in enumerate(matrix):
        for j, e in enumerate(line[:N]):
            if i != j:
                if e != 0:
                    raise ArithmeticError("Matrix is not invertible!")
            else:
                if e != 1:
                    raise ArithmeticError("Matrix is not invertible!")

    for i, line in enumerate(matrix):
        matrix[i] = line[N:]

    return matrix


if(__name__ == "__main__"):
    matrix = read_matrix("input.txt")

    try:
        matrix = inverse(matrix)

        # round the numbers:
        rounded = []
        for row in matrix:
            new_row = []
            for e in row:
                new_row.append(round(e, 4))

            rounded.append(new_row)

        # print the rounded form
        for row in rounded:
            print(row)

    except ArithmeticError:
        print("Matrix is not invertible!")
