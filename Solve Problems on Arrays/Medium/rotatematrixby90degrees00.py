# Brute Force Approach

def RotateMatrixBy90Degrees(matrix):
    n = len(matrix)
    m = len(matrix[0])
    if n == 0 or m != n:
        return
    
    rotated = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = matrix[i][j]
    
    return rotated

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    answer = RotateMatrixBy90Degrees(matrix)

    for row in answer:
        print(row)