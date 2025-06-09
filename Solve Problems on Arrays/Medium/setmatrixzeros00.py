# Brute Force Approach

def markRow(matrix, i):
    m = len(matrix[0])
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(matrix, j):
    n = len(matrix)
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def SetMatrixToZeros(matrix):
    n = len(matrix)

    if n == 0:
        return
    
    m = len(matrix[0])
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(matrix, i)
                markCol(matrix, j)
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0


if __name__ == "__main__":
    matrix = [
        [1,1,1,1],
        [1,0,0,1],
        [1,1,0,1],
        [1,1,1,1]
    ]
    
    SetMatrixToZeros(matrix)
    
    for row in matrix:
        print(row)