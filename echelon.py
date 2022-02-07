def is_almost_0(a: float):
    return -1e-10 < a and a < 1e-10


def get_reduced_echelon_form(matrix):
    solved_cols = 0
    active_row = 0

    while active_row < len(matrix) and solved_cols < len(matrix[active_row]):
        row = active_row
        swap_required = False

        # find first non-zero under active-row
        while row < len(matrix) and is_almost_0(matrix[row][solved_cols]):
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
        if not is_almost_0(matrix[active_row][solved_cols]):
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
    with open("input.txt") as f:
        n = int(f.readline())
        m = int(f.readline())
        matrix = []

        for i in range(n):
            temp = f.readline().split()
            temp = list(map(float, temp))
            matrix.append(temp)

    matrix = get_reduced_echelon_form(matrix)

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
