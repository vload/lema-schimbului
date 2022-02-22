#!/usr/bin/env python
def read_matrix(filename: str):
    with open("input.txt") as f:
        matrix = []

        for line in f.readlines():
            temp = line.split()
            temp = list(map(float, temp))
            matrix.append(temp)

    return matrix
