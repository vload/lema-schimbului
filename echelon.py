from my_util import read_matrix


def is_almost_0(a: float, e=1e-10):
    return -e < a and a < e


def reduced_echelon_form(matrix, e=1e-10):
    solved_cols = 0
    active_row = 0

    while active_row < len(matrix) and solved_cols < len(matrix[active_row]):
        row = active_row
        swap_required = False

        # find first non-zero under active-row
        while row < len(matrix) and is_almost_0(matrix[row][solved_cols], e):
            row = row + 1
            swap_required = True

        # if none we go to the next column
        if row == len(matrix):
            solved_cols = solved_cols + 1
            continue

        # swap
        if swap_required:
            for col in range(len(matrix[active_row])):
                matrix[row][col], matrix[active_row][col] = \
                    matrix[active_row][col], matrix[row][col]

        # factor
        if not is_almost_0(matrix[active_row][solved_cols], e):
            factor = 1.0 / matrix[active_row][solved_cols]
            for col in range(len(matrix[active_row])):
                matrix[active_row][col] = matrix[active_row][col] * factor

        # difference
        for diff_row in range(len(matrix)):
            if diff_row != active_row:
                factor = matrix[diff_row][solved_cols]
                for col in range(len(matrix[diff_row])):
                    matrix[diff_row][col] = matrix[diff_row][col] - \
                        factor * matrix[active_row][col]

        solved_cols = solved_cols + 1
        active_row = active_row + 1

    return matrix


if(__name__ == "__main__"):
    matrix = read_matrix("input.txt")

    matrix = reduced_echelon_form(matrix)

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
