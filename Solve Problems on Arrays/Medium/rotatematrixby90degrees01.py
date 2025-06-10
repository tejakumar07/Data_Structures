def rotate_matrix_90(matrix):

    n = len(matrix)
    m = len(matrix[0])
    if n == 0 or n!=m:
        return

    # Transverse the Matrix

    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse the Matrix
    for i in range(n):
        matrix[i].reverse()


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]

    rotate_matrix_90(matrix)

    for row in matrix:
        print(row)
